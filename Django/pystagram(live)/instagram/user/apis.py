from django.core.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.models import CustomUser, Follow
from user.serializers import UserSignUpSerializer, UserMeReadSerializer, UserMeUpdateSerializer, \
    UserFollowReadSerializer


class UserSignUpAPIView(CreateAPIView):
    queryset =  CustomUser.objects.all() # Model
    serializer_class = UserSignUpSerializer # Serializer

class UserMeAPIView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    # serializer_class = UserMeReadSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 데이터 접근 가능
    authentication_classes = [JWTAuthentication]  # JWT 인증

    def get_object(self):
        # DRF 기본 동작
        # URL 통해 넘겨 받은 pk를 통해 queryset에 데이터를 조회
        # -> CustomUser.objects.all()
        return self.request.user  # 인증이 끝난 유저가 들어감.

    def get_serializer_class(self):
        # HTTP 메소드 별로 다른 Serializer 적용
        # -> 각 요청마다 입/출력에 사용되는 데이터의 형식이 다르기 때문

        if self.request.method == "GET":
            return UserMeReadSerializer

        elif self.request.method == "PATCH":
            return UserMeUpdateSerializer

        return super().get_serializer_class()

class UserFollowAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 데이터 접근 가능
    authentication_classes = [JWTAuthentication]  # JWT 인증

    def post(self, request, user_id):
        # 자기 자신을 팔로우 할 수 없다.
        if user_id == self.request.user.id:
            raise PermissionDenied("You can't follow yourself")

        # 멱등성 (idempotency) : 동일한 요청을 반복해도 결과가 일정한 성질
        follow, created = Follow.objects.get_or_create(user_id=user_id, follower_id=request.user.id)
        serializer = UserFollowReadSerializer(follow)
        if created:
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


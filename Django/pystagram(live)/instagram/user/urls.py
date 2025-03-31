from django.urls.conf import path

from user import apis

from rest_framework_simplejwt.views import TokenObtainPairView

from user import apis

urlpatterns = [
    # POST /users -> 회원가입
    path("", apis.UserSignUpAPIView.as_view(), name="user-sign-up"),
    # POST /users/login/ -> 로그인
    path("login/", TokenObtainPairView.as_view(), name="user_login"),
    # GET /users/me/ -> 내 프로필 조회
    # PATCH /users/me/ -> 내 프로필 수정
    path('me/', apis.UserMeAPIView.as_view(), name="user-me"),
    # POST /users/<int:pk>/follow/ -> 팔로우
    path("<int:user_id>/follow/", apis.UserFollowAPIView.as_view(), name="user-follow"),
]

# User API 설계
# - POST /users/: 회원가입
# - POST /users/login/: 로그인 (JWT 반환)
# - GET /users/me/: 내 프로필 조회
# - PATCH /users/me/: 내 프로필 수정
# - GET /users/<int:user_id>/: 다른 사람 프로필 조회
# - POST /users/<int:user_id>/follow/: 다른 사람 팔로우
# - DELETE /users/<int:user_id>/follow/: 다른 사람 언팔로우
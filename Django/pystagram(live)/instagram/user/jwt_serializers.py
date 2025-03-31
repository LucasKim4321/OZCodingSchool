# 커스텀 로그인 시리얼라이저
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = 'email'

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['user_name'] = user.username  # 토큰에 유저 이름을 함께 담아서 보냄
#
#         return token
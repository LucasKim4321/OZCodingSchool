from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from user.models import CustomUser, Follow

# 시리얼라이저 만드는 방법
# 1. Seriallizer
from django.contrib.auth.models import User
# 2. ModelSerializer

# Django Form
# 1. 데이터 입력을 받을 수 있고, 검증
# 2. HTML을 그려줄 수

class UserSignUpSerializer(serializers.ModelSerializer):
    # 입력, 출력 가능
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]
        # write_only_fields = ["password"]


    def create(self, validated_data):

        # create_user() -> 비밀번호 해싱
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # 비밀번호 자동으로 해싱
        )
        return user

class UserMeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class UserMeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "password"]

    def update(self, instance, validated_data):
        if password := validated_data.get("password"):
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)

class UserFollowReadSerializer(serializers.ModelSerializer):
    # 연결된 user에서 user_id를 가져옴.
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    follower_id = serializers.PrimaryKeyRelatedField(source="follower", read_only=True)

    class Meta:
        model = Follow
        fields = ["id","user_id","follower_id","created_at"]

# 데이터베이스
# PrimaryKey(고유키) -> id 컬럼(int, auto increment)
# 1 -> 2 -> 3 -> 4 -> 5 ...

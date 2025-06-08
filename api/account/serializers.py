from account.models import CustomUser
from rest_framework import serializers

class CustomUserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "user_type", "first_name", "last_name", "password", 'password2')
        read_only_fields = ("id", "user_type", )
        extra_kwargs = {
            'password2': {'write_only': True},
            'password': {'write_only': True},

        }

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("both password must be equal.")
        return attrs
    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


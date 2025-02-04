from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ["name","email","password","confirm_password","profile_pic","created_at"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    ## Validating that password
    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords must match."})
        return data

    ## Hashing the password
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
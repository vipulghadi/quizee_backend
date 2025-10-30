from rest_framework import serializers

class AdminLoginEmailPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email:
            raise serializers.ValidationError("Email address not provided.")
        if not password:
            raise serializers.ValidationError("Password not provided.")

        if len(password) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters.")

        if len(password) > 100:
            raise serializers.ValidationError("Password must be less than 100 characters.")

        return data
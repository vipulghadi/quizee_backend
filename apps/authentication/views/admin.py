from django.core.serializers import serialize
from rest_framework.views import APIView
from apps.core.api_response import api_response
from rest_framework import permissions, status
from ..services import AuthenticationService
from ..serializers import AdminLoginEmailPasswordSerializer

class AdminLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer=AdminLoginEmailPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        service = AuthenticationService()
        data = service.login_email_password(data["email"],data["password"],"ADMIN")
        print(data)
        return api_response(
            message="Login Successful",
            data=data,
            status_code=status.HTTP_200_OK,
            success=True,
            errors=[]
        )

class AdminOTPLoginView(APIView):
    permission_classes = [permissions.AllowAny]


from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.api_response import api_response

class TestAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        return api_response(
            message="ok",
            status_code=status.HTTP_200_OK,
            data={},
            success=True,
            errors=[]
        )

class CurrentUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return api_response(
            message="ok",
            status_code=status.HTTP_200_OK,
            data={},
            success=True,
            errors=[]
        )



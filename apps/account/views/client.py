from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from ..serializers import CurrentUserSerializer
from apps.core.api_response import api_response

class CurrentUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        serializer = CurrentUserSerializer(request.user)
        return api_response(
            message="current user",
            data=serializer.data,
            status_code=status.HTTP_200_OK,
            success=True
        )
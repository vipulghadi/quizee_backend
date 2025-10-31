from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from apps.core.api_response import  api_response
from apps.core.permissions import IsSuperAdmin

class UploadQuestionMaterialAPIView(APIView):
    permission_classes = (IsSuperAdmin,)

    def get(self,request):
        return api_response(
            message="ok",
            success=True,
            data={},
            status_code=200,
            errors=[]
        )

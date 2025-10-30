from rest_framework.response import  Response
def api_response(success=True,message="ok", status_code=200,data=None,errors=None):
    return Response( {
        "success": success,
        "message":message,
        "status_code":status_code,
        "data":data,
        "errors":errors
    })


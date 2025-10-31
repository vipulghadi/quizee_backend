
from django.db import DatabaseError, IntegrityError, OperationalError
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied ,ValidationError as DjangoValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied as DRFPermissionDenied,
    ValidationError,
    ParseError,
    NotFound
)
from rest_framework.response import Response
from rest_framework import status
from .api_response import api_response

def custom_exception_handler(exc, context):
    """
    Global DRF exception handler that catches most common Django/DRF/database errors.
    """
    print("-----------")
    response = exception_handler(exc, context)
    print(response)
    print((response))
    print(type(exc))

    if isinstance(exc, ValidationError):
        errors = []
        for field, messages in dict(exc.detail).items():
            for msg in messages:
                errors.append(str(msg))
        return api_response(
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Validation Error",
            success=False,
            errors=errors
        )

    # Custom handling
    elif isinstance(exc, ( DjangoValidationError, ParseError)):
        return api_response(
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST,
            message=str(exc.detail),
            success=False,
            errors=[]
        )

    elif isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        print(exc)

        return api_response(
            data=None,
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Authentication Failed",
            success=False,
            errors=['Authentication Failed']
        )


    elif isinstance(exc, (DRFPermissionDenied, PermissionDenied)):
        return api_response(
            data=None,
            status_code=status.HTTP_403_FORBIDDEN,
            message="You do not have permission to perform this action.",
            success=False,
            errors=[]
        )


    elif isinstance(exc, ObjectDoesNotExist):
        return api_response(
            data=None,
            status_code=status.HTTP_404_NOT_FOUND,
            message="Object Not Found",
            success=False,
            errors=[]
        )


    elif isinstance(exc, IntegrityError):
        return api_response(
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Integrity Error",
            success=False,
            errors=[]
        )


    elif isinstance(exc, OperationalError):
        return api_response(
            data=None,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            message="Database Operational Error",
            success=False,
            errors=[]
        )


    elif isinstance(exc, DatabaseError):
        return api_response(
            data=None,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Database Error",
            success=False,
            errors=[]
        )
    elif isinstance(exc,(Http404,NotFound)):
        return api_response(
            data=None,
            status_code=status.HTTP_404_NOT_FOUND,
            message=str(exc.detail),
            success=False,
            errors=[str(exc.detail)]
        )
    elif isinstance(exc,ValueError):
        return api_response(
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Value Error",
            success=False,
            errors=[]
        )


    else:
        print(exc)
        return api_response(
            data=None,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Internal Server Error",
            success=False,
            errors=[]
        )


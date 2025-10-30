from apps.account.models import UserModel
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

class AuthenticationService:
    def __init__(self):
        pass

    def login_email_password(self,email,password,role):
        user = UserModel.objects.filter(email=email).first()
        print(user)
        if not user:
            raise NotFound('User not found...')
        elif not user.check_password(password):
            raise AuthenticationFailed ("Invalid password...")

        elif user.is_active==False:
            raise AuthenticationFailed("User is not active...")

        tokens=self.generate_access_refresh_token(user)
        return {
            "id":user.id,
            "email":user.email,
            "access_token":tokens[0],
            "refresh_token":tokens[1]
        }

        return user

    def otp_login(self):pass

    def verify_new_user(self):pass

    def change_password(self):pass

    def forgot_password(self):pass

    def reset_password(self):pass

    def generate_access_refresh_token(self,user):
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return access_token,refresh_token







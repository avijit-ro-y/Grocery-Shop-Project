from rest_framework_simplejwt.tokens import RefreshToken

def generate_email_token(user):
    token = RefreshToken.for_user(user).access_token
    return str(token)
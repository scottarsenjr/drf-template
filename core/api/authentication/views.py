from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from core.api.common.swagger.tags import AUTHENTICATION_TAG


class ObtainView(TokenObtainPairView):
    @swagger_auto_schema(tags=[AUTHENTICATION_TAG])
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class RefreshView(TokenRefreshView):
    @swagger_auto_schema(tags=[AUTHENTICATION_TAG])
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class VerifyView(TokenVerifyView):
    @swagger_auto_schema(tags=[AUTHENTICATION_TAG])
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)

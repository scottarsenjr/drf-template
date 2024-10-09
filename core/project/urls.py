from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from core.api.common.swagger.schemes import APISchemeGenerator

swagger_view = get_schema_view(
    openapi.Info(
        title='Missout API',
        default_version='v1',
        description='Swagger for Missout API',
        contact=openapi.Contact(email='scxrchybeats@gmail.com'),
    ),
    public=True,
    generator_class=APISchemeGenerator,
)


handler404 = 'core.api.views.custom404'

urlpatterns = [
    path('swagger/', swagger_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', swagger_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('core.api.urls'), name='api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

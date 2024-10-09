from django.urls import path

from . import views

urlpatterns = [
    path('token/', views.ObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.RefreshView.as_view(), name='token_refresh'),
    path('token/verify/', views.VerifyView.as_view(), name='token_verify'),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from customers import views


router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('drf_registration.urls')),
    path('admin/', admin.site.urls),
]
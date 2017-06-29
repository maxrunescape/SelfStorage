from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter
# from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'api', views.ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from rest_framework import routers
from django.conf.urls import url, include
from . import views

app_name = 'price'

router = routers.SimpleRouter()
router.register(r'monthly', views.MonthlyViewSet)
router.register(r'daily', views.DailyViewSet)
router.register(r'compat', views.CompatViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

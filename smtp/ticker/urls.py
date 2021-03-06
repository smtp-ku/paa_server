from rest_framework import routers
from django.conf.urls import url, include
from . import views

app_name = 'ticker'

router = routers.DefaultRouter()
router.register(r'', views.TickerView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

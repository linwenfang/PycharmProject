from django.conf.urls import url
from . import views
urlpatterns = [
    url('^index/$',views.index),
    url('^detail/$',views.detail),
    url('^book/$',views.book),
    url('^(\d+)/$',views.detail)
]
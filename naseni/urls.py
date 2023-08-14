from django.urls import path

from naseni.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

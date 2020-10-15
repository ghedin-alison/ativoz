from django.urls import path
from .views import IndexView, SaibaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('saiba/', SaibaView.as_view(), name='saiba'),
]

from django.urls import path
from .import views as forum_views

urlpatterns = [
    path('', forum_views.home, name='home'),
    path('question/<int:pk>/', forum_views.detail, name='detail'),
]
#static url

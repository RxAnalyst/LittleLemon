#define URL route for index() view
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)



urlpatterns = [
    
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurant/menu/', views.MenuView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]


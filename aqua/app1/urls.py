from django.urls import path
from . import views
from .views import RegisterView,LoginView,Model1View,GetModel1View


urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('signup_api/', RegisterView.as_view(), name='signup_api'),
    path('login_api/', LoginView.as_view(), name='login_api'),
    path('post_data/', Model1View.as_view(), name='post_data'),
    path('get_data/<str:device_id>/', GetModel1View.as_view(), name='get_data'),


]
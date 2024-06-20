from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# from django.urls import reverse_lazy

# LOGIN_URL = reverse_lazy('login')
# LOGOUT_URL = reverse_lazy('logout')
# LOGIN_REDIRECT_URL = reverse_lazy('')

urlpatterns = [
    path('home/', views.home, name='home'),
    path('integration/', views.integration, name='integration'),
    path('', views.login_view, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('login', views.insta_login, name='insta_login'),
    path('instagram/', views.instagram_scrapper, name='instagram'),
    # path('followings', views.get_followers, name='user_followers'),
    # path('followers', views.get_following, name='user_followings'),
    path('user_profile', views.user_details, name='user_profile'),
    path('proxy-instagram-image/', views.proxy_instagram_image, name='proxy_instagram_image'),
    path('followers', views.get_followers, name='user_followers'),
    path('followings', views.get_followings, name='user_followings'),



    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]




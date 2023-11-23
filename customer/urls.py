
from customer import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_user, name='login' ),
    path('logout/', views.logout_user, name='logout' ),
    path('registration/', views.register_user, name='register_user' )
]
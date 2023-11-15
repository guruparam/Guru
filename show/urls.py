from show import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.displayview, name='Main_page' ),
    path('msg1', views.msg, name='message' ),
    path('create_brand/', views.create_brand, name='Create_brand' ),
    path('create_model/', views.create_model, name='Create_model' ),
    path('update_model/', views.update_model, name='Update_model' ),
    path('list_brand/', views.list_brand, name='List_brand' ),
    path('list_model/', views.list_model, name= 'List_model' ),
    path('list_model/<str:brand_id>/', views.list_model1, name= 'List_model1' ),
    path('sell/<str:mname>', views.transaction, name= 'transaction' ),
    path('data', views.data, name='data' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
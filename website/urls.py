from django.urls import path
from website.views import contact, test, sevil, about, index

app_name = 'website' 

urlpatterns = [
    
    path('test/', test , name='test'),
    path('sevil/', sevil , name='sevil'),
    path('about/', about , name='about'),
    path('index/', index , name='index'),
    path('contact/', contact , name='hadis'),
   
]
from django.urls import path
from .views import (productslistapi, productdetailapi, productcreateapi,
                    productupdateapi, productdeleteapi)
app_name = 'store'

urlpatterns = [
    path('',productslistapi, name='api_list'),
    path('<int:id>/',productdetailapi, name='api_detail'),
    path('createapi/',productcreateapi,name='api_create'),
    path('updateapi/<int:id>/',productupdateapi, name='api_update'),
    path('deleteapi/<int:id>/',productdeleteapi, name='api_delete'),

]

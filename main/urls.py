from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='createtask'),
    path('product', views.product, name='product'),
    path('product_list', views.product_list, name='product_list'),
    path('order', views.order, name='order'),
    path('order_list', views.order_list.as_view(), name ='order_list'),

    path('add_product', views.add_product.as_view(), name='add_product'),
    path('edit_product', views.edit_product, name='edit_product'),
    path('add_product_count', views.add_product_count, name='add_product_count'),
    path('add_product_count_page', views.add_product_count_page, name='add_product_count_page'),
    path('product/<int:pk>/', views.product_page.as_view(), name='product_page'),
    path('order/<int:pk>/', views.order_page.as_view(), name='order_page'),

    path('change_order_status', views.change_order_status, name='change_order_status'),
    path('filter_order_status', views.filter_order_status.as_view(), name='filter_order_status'),

    path('search_product_list', views.search_product_list.as_view(), name='search_product_list'),
    path('search_add_product', views.search_add_product.as_view(), name='search_add_product'),
    path('delete_product', views.delete_product, name='delete_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
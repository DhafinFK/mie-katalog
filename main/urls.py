from django.urls import path
from . import views

app_name = "mie"
urlpatterns = [
    path('', views.show_katalog, name="katalog"),
    path('random/', views.random, name="random"),
    path('create-mie/', views.create_Indomie, name="create-mie"),
    path('xml/', views.show_xml, name='show_xml'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/', views.show_json, name='show_json'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('create-mie-ajax/', views.add_mie_by_ajax, name="mie_ajax"),
    path('get-mie/', views.get_mie_json, name="get_mie_json"),
    path('create-flutter/', views.create_product_flutter, name='create_product_flutter'),
]

from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView,

)


urlpatterns = [

    path('<int:pk>/edit/',ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('<int:pk>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('<int:clientpk>/edit_comment/<int:pk>', CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:clientpk>/delete_comment/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),

    path('<int:pk>/add_vehicle/', VehicleCreateView.as_view(), name='add_vehicle'),
    path('<int:clientpk>/edit_vehicle/<int:pk>', VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('<int:clientpk>/delete_vehicle/<int:pk>', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('', ClientListView.as_view(), name='client_list'),


]

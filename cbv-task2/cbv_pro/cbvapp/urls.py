from . import views
from django.urls import path


urlpatterns = [
    path('laptop/',views.laptopview.as_view(),name='laptop'),
    path('show/',views.showlaptopview.as_view(),name='show_lap'),
    path('delete/<int:i>/',views.deleteview.as_view(),name='delete'),
    path('update/<int:i>/',views.updateview.as_view(),name='update'),
]
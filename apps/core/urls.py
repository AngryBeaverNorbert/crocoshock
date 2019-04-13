from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [

    path('list/', views.CoreHomeView.as_view()),
    # path('list/c/', views.BrandsListClientView.as_view(), name='home_client'),
    # # api
    # path('brand-logo/', views.UploadView.as_view()),
]

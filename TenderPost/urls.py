from django.urls import path
from TenderPost import views as tenderpost_views
app_name = 'tender'

urlpatterns = [
    path('post/', tenderpost_views.postview, name='tender-post'),
    path('post-detail/<int:pk>', tenderpost_views.postdetail, name='post-detail')
]


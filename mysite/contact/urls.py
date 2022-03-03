from django.urls import path, include
from .views import ContactPageView, thanks

urlpatterns = [
    path('', ContactPageView.as_view(),name='contact'),
    path('thanks', thanks,name='thanks'),
    path('send-message', ContactPageView.as_view(),name='send_message'),
]
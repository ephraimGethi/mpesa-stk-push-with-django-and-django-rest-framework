from django.urls import path, include
from . import views
from django.urls import path
from .views import MpesaPaymentView, StkPushCallbackView


urlpatterns = [
    path('', views.index, name='index'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
    path('mpesa-payment/', MpesaPaymentView.as_view(), name='mpesa-payment'),
    path('mpesa-callback/', StkPushCallbackView.as_view(), name='stk-callback'),
]
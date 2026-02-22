from django.urls import path
from .views import predict_price, model_info, prediction_history, health_check

urlpatterns = [
    path('predict/', predict_price, name='predict_price'),
    path('model-info/', model_info, name='model_info'),
    path('prediction-history/', prediction_history, name='prediction_history'),
    path('health-check/', health_check, name='health_check'),
]
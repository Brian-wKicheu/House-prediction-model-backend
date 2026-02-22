from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import HouseFeaturesSerializer, PredictionResponseSerializer, PredictionHistorySerializer
from .models import PredictionHistory
from .ml_service import MLModdelService

ml_service = MLModdelService()

@api_view(['POST'])
def predict_price(request):
    serializer = HouseFeaturesSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {"error": "Invalid input data", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        features = serializer.validated_data
        predict_result = ml_service.predict(features)

        prediction_history = PredictionHistory.objects.create(
            **features,
            predicted_price = predict_result['predicted_price']
        )

        response_serializer = PredictionResponseSerializer(predict_result)

        return Response(
                {'success': True,
                'data': response_serializer.data,
                'history_id': prediction_history.id
                },status=status.HTTP_200_OK
            )
    
    except Exception as e:
        return Response(
            {"error": "Prediction failed", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    

@api_view(['GET'])
def model_info(request):
    try:
        info = ml_service.get_model_info()
        return Response({
            'success': True,
            'data': info
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {"error": "Failed to retrieve model info", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@api_view(['GET'])
def prediction_history(request):
    try:
        limit = int(request.query_params.get('limit', 10))
        predictions = PredictionHistory.objects.all()
        serializer = PredictionHistorySerializer(predictions, many=True)
        return Response(
            {
            'success': True,
            'count': len(serializer.data),
            'data': serializer.data
            }, status=status.HTTP_200_OK
        )
    
    except Exception as e:
        return Response(
            {"error": "Failed to retrieve prediction history", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@api_view(['GET'])
def health_check(request):
    return Response(
        {
        'status': 'healthy',
        'service': 'House Price Prediction API',
        'model_loaded': ml_service._model is not None
         
         },status=status.HTTP_200_OK
    )
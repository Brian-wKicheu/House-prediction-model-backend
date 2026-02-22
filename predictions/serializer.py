from rest_framework import serializers
from .models import PredictionHistory

class HouseFeaturesSerializer(serializers.Serializer):
    square_feet = serializers.IntegerField(min_value=100, max_value=1000)
    bedrooms = serializers.IntegerField(min_value=1, max_value=10)
    bathrooms = serializers.FloatField(min_value=1.0, max_value=10.0)
    age_years = serializers.IntegerField(min_value=0, max_value=150)

    # garage: if this is YES/NO, keep BooleanField with no min/max
    garage = serializers.BooleanField()

    lot_size_sqft = serializers.FloatField(min_value=500.0, max_value=5000.0)
    floors = serializers.IntegerField(min_value=1, max_value=10)
    crime_rate = serializers.FloatField(min_value=0.0, max_value=20.0)
    school_rating = serializers.FloatField(min_value=1.0, max_value=10.0)
    distance_to_city_miles = serializers.FloatField(min_value=0.0, max_value=100.0)

    # booleans: remove min/max
    has_pool = serializers.BooleanField()
    has_fireplace = serializers.BooleanField()
    has_renovated = serializers.BooleanField()

    neighborhood_quality = serializers.IntegerField(min_value=1, max_value=5)


class PredictionResponseSerializer(serializers.Serializer):
    predicted_price = serializers.FloatField()
    model_name = serializers.CharField()
    confidence_score = serializers.FloatField()
    features_used = serializers.DictField()


class PredictionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = '__all__'
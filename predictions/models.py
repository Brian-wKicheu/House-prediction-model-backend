from django.db import models

class PredictionHistory(models.Model):
    square_feet = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    age_years = models.IntegerField()
    garage = models.BooleanField()
    lot_size_sqft = models.FloatField()
    floors = models.IntegerField()
    crime_rate = models.FloatField()
    school_rating = models.FloatField()
    distance_to_city_miles = models.FloatField()
    has_pool = models.BooleanField()
    has_fireplace = models.BooleanField()
    has_renovated = models.BooleanField()
    neighborhood_quality = models.IntegerField()
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Prediction Histories"

    def __str__(self):
        return f"Prediction ${self.predicted_price:,.2f} - {self.created_at}"
    
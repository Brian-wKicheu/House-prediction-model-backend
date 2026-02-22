import pickle
import os
from pyexpat import features
import pandas as pd
from django.conf import settings

class MLModdelService:
    _instance = None
    _model = None
    _scaler = None
    _feature_names = None
    _metadata = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MLModdelService, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance
    
    def _load_model(self):
        base_path = os.path.join(settings.BASE_DIR, 'predictions', 'ml_models')# folder to store model and scaler

        try:
            # Load the trained model
            with open(os.path.join(base_path, 'house_price_model.pkl'), 'rb') as file:
                self._model = pickle.load(file)

            # Load the scaler
            with open(os.path.join(base_path, 'scaler.pkl'), 'rb') as file:
                self._scaler = pickle.load(file)

            # Load Feature names
            with open(os.path.join(base_path, 'feature_names.pkl'), 'rb') as file:
                self._feature_names = pickle.load(file)

            # Load metadata
            with open(os.path.join(base_path, 'model_metadata.pkl'), 'rb') as file:
                self._metadata = pickle.load(file)
            
            print("Models loaded successfully.")
            print(f"Model: {self._metadata['model_name']}")
            print(f"Test R2 : {self._metadata['test_r2']:.4f}")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise 

    def predict(self, features_dict):
        try:
            features_df = pd.DataFrame([features_dict])[self._feature_names]

            features_scaled = self._scaler.transform(features_df)

            predicted_price = self._model.predict(features_scaled)[0]

            confidence = self._metadata['test_r2']

            return {
                'predicted_price': float(predicted_price),
                'model_name': self._metadata['model_name'],
                'confidence_score': float(confidence)
            }
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")
        
    def get_model_info(self):
        return {
            'model_name': self._metadata['model_name'],
            'test_r2_score': self._metadata['test_r2'],
            'tesst_rmse': self._metadata['test_mse'],
            'test_mae': self._metadata['test_mae'],
            'training_samples': self._metadata['training_samples'],
            'feature_names': self._feature_names
        }
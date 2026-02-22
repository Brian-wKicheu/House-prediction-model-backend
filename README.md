# House Price Prediction API (Django + ML) — Local Setup Guide

This project is a **Django REST API** that predicts house prices using a **trained ML model saved as a pickle file**, and stores each prediction in a `PredictionHistory` database table. A frontend (React + Tailwind) can interact with the API endpoints to submit features and fetch prediction history.

---

## Table of Contents
- [What You’ll Build](#what-youll-build)
- [Prerequisites](#prerequisites)
- [Install Python](#install-python)
- [Create a Virtual Environment (Recommended)](#create-a-virtual-environment-recommended)
- [Install Jupyter Notebook Locally](#install-jupyter-notebook-locally)
- [Install Dependencies](#install-dependencies)
- [What Each Dependency Does](#what-each-dependency-does)
- [Project Workflow (How the Django API is Built)](#project-workflow-how-the-django-api-is-built)
- [Run Django Locally](#run-django-locally)
- [API Endpoints](#api-endpoints)
- [Testing With Postman](#testing-with-postman)
- [requirements.txt Example](#requirementstxt-example)
- [Common Issues](#common-issues)

---

## What You’ll Build

✅ A machine learning prediction API that:
- Accepts house features via `POST /predict/`
- Returns a response like:
  ```json
  {
    "predicted_price": 123456.78,
    "model_name": "RandomForestRegressor",
    "confidence_score": 0.87,
    "features_used": { ... }
  }
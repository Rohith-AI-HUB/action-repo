#!/usr/bin/env python3
"""
Configuration settings for the sample application
"""

# Application Information
APP_NAME = "GitHub Webhook Test Application"
VERSION = "1.0.0"
DESCRIPTION = "Sample application for testing GitHub webhooks"

# Application Settings
DEBUG_MODE = True
LOG_LEVEL = "INFO"

# Sample Configuration Values
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
BUFFER_SIZE = 1024

# Environment Settings
SUPPORTED_ENVIRONMENTS = ["development", "staging", "production"]
DEFAULT_ENVIRONMENT = "development"

# Sample API Configuration
API_ENDPOINTS = {
    "development": "https://dev-api.example.com",
    "staging": "https://staging-api.example.com", 
    "production": "https://api.example.com"
}

# Feature Flags
FEATURES = {
    "user_authentication": True,
    "data_validation": True,
    "advanced_logging": False,
    "experimental_features": False
}

# Sample Database Configuration (for demonstration)
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "name": "webhook_test_db",
    "timeout": 30
}

# Webhook Configuration Info
WEBHOOK_INFO = {
    "supported_events": ["push", "pull_request", "merge"],
    "endpoint": "https://your-webhook-endpoint.ngrok.io/webhook",
    "content_type": "application/json"
}
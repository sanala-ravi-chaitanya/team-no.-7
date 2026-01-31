"""
Configuration management for Kisan Call Centre Assistant
Loads environment variables and provides configuration constants
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Groq Model Configuration
    GROQ_MODEL = "llama-3.3-70b-versatile"  # Llama 3.3 70B Versatile
    MAX_TOKENS = 1024
    TEMPERATURE = 0.7
    
    # Application Settings
    APP_TITLE = "🌾 Kisan Call Centre Query Assistant"
    PAGE_TITLE = "Kisan Call Centre Assistant"
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        if not cls.GROQ_API_KEY:
            return False, "GROQ_API_KEY not found in environment variables"
        if cls.GROQ_API_KEY == "your-groq-api-key-here":
            return False, "Please replace 'your-groq-api-key-here' with your actual API key"
        return True, "Configuration valid"


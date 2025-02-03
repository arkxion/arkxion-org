"""Development configuration."""

from config.base import Config


class DevelopmentConfig(Config):
    """Development-specific configurations."""

    DEBUG = True
    SECRET_KEY = "development-secret-key"

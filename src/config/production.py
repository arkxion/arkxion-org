"""Production configuration."""

from config.base import Config


class ProductionConfig(Config):
    """Production-specific configurations."""

    DEBUG = False
    SECRET_KEY = "production-secret-key"

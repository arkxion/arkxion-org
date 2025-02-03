from flask import Flask, request, send_from_directory, redirect
from flask_babel import Babel
import os


# Application Factory Function
def create_app(config_name: str = "development") -> Flask:
    app = Flask(__name__)

    # Load environment-specific configuration
    if config_name == "production":
        app.config.from_object("config.production.ProductionConfig")
    elif config_name == "development":
        app.config.from_object("config.development.DevelopmentConfig")
    else:
        raise ValueError(f"Unknown configuration: {config_name}")

    # Initialize Babel for multilingual support
    def get_locale():
        lang = request.view_args.get("lang")  # Get language code from the URL path
        if lang:
            return lang
        return request.accept_languages.best_match(["en", "ja"], default="en")

    babel = Babel(app, locale_selector=get_locale)

    # Redirect users to the appropriate language-based URL based on browser settings
    @app.route("/")
    def index():
        """Redirects root (/) access to the appropriate language-based URL based on browser preferences."""
        preferred_lang = request.accept_languages.best_match(["en", "ja"], default="en")
        return redirect(f"/{preferred_lang}/")

    # 🔥 Delayed import of `home_bp` to prevent circular imports
    from app.views.home import home_bp  # noqa: E402

    app.register_blueprint(home_bp, url_prefix="/<lang>")
    return app

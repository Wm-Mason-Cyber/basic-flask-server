from flask import Flask

# Factory function to create Flask app
# This pattern is recommended for larger apps and testing

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'classroom-demo-key'  # Not for production!

    # Import and register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

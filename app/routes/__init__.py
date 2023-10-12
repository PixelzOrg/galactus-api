from app import server
from app.routes.generationRoutes import generate
from app.routes.healthRoutes import health_check

print("Registering blueprints...")

server.register_blueprint(generate, url_prefix="/")
server.register_blueprint(health_check, url_prefix="/")
from flask import Flask, jsonify
from db import db
from flask_smorest import Api
import os
from Chapters.chapter_logic import blp as ChapterBluePrint
from Certificate.certificate_logic import blp as CertificateBluePrint
from flask_migrate import Migrate

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_VERSION"] = os.getenv("API_VERSION", "v1")
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Chapter API's"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://finance_database_owner:gA38riEosFkl@ep-summer-glitter-a5lo1tfv.us-east-2.aws.neon.tech/finance_database")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    api.register_blueprint(ChapterBluePrint)
    api.register_blueprint(CertificateBluePrint)
    @app.errorhandler(Exception)
    def handle_error(e):
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=80)

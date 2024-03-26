from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
import os
import json
from CertificateGenerator.main import make_certificates


blp = Blueprint("Certificate", __name__, "For Generating Certificate")

@blp.route("/api/v1/finance/get_certificate")
class CertificateMaker(MethodView):
    def post(self):
        data = request.json
        name = data.get('name')
        if name is not None and name != "":
            base64_url = make_certificates(name)
            return jsonify({
                'data' : {
                    'base64_url' : base64_url
                }
            }), 201
        else:
            abort(500, message={
                "error" : "name not found"
            })

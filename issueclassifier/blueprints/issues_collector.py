# coding: utf-8
# import os
# from werkzeug import secure_filename
from flask import (
    Blueprint, request, render_template, jsonify
    # , current_app, send_from_directory, 
)
# from ..db import get_table

issues_collector_blueprint = Blueprint('issues_collector', __name__)

@issues_collector_blueprint.route("/issuescollector")
def index():
    # noticias = get_table('noticias')
    # todas_as_noticias = noticias.all()
    return jsonify({'teste': 'Funcionou galo'})

# coding: utf-8
import requests
from flask import (
    Blueprint, request, render_template, jsonify
)
from github import Github

issues_collector_blueprint = Blueprint('issues_collector', __name__)

@issues_collector_blueprint.route("/issuescollector")
def index():
    access_token = 'TOKEN_HERE'

    gh = Github(access_token, base_url='https://api.github.com')

    gh.get_repo('REPO_HERE')
    
    return jsonify({'funcionou':'Sim, é claro..'})
from flask import Flask, jsonify,
from playerDAO import PlayerDAO
from playerStatsDAO import PlayerStatsDAO

app = Flask(__name__, static_url_path='', static_folder='static_pages')

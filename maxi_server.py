from flask import Flask, request, jsonify, render_template, redirect, url_for, abort
from playerDAO import PlayerDAO
from playerStatsDAO import PlayerStatsDAO

app = Flask(__name__, static_url_path='', static_folder='static_pages')

playerdao = PlayerDAO()
playerstatsdao = PlayerStatsDAO()

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != '' or request.form['password'] != '':
#             username = request.form['username']
#             password = request.form['password']
#             foundUser = playerdao.checkUser(username, password)  
#             if not foundUser:
#                 error = 'Invalid Credentials. Please try again.'

#         else:
#             return error
#     return render_template('login.html', error=error)


@app.route('/players')
def get_all_players():
    return jsonify(playerdao.getAll())

@app.route('/players/<int:id>')
def find_player_by_id(id):
    found_player = playerdao.findByID(id)
    if not found_player:
        abort(400)
    return jsonify(found_player)

@app.route('/players', methods=['POST'])
def create_player():
    if not request.json:
        abort(400)
    player_data = {
        "Full_Name": request.json["Full_Name"],
        "Age": request.json["Age"],
        "Nationality": request.json["Nationality"],
    }
    return jsonify(playerdao.create(player_data))

@app.route('/playerstats')
def get_all_playerstats():
    return jsonify(playerstatsdao.getAll())

@app.route('/playerstats/<int:id>')
def find_playerstats_by_id(id):
    found_playerstats = playerstatsdao.findByID(id)
    if not found_playerstats:
        abort(400)
    return jsonify(found_playerstats)

@app.route('/playerstats', methods=['POST'])
def create_playerstats():
    if not request.json:
        abort(400)
    playerstats_data = {
        "Full_Name": request.json["Full_Name"],
        "Prize_Money": request.json["Prize_Money"],
        "Year": request.json["Year"],
    }
    return jsonify(playerstatsdao.create(playerstats_data))

if __name__ == "__main__":
    app.run(debug=True)

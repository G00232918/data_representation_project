from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from playerDAO import PlayerDAO
from playerStatsDAO import PlayerStatsDAO

app = Flask(__name__, static_url_path='', static_folder='static')

PlayerDAO = PlayerDAO()
PlayerStatsDAO = PlayerStatsDAO()

auth = HTTPBasicAuth()


# https://stackoverflow.com/questions/57218553/flask-restul-basic-authentication
# login details defined
USER_DATA = {
    "user": "password"
}

@auth.verify_password
def verify_password(username, password):
    if username in USER_DATA and USER_DATA[username] == password:
        return username

@app.route('/')
@auth.login_required
def home():
    return app.send_static_file('snooker_loot.html')
    
    
@app.route('/players', methods=['GET'])
def getAll():
    results = PlayerDAO.getAll()
    return jsonify(results)
    
@app.route('/players/<int:id>')
def find_player_by_id(id):
    found_player = PlayerDAO.findByID(id)
    if not found_player:
        abort(404)
    return jsonify(found_player)

@app.route('/players', methods=['POST'])
def create_player():
    if not request.json:
        abort(400)
    player = {
        "Full_Name": request.json["Full_Name"],
        "Age": request.json["Age"],
        "Nationality": request.json["Nationality"],
    }
    values =(player['Full_Name'],player['Age'],player['Nationality'])
    newId = PlayerDAO.create(values)
    player['id'] = newId
    return jsonify(player)

@app.route('/players/<int:id>', methods=['PUT'])
def update(id):
    foundPlayer = PlayerDAO.findByID(id)
    if not foundPlayer:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Age' in reqJson and type(reqJson['Age']) is not int:
        abort(400)
    if 'Full_Name' in reqJson:
        foundPlayer['Full_Name'] = reqJson['Full_Name']
    if 'Age' in reqJson:
        try:
            foundPlayer['Age'] = int(reqJson['Age'])
        except ValueError:
            abort(400)

    if 'Nationality' in reqJson:
        foundPlayer['Nationality'] = reqJson['Nationality']
    values = (foundPlayer['Full_Name'], foundPlayer['Age'], foundPlayer['Nationality'], foundPlayer['id'])
    PlayerDAO.update(values)
    return jsonify(foundPlayer)




@app.route('/players/<int:id>' , methods=['DELETE'])
def delete(id):
    PlayerDAO.delete(id)
    return jsonify({"done":True})

# playerstats table calls

@app.route('/playerstats')
def getAllPlayerStats():
    try:
        results = PlayerStatsDAO.getAll()
        return jsonify(results)
    except Exception as e:
        print(f"Error getting playerstat: {e}")
        abort(500)

@app.route('/playerstats/<int:id>')
def find_playerstats_by_id(id):
    found_playerstats = PlayerStatsDAO.findByID(id)
    if not found_playerstats:
        abort(400)
    return jsonify(found_playerstats)

@app.route('/playerstats', methods=['POST'])
def create_playerstats():
    if not request.json:
        abort(400)
    playerstat = {
        "Full_Name": request.json["Full_Name"],
        "Prize_Money": request.json["Prize_Money"],
        "Year": request.json["Year"],
    }
    values =(playerstat['Full_Name'],playerstat['Prize_Money'],playerstat['Year'])
    newId = PlayerDAO.create(values)
    playerstat['id'] = newId
    return jsonify(playerstat)

@app.route('/playerstats/<int:id>', methods=['PUT'])
def update_playerstat(id):
    foundPlayer = PlayerStatsDAO.findByID(id)
    if not foundPlayer:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Prize_Money' in reqJson and type(reqJson['Prize_Money']) is not int:
        abort(400)
    if 'Year' in reqJson and type(reqJson['Year']) is not int:
        abort(400)
    if 'Full_Name' in reqJson:
        foundPlayer['Full_Name'] = reqJson['Full_Name']
    if 'Prize_Money' in reqJson:
        foundPlayer['Prize_Money'] = reqJson['Prize_Money']
    if 'Year' in reqJson:
        foundPlayer['Year'] = reqJson['Year']
    values = (foundPlayer['Full_Name'],foundPlayer['Prize_Money'],foundPlayer['Year'],foundPlayer['id'])
    PlayerDAO.update(values)
    return jsonify(foundPlayer)

@app.route('/players/<int:id>' , methods=['DELETE'])
def delete_playerstat(id):
    PlayerStatsDAO.delete(id)
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)

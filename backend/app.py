from flask import Flask, request, jsonify, make_response, redirect, url_for
from flask_cors import CORS
from posture_analysis.pose1_Foream_Plank import Foream_Plank_calculate
from posture_analysis.pose2_V_Brace import V_Brace_calculate
from posture_analysis.pose3_Sumo_Glute_Bridge import Sumo_Glute_Bridge_calculate
from posture_analysis.pose4_Lying_Leg_Raise import Lying_Leg_Raise_calculate
from posture_analysis.pose5_Left_Right_Bridge import Left_Right_Bridge_calculate



app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS 跨源HTTP请求控制
CORS(app)

message = ""
joints = [
    [100.0, 200.0],  # Head
    [105.0, 180.0],  # Neck
    [110.0, 170.0],  # RShoulder
    [120.0, 150.0],  # RElbow
    [130.0, 130.0],  # RWrist
    [90.0, 170.0],   # LShoulder
    [80.0, 150.0],   # LElbow
    [70.0, 130.0],   # LWrist
    [125.0, 220.0],  # RHip
    [135.0, 190.0],  # RKnee
    [145.0, 160.0],  # RAnkle
    [75.0, 220.0],   # LHip
    [65.0, 190.0],   # LKnee
    [55.0, 160.0],   # LAnkle
    [115.0, 200.0],  # Chest
]

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/vueflask', methods=['POST', 'GET'])
def vueflask():
    response = jsonify({"message": "Success!"})
    response.headers.set('Access-Control-Allow-Origin', '*')
    if request.method == 'POST': # 如果是POST请求
        data = request.json
    
        action_id = data.get('actionId')
        if action_id == 1:
            text = Foream_Plank_calculate(joints)
        elif action_id == 2:
            text = V_Brace_calculate(joints)
        elif action_id == 3:
            text = Sumo_Glute_Bridge_calculate(joints)
        elif action_id == 4:
            text = Lying_Leg_Raise_calculate(joints)
        elif action_id == 5:
            text = Left_Right_Bridge_calculate(joints)
        else:
            error = 'Invalid action ID'
        return jsonify({'text': text})
    else:
        return response
    

    





if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from posture_analysis.posture_detection_pose1 import Foream_Plank_calculate
from posture_analysis.posture_detection_pose2 import Push_up_calculate
from posture_analysis.posture_detection_pose3 import Sumo_Glute_Bridge_calculate
from posture_analysis.posture_detection_pose4 import Lying_Leg_Raise_calculate
# import pygame
# pygame.mixer.music.load(audio)



app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS 跨源HTTP请求控制
CORS(app, resources={r'/*':{'origins':'*'}})


message = ""
audio = ""
joints = []

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/vueflask', methods=['POST'])
def vueflask():
    if request.method == 'POST':
        data = request.get_data()
        action_id = data.get('actionId')
        if action_id == 1:
            text, audio = Foream_Plank_calculate(joints)
        elif action_id == 2:
            text, audio = Push_up_calculate(joints)
        elif action_id == 3:
            text, audio = Sumo_Glute_Bridge_calculate(joints)
        elif action_id == 4:
            text, audio = Lying_Leg_Raise_calculate(joints)
        else:
            error = 'Invalid action ID'
    return jsonify(int(action_id))
        
    # return jsonify({'text': text, 'audio': audio})





if __name__ == '__main__':
    app.run(debug=True)
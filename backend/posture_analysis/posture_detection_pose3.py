from posture_analysis.calculation import angle_calculation

message = ""
audio_path = ""



def Sumo_Glute_Bridge_calculate(joints):
    Head = joints[0]
    RShoulder = joints[2]
    LShoulder = joints[5]
    RHip = joints[8]
    LHip = joints[11]
    RAnkle = joints[10]
    LAnkle = joints[13]
    
    angle_HSH_R = angle_calculation()
    angle_HSH_L = angle_calculation()
    angle_SHA_R = angle_calculation()
    angle_SHA_L = angle_calculation()
    
    if angle_HSH_R < 170 or angle_HSH_L < 170:
        text_message = "您的臀部下垂，请抬起臀部"
        audio_path = "backend.data.audio.foream_plank/1.mp3"
    elif angle_HSH_R > 190 or angle_HSH_L > 190:
        text_message = "您的背部拱起，请挺直背部"
        audio_path = "backend.data.audio.foream_plank/2.mp3"
    elif angle_SHA_R < 170 or angle_SHA_L < 170 :
        text_message = "请您将肩髋踝保持在同一直线上"
        audio_path = "backend.data.audio.foream_plank/3.mp3"
    return text_message, audio_path
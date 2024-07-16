from posture_analysis.calculation import angle_calculation

message = ""


# 头部 (H)
# 肩膀 (S)
# 臀部 (H)
# 膝盖 (K)
# 脚踝 (A)
# 角度计算：
# 头肩髋 (HSH) 角度：应接近 180°。
# 肩髋踝 (SHA) 角度：应接近 180°。

# 偏差规则：
# 如果 HSH 角度 < 170°，则用户臀部下垂。
# 如果 HSH 角度 > 190°，则用户背部拱起。
# 如果 SHA 角度 < 170°，则用户身体不在一条直线上。


def Foream_Plank_calculate(joints):
    Head = joints[0]
    RShoulder = joints[2]
    LShoulder = joints[5]
    RHip = joints[8]
    LHip = joints[11]
    RAnkle = joints[10]
    LAnkle = joints[13]
    
    angle_HSH_R = angle_calculation(Head, RShoulder, RHip)
    angle_HSH_L = angle_calculation(Head, LShoulder, LHip)
    angle_SHA_R = angle_calculation(RShoulder, RHip, RAnkle)
    angle_SHA_L = angle_calculation(LShoulder, LHip, LAnkle)
    
    if angle_HSH_R < 170 or angle_HSH_L < 170:
        text_message = "您的臀部下垂，请抬起臀部"
    elif angle_HSH_R > 190 or angle_HSH_L > 190:
        text_message = "您的背部拱起，请挺直背部"
    elif angle_SHA_R < 170 or angle_SHA_L < 170 :
        text_message = "请您将肩髋踝保持在同一直线上"
    return text_message
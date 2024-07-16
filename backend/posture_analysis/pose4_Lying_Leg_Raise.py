from posture_analysis.calculation import angle_calculation

message = ""

# 头部 (H)
# 臀部 (H)
# 膝盖 (K)
# 脚踝 (A)
# 角度计算：
# 髋膝踝 (HKA) 角度：应接近 180°。
# 肩髋膝 (SHK) 角度：应介于90°至170°（不落地）。

# 偏差规则：
# 如果 HKA 角度 < 170°，则用户腿未伸直。
# 如果 SHK 角度 < 90°，则用户抬腿过度。
# 如果 SHK 角度 > 170°，则用户腿落地。

def Lying_Leg_Raise_calculate(joints):
    Head = joints[0]
    RShoulder = joints[2]
    LShoulder = joints[5]
    RHip = joints[8]
    LHip = joints[11]
    RKnee = joints[9]
    LKnee = joints[12]
    RAnkle = joints[10]
    LAnkle = joints[13]
    
    angle_SHK_R = angle_calculation(RHip, RKnee, RAnkle)
    angle_SHK_L = angle_calculation(LHip, LKnee, LAnkle)
    angle_SHK_R = angle_calculation(RShoulder, RHip, RKnee)
    angle_SHK_L = angle_calculation(LShoulder, LHip, LKnee)
    
    if angle_SHK_R < 170 or angle_SHK_L < 170:
        text_message = "请保持双腿伸直"
    elif angle_SHK_R < 90 or angle_SHK_L < 90:
        text_message = "请不要折叠双腿超过90°"
    elif angle_SHK_R > 170 or angle_SHK_L > 170:
        text_message = "请始终保持双腿悬空"
    else: 
        text_message = ""
    return text_message
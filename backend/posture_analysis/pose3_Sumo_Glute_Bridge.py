from posture_analysis.calculation import angle_calculation

message = ""

# 头部 (H)
# 肩膀 (S)
# 臀部 (H)
# 膝盖 (K)
# 脚踝 (A)
# 角度计算：
# 肩髋膝 (SHK) 角度：应接近 180°。
# 头踝膝 (HAK) 角度：应接近 90°。

# 偏差规则：
# 如果 SHK 角度 < 170°，则用户臀部顶起过多。
# 如果 SHK 角度 > 190°，则用户展髋不足。
# 如果 HAK 角度 < 80°，则用户脚太靠前。
# 如果 HAK 角度 > 100°，则用户脚太靠后。

def Sumo_Glute_Bridge_calculate(joints):
    Head = joints[0]
    RShoulder = joints[2]
    LShoulder = joints[5]
    RHip = joints[8]
    LHip = joints[11]
    RKnee = joints[9]
    LKnee = joints[12]
    RAnkle = joints[10]
    LAnkle = joints[13]
    
    angle_SHK_R = angle_calculation(RShoulder, RHip, RKnee)
    angle_SHK_L = angle_calculation(LShoulder, LHip, LKnee)
    angle_HAK_R = angle_calculation(Head, RAnkle, RKnee)
    angle_HAK_L = angle_calculation(Head, LAnkle, LKnee)
    
    if angle_SHK_R < 170 or angle_SHK_L < 170:
        text_message = "请充分展髋，收紧臀部向上顶起"
    elif angle_SHK_R > 190 or angle_SHK_L > 190:
        text_message = "请降低臀部高度"
    elif angle_HAK_R < 80 or angle_HAK_L < 80:
        text_message = "请将双脚稍向前移"
    elif angle_HAK_R > 100 or angle_HAK_L > 100:
        text_message = "请将双脚稍向后移"
    else: 
        text_message = ""
    return text_message

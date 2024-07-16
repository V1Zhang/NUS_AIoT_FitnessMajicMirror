from posture_analysis.calculation import angle_calculation, horizontal

message = ""

# 头部 (H)
# 肩膀 (S)
# 臀部 (H)
# 膝盖 (K)
# 脚踝 (A)
# 角度计算：
# 肩手 (SH) 与水平夹角：应接近0°。
# 肩髋踝 (SHA) 角度：应接近 90°。

# 偏差规则：
# 如果 SH 与水平夹角 > 10°，则用户双手未举平。
# 如果 SHA 角度 < 170°，则用户身体不在一条直线上。
# 如果 KAH 与水平夹角 > 10°，则用户小腿未与地面平行。

def V_Brace_calculate(joints):
    RShoulder = joints[2]
    LShoulder = joints[5]
    RHand = joints[4]
    LHand = joints[7]
    RHip = joints[8]
    LHip = joints[11]
    RKnee = joints[9]
    LKnee = joints[12]
    RAnkle = joints[10]
    LAnkle = joints[13]
    
    
    angle_SH_R = horizontal(RShoulder, RHand)
    angle_SH_L = horizontal(LShoulder, LHand)
    angle_SHA_R = angle_calculation(RShoulder, RHip, RAnkle)
    angle_SHA_L = angle_calculation(LShoulder, LHip, LAnkle)
    angle_KA_R = horizontal(RKnee, RAnkle)
    angle_KA_L = horizontal(LKnee, LAnkle)
    
    if angle_SH_R > 10 or angle_SH_L > 10:
        text_message = "请将双手举平"
    elif angle_SHA_R > 150 or angle_SHA_L > 150 :
        text_message = "请保持腹部绷紧"
    elif angle_KA_R > 10 or angle_KA_L > 10:
        text_message = "请保持小腿与地面平行"      
    else: 
        text_message = ""
    return text_message
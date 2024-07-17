from utils.calculation import angle_calculation, horizontal

text_message = "None"

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


def Foream_Plank_Calculate(joints):
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
    
    try:
        if angle_HSH_R < 170 or angle_HSH_L < 170:
            text_message = "您的臀部下垂，请抬起臀部"
        elif angle_HSH_R > 190 or angle_HSH_L > 190:
            text_message = "您的背部拱起，请挺直背部"
        elif angle_SHA_R < 170 or angle_SHA_L < 170:
            text_message = "请您将肩髋踝保持在同一直线上"
        else:
            text_message = "很棒，请继续保持"
    except Exception as e:
        text_message = "请露出关键点位"
    return text_message


# 肩膀 (S)
# 臀部 (H)
# 膝盖 (K)
# 角度计算：
# 肩肘 (SE) 与水平夹角：应接近90°。
# 肩髋膝 (SHK) 角度：应接近 180°。

# 偏差规则：
# 如果 SE 与水平夹角 < 80° 或 > 100°，则用户手臂与地面不垂直。
# 如果 SHK 角度 < 170°，则用户身体不在一条直线上。


def Left_Right_Bridge_Calculate(joints):
    RShoulder = joints[2]
    LShoulder = joints[5]
    RElbow = joints[4]
    LElbow = joints[7]
    RHip = joints[8]
    LHip = joints[11]
    RKnee = joints[9]
    LKnee = joints[12]

    knee_height = min(LKnee[1], RKnee[1])
    angle_SE_R = horizontal(RShoulder, RElbow)
    angle_SE_L = horizontal(LShoulder, LElbow)
    angle_SHK_R = angle_calculation(RShoulder, RHip, RKnee)
    angle_SHK_L = angle_calculation(LShoulder, LHip, LKnee)

    try:
        if knee_height < 10:
            text_message = "请保持膝盖离开地面"
        if RShoulder[1] < LShoulder[1]:
            # 右侧桥
            if angle_SE_R > 100 or angle_SE_R < 80:
                text_message = "请保持右臂与地面垂直"
            elif angle_SHK_R > 190 or angle_SHK_R < 170:
                text_message = "请保持身体躯干呈直线"
            else:
                text_message = ""
        else:
            # 左侧桥
            if angle_SE_L > 100 or angle_SE_L < 80:
                text_message = "请保持左臂与地面垂直"
            elif angle_SHK_L > 190 or angle_SHK_L < 170:
                text_message = "请保持身体躯干呈直线"
            else:
                text_message = "很棒，请继续保持"
    except Exception as e:
        text_message = "请露出关键点位"
    return text_message


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


def V_Brace_Calculate(joints):
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

    try:
        if angle_SH_R > 10 or angle_SH_L > 10:
            text_message = "请将双手举平"
        elif angle_SHA_R > 150 or angle_SHA_L > 150:
            text_message = "请保持腹部绷紧"
        elif angle_KA_R > 10 or angle_KA_L > 10:
            text_message = "请保持小腿与地面平行"
        else:
            text_message = "很棒，请继续保持"
    except Exception as e:
        text_message = "请露出关键点位"
    return text_message


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


def Lying_Leg_Raise_Calculate(joints):
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
    
    try:
        if angle_SHK_R < 170 or angle_SHK_L < 170:
            text_message = "请保持双腿伸直"
        elif angle_SHK_R < 90 or angle_SHK_L < 90:
            text_message = "请不要折叠双腿超过90°"
        elif angle_SHK_R > 170 or angle_SHK_L > 170:
            text_message = "请始终保持双腿悬空"
        else:
            text_message = "很棒，请继续保持"
    except Exception as e:
        text_message = "请露出关键点位"
    return text_message


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


def Sumo_Glute_Bridge_Calculate(joints):
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

    try:
        if angle_SHK_R < 170 or angle_SHK_L < 170:
            text_message = "请充分展髋，收紧臀部向上顶起"
        elif angle_SHK_R > 190 or angle_SHK_L > 190:
            text_message = "请降低臀部高度"
        elif angle_HAK_R < 80 or angle_HAK_L < 80:
            text_message = "请将双脚稍向前移"
        elif angle_HAK_R > 100 or angle_HAK_L > 100:
            text_message = "请将双脚稍向后移"
        else:
            text_message = "很棒，请继续保持"
    except Exception as e:
        text_message = "请露出关键点位"
    return text_message

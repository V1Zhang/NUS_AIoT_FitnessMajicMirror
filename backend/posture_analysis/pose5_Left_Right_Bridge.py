from posture_analysis.calculation import angle_calculation, horizontal

message = ""

# 肩膀 (S)
# 臀部 (H)
# 膝盖 (K)
# 角度计算：
# 肩肘 (SE) 与水平夹角：应接近90°。
# 肩髋膝 (SHK) 角度：应接近 180°。

# 偏差规则：
# 如果 SE 与水平夹角 < 80° 或 > 100°，则用户手臂与地面不垂直。
# 如果 SHK 角度 < 170°，则用户身体不在一条直线上。

def Left_Right_Bridge_calculate(joints):
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
    
    if knee_height < 10:
        text_message = "请保持膝盖离开地面"
    if RShoulder[1] < LShoulder[1]:
        # 右侧桥
        if angle_SE_R > 100 or angle_SE_R < 80 :
            text_message = "请保持右臂与地面垂直"
        elif angle_SHK_R > 190 or angle_SHK_R < 170:
            text_message = "请保持身体躯干呈直线"     
        else:
            text_message = ""
    else: 
         # 左侧桥
        if angle_SE_L > 100 or angle_SE_L < 80 :
            text_message = "请保持左臂与地面垂直"
        elif angle_SHK_L > 190 or angle_SHK_L < 170:
            text_message = "请保持身体躯干呈直线" 
        else:
            text_message = ""
            
    return text_message
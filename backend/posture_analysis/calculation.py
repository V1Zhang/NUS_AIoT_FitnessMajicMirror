import math

def angle_calculation(p1, p0, p2):
    x1, y1 = p1
    x0, y0 = p0
    x2, y2 = p2
   # 计算两个向量 v1 和 v2
    v1 = (x1 - x0, y1 - y0)
    v2 = (x2 - x0, y2 - y0)
    
    # 计算向量的点积和模长
    dot_product = v1[0]*v2[0] + v1[1]*v2[1]
    mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
    
    # 计算角度(弧度制)
    angle_radians = math.acos(dot_product / (mag_v1 * mag_v2))
    
    # 将弧度转换为角度
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees
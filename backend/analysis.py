from flask import Flask, request, jsonify

app = Flask(__name__)



def calculate_angle(joint_data, p1, p2, p3):
    # 根据三个关节点的坐标,计算角度
    # 这里需要实现具体的计算逻辑
    pass

def analyze_joint_angles(joint_data, activity):
    warnings = []

    # 根据运动类型,计算特定关节角度并检查是否超出范围
    if activity == 'squat':
        knee_angle = calculate_angle(joint_data, 2, 3, 4)
        hip_angle = calculate_angle(joint_data, 1, 2, 3)
        
        if knee_angle < 90 or knee_angle > 150:
            warnings.append('膝关节角度异常')
        if hip_angle < 45 or hip_angle > 120:
            warnings.append('髋关节角度异常')
    
    # 添加更多运动类型的分析逻辑
    
    return {
        'joint_data': joint_data,
        'warnings': warnings
    }

def generate_feedback(warnings):
    voice_feedback = ''
    text_feedback = ''

    for warning in warnings:
        voice_feedback += f"{warning},请调整您的动作姿势。"
        text_feedback += f"- {warning}\n"

    if not voice_feedback:
        voice_feedback = '动作良好,请继续保持。'
        text_feedback = '动作良好,请继续保持。'

    return {
        'voice_feedback': voice_feedback,
        'text_feedback': text_feedback
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    activity = data['activity']
    joint_data = data['jointData']

    result = analyze_joint_angles(joint_data, activity)
    feedback = generate_feedback(result['warnings'])

    return jsonify({**result, **feedback})

if __name__ == '__main__':
    app.run(debug=True)
import json

def parse_pose_data(file_path):
    joints = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('{'):
                parts = line[1:-1].split(';')
                type = parts[0]
                if type == 'type circle':
                    joint = parts[1]
                    joints.append(joint)
    return joints

# 提取 15 个点的中心坐标
joints = parse_pose_data('utils/pose.txt')

print(joints)

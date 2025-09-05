import redis
import json
from flask import Flask, request

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

# 이 API 엔드포인트로 사용자의 요구사항을 받습니다.
@app.route('/design', methods=['POST'])
def design_architecture():
    user_input = request.json.get('text', '')

    services = []
    if 'EC2' in user_input.upper(): services.append('EC2')
    if 'RDS' in user_input.upper(): services.append('RDS')
    if 'S3' in user_input.upper(): services.append('S3')
    if 'VPC' in user_input.upper(): services.append('VPC')

    # 추출된 서비스 목록을 JSON 형태로 만들어 다음 에이전트에게 보냅니다.
    payload = json.dumps({'services': services, 'original_text': user_input})
    r.publish('architecture_channel', payload)

    return f'Message sent to architecture agent with services: {", ".join(services)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
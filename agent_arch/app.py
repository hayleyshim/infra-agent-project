import redis
import threading
import json
from flask import Flask
import plantuml

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)
p = r.pubsub()

def generate_plantuml_code(services):
    """서비스 목록을 기반으로 PlantUML 코드를 생성합니다."""
    plantuml_code = "@startuml\n"

    if 'VPC' in services:
        plantuml_code += "cloud AWS {\n"
        plantuml_code += "  folder VPC {\n"

    if 'EC2' in services:
        plantuml_code += "    node \"Web Server\" as EC2\n"
    if 'RDS' in services:
        plantuml_code += "    database \"Database\" as RDS\n"
    if 'S3' in services:
        plantuml_code += "    storage \"File Storage\" as S3\n"

    if 'EC2' in services and 'RDS' in services:
        plantuml_code += "    EC2 -- RDS : connect\n"

    if 'VPC' in services:
        plantuml_code += "  }\n"
        plantuml_code += "}\n"

    plantuml_code += "@enduml\n"
    return plantuml_code

def listen_for_messages():
    p.subscribe('architecture_channel')
    print("Listening for messages on 'architecture_channel'...")

    for message in p.listen():
        if message['type'] == 'message':
            received_payload = json.loads(message['data'].decode('utf-8'))
            services = received_payload['services']
            original_text = received_payload['original_text']

            print(f"Received request for services: {services}")

            # PlantUML 코드 생성
            plantuml_code = generate_plantuml_code(services)
            print("Generated PlantUML code.")

            # 다음 에이전트에게 전달할 페이로드
            next_payload = json.dumps({'plantuml_code': plantuml_code, 'original_text': original_text})
            r.publish('docs_channel', next_payload)
            print(f"Forwarded code to 'docs_channel'.")

threading.Thread(target=listen_for_messages, daemon=True).start()

@app.route('/')
def status():
    return 'agent_arch is running and listening for messages!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
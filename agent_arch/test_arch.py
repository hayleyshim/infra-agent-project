import unittest
import sys
import os

# 현재 디렉토리를 Python 경로에 추가하여 app.py 모듈을 import할 수 있게 함
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from app import generate_plantuml_code

class TestAgentArch(unittest.TestCase):
    """agent_arch의 핵심 로직을 테스트하는 클래스"""

    def test_generate_plantuml_code_with_all_services(self):
        """모든 서비스가 포함된 경우 PlantUML 코드가 올바르게 생성되는지 테스트"""
        services = ["EC2", "RDS", "S3", "VPC"]
        plantuml_code = generate_plantuml_code(services)

        self.assertIn("@startuml", plantuml_code)
        self.assertIn("@enduml", plantuml_code)
        self.assertIn("node \"Web Server\" as EC2", plantuml_code)
        self.assertIn("database \"Database\" as RDS", plantuml_code)
        self.assertIn("storage \"File Storage\" as S3", plantuml_code)
        self.assertIn("EC2 -- RDS : connect", plantuml_code)
        self.assertIn("cloud AWS", plantuml_code)
        self.assertIn("folder VPC", plantuml_code)

    def test_generate_plantuml_code_with_no_services(self):
        """서비스가 없는 경우에도 기본 코드가 생성되는지 테스트"""
        services = []
        plantuml_code = generate_plantuml_code(services)

        self.assertIn("@startuml", plantuml_code)
        self.assertIn("@enduml", plantuml_code)
        self.assertNotIn("EC2", plantuml_code)
        self.assertNotIn("RDS", plantuml_code)

if __name__ == '__main__':
    unittest.main()
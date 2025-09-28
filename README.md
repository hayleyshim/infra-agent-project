🚀 Multi-Agent System (MAS) 포트폴리오: 자동화 및 비용 분석 에이전트
이 저장소는 **Multi-Agent System (MAS)**과 A2A (Agent-to-Agent) 통신 개념을 활용하여 클라우드 인프라 아키텍트의 핵심 업무를 자동화하는 두 가지 프로젝트를 담고 있습니다.

🛠️ 공통 기술 스택
분류	기술	역할
Agent Framework	Python 3.9+	주요 개발 언어 및 에이전트 로직 구현
A2A 통신	Redis (Message Queue)	에이전트 간 비동기 메시지 전달 및 협업 프로토콜
컨테이너	Docker, Docker Compose	각 에이전트와 Redis를 독립적인 서비스로 격리
자동화	GitHub Actions	코드 테스트 및 컨테이너 이미지 빌드 자동화 (CI/CD)


1. 🏗️ 인프라 설계 자동화 및 문서화 에이전트 (MAS - Design)
사용자의 요구사항을 파악하여 아키텍처 설계 및 Markdown 문서를 자동으로 생성하는 에이전트 시스템입니다.

📝 프로젝트 개요
목표	기능	결과물
A2A 협업	3개의 에이전트가 순차적으로 작업을 분담 (분석 → 설계 → 문서화)	design_document.md 파일
설계	요구사항 기반 PlantUML 다이어그램 코드 생성	PlantUML 코드가 삽입된 Markdown


📁 프로젝트 구조 및 포트
서비스 이름	역할	포트 (Local)
agent_reqs	사용자 입력 수신 및 요구사항 분석 시작점	5001
agent_arch	아키텍처 설계 (PlantUML 코드 생성)	N/A (내부 통신 전용)
agent_docs	최종 Markdown 문서 생성 및 로컬 저장	N/A (내부 통신 전용)


▶️ 테스트 방법
컨테이너 구동: docker compose up --build

요청 트리거: agent_reqs에 POST 요청을 보냅니다.

JSON

POST http://localhost:5001/design
Content-Type: application/json

{
    "text": "AWS에 EC2 인스턴스와 RDS 데이터베이스를 연결하는 웹 서비스 아키텍처를 설계해줘"
}
결과: ./output 폴더에 design_document.md 파일이 생성됩니다.

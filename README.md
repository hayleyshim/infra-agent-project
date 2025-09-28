🌩️ 클라우드 인프라 설계 자동화 및 CI/CD 경험 프로젝트 (Multi-Agent System)
이 프로젝트는 Google의 Gemini 모델을 활용하여 A2A (Agent-to-Agent) 및 MCP (Multi-Agent Collaboration Protocol) 개념을 적용한 Multi-Agent System (MAS) 구축 경험을 쌓기 위해 진행되었습니다. 사용자의 간단한 인프라 요구사항을 입력받아 아키텍처를 설계하고 문서를 자동 생성하는 에이전트를 로컬 환경에서 구현합니다.


🚀 프로젝트 목표
A2A/MCP 학습: 여러 에이전트가 Redis 메시지 큐를 통해 순차적으로 작업을 분담하고 협업하는 구조를 이해하고 구축합니다.
CI/CD 자동화: GitHub Actions를 활용하여 코드 테스트 및 컨테이너 빌드 과정을 자동화합니다.
실무 적용: 클라우드 인프라 아키텍트의 설계 및 문서화 업무를 자동화하여 효율을 높이는 프로토타입을 제작합니다.


🛠️ 기술 스택
분류	기술	역할
Agent Framework	Python 3.9+	주요 개발 언어
Web Framework	Flask	각 에이전트의 API 엔드포인트 및 서버 구성
A2A 통신	Redis (Message Queue)	에이전트 간의 메시지 전달 및 협업 프로토콜 구현
컨테이너	Docker, Docker Compose	각 에이전트를 독립적인 서비스로 격리 및 관리
문서화	PlantUML, Markdown	텍스트 기반 아키텍처 다이어그램 및 최종 문서 생성
자동화	GitHub Actions	테스트 및 컨테이너 이미지 빌드 자동화 (CI/CD)


🏗️ 프로젝트 구조
프로젝트는 세 개의 독립적인 에이전트로 구성되며, Docker Compose를 통해 통합 관리됩니다.

infra-agent-project/
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD (GitHub Actions) 워크플로우
├── agent_reqs/                # 1. 요구사항 분석 에이전트
│   └── app.py                 # (사용자 입력 수신 및 요구사항 분석)
├── agent_arch/                # 2. 아키텍처 설계 에이전트
│   └── app.py                 # (분석 결과 기반 PlantUML 생성)
├── agent_docs/                # 3. 문서화 에이전트
│   └── app.py                 # (PlantUML 및 설명을 취합하여 Markdown 문서 생성)
├── output/                    # 최종 결과물(.md)이 저장되는 로컬 폴더 (Volume)
├── docker-compose.yml         # 모든 서비스(3개 Agent + Redis) 정의 파일
└── README.md

⚙️ 시작하는 방법 (Local Run)
1. 환경 설정
필수 설치 항목: Python, Git, Docker Desktop (Docker Compose 기능 포함)

2. 저장소 클론 및 컨테이너 구동
터미널에서 프로젝트 폴더로 이동한 후, 모든 컨테이너를 빌드하고 실행합니다.

Bash

# 1. 프로젝트 폴더로 이동
# cd infra-agent-project

# 2. output 폴더 생성 (Volume Mapping을 위해 필수)
mkdir output

# 3. 모든 컨테이너 빌드 및 실행 (Docker Compose)
docker compose up --build
💡 참고: 컨테이너가 실행되면, Redis는 6379, 각 에이전트는 5001, 5002, 5003 포트에서 실행됩니다. (agent_reqs는 5001 포트)

3. 에이전트 워크플로우 테스트
REST Client (VS Code 확장 프로그램) 또는 curl 명령어를 사용하여 agent_reqs에 요청을 보냅니다. 이것이 전체 에이전트 협업의 시작점입니다.

요청 대상: agent_reqs (포트 5001)

요청 내용 (JSON):

JSON

POST http://localhost:5001/design
Content-Type: application/json

{
    "text": "AWS에 EC2 인스턴스와 RDS 데이터베이스를 연결하는 웹 서비스 아키텍처를 설계해줘"
}


4. 결과 확인
요청이 성공적으로 처리되면, agent_cost → agent_report → agent_docs 순서로 메시지가 전달됩니다.
최종 결과물인 design_document.md 파일이 로컬의 ./output 폴더에 자동으로 생성됩니다.


🌐 CI/CD (GitHub Actions)
이 프로젝트는 GitHub Actions를 사용하여 코드가 main 브랜치에 푸시되거나 Pull Request가 열릴 때마다 다음 과정을 자동화합니다.

Dependency Check: 필요한 Python 라이브러리가 올바른지 확인합니다.

Container Build: docker-compose.yml을 기반으로 모든 에이전트의 Docker 이미지를 빌드합니다.

Validation: 빌드된 컨테이너가 정상적으로 시작되는지 검증합니다.

이 자동화 파이프라인을 통해 코드가 프로덕션 환경에 배포되기 전, 안정성을 확보할 수 있습니다.

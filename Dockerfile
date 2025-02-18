# Python 3.9 기반의 경량 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY ./agent .

# Streamlit 실행 포트 설정
EXPOSE 8501

# 컨테이너 시작 시 실행할 명령
CMD ["streamlit", "run", "agent_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# 가상환경 생성 
python -m venv venv

# 가상환경 접속 
## 디렉토리 이동 필요
source venv/Scripts/activate

# 모듈설치 
pip install requirements.txt

# DB 설정 동기화 
python manage.py makemigrations
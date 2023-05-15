```
05/15 작업내용 

1. 지난번 말한 선수하나의 정보를 각각의 dict타입에 저장하여 전체 정보를 list에 담아두기 완료 
url = http://127.0.0.1:8000/baseballs/index2 에서 확인가능 
테이블 컬럼에 들어갈 부분은 주석처리 해놨음 하나씩 박아 넣으면 될듯 


2. DataFrame에 to_html모듈을 사용하여 테이블 형태 구성 
url = http://127.0.0.1:8000/baseballs/
간편하게 테이블 형태로 구현했으나 css 적용이 가능할지는 모르겠음 현재는 중앙정렬만 해둔 상태 

## 현재 데이터는 23년도 14주차만 가져오게 되어있음 만약 전체 데이터를 가지고 오고싶다면 
## views.py 34번 줄 주석 해제하고 사용하면 됨 위에 "sql = " 주석처리해야함 

3. 원래 DB에 있던 테이블들 baseballs/models.py에 전부 선언해두었음 
명령어 "python manage.py inspectdb > 'baseballs/models.py' --database 'default'" 사용 
이제 기존에 있던 테이블들이 model에 선언되어서 쿼리셋형태로 가는것같음 
확인 해보면될듯 ~ 

```






# 가상환경 생성 
python -m venv venv

# 가상환경 접속 
## 디렉토리 이동 필요
source venv/Scripts/activate

# 모듈설치 
pip install -r requirements.txt

# DB 설정 동기화 
python manage.py makemigrations
python manage.py migrate

# 서버 실행 
python manage.py runserver
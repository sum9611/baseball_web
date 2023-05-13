from django.shortcuts import render, redirect
from .models import test
import yaml
import pandas as pd
import pymysql


# db정보 가져오기
with open('./yamls/sql_info.yaml') as f:

    info = yaml.load(f, Loader=yaml.FullLoader)

host = info['MARIADB']['IP']
user = info['MARIADB']['USER']
passwd=info['MARIADB']['PASSWD']
db = info['MARIADB']['DB']
port = info['MARIADB']['PORT']

def index(request):
    # posts = test.objects.all()

    conn = pymysql.connect(host = host, user = user, passwd=passwd, db = db, charset='utf8', port = port, cursorclass=pymysql.cursors.DictCursor)
    # conn = pymysql.connect(host = host, user = user, passwd=passwd, db = db, charset='utf8', port = port)
    cur = conn.cursor()
    sql = '''select * from weekly_batting_info
        where 1=1
        and week = '202314'
        and TPA >= RTPA
        order by H desc
    '''
    cur.execute(sql)

    result = cur.fetchall()
    batting = pd.DataFrame(result)
    batting = batting.to_json()
    print(batting)

    context = {
        'posts': batting,
    }
    return render(request, 'baseballs/index.html', context)
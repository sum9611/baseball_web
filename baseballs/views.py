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


## to_html() 메소드 사용하여 구현
def index(request):
    conn = pymysql.connect(host = host, user = user, passwd=passwd, db = db, charset='utf8', port = port, cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = '''select * from weekly_batting_info
        where 1=1
        and week = '202314'
        and TPA >= RTPA
        order by H desc
    '''

    # sql = '''select * from weekly_batting_info
    #      where 1=1
    #      and TPA >= RTPA
    # '''

    
    cur.execute(sql)

    result = cur.fetchall()
    batting = pd.DataFrame(result)
    batting = batting.to_html(justify='center')

    context = {
        'posts': batting,
    }
    return render(request, 'baseballs/index.html', context)


## list안에 선수하나씩 dict 타입으로 저장
def index2(request):

    conn = pymysql.connect(host = host, user = user, passwd=passwd, db = db, charset='utf8', port = port, cursorclass=pymysql.cursors.DictCursor)
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
    col = batting.columns
    print(col)
    batting_list = []
    for i in batting.iterrows():
        batting_dic = {}
        for j in range(len(col)):
            if col[j] == 'player_birth':
                batting_dic[col[j]] = i[1][j].strftime('%Y-%m-%d')
            elif col[j] == 'AVG':
                batting_dic[col[j]] = float(i[1][j])
            else:    
                batting_dic[col[j]] = i[1][j]
        batting_list.append(batting_dic)

    context = {
        'batting': batting_list,
    }
    return render(request, 'baseballs/index2.html', context)
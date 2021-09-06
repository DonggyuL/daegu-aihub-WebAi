import sqlite3

cnt = sqlite3.connect('topics.db') #topic 테이블 연결
result = cnt.execute('SELECT * FROM topic') #select문 실행
rows = result.fetchall() #result를 파이썬에서 이용가능하도록 변경, 모든 데이터 가져옴

for row in rows:
    print(row)

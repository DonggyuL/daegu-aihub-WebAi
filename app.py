from flask import Flask
import sqlite3

app = Flask(__name__)
@app.route('/') #최상위 경로
def home():
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()
    contents = '<h1><a href="/">Web</a></h1>'
    contents += '<ol>' #이어 붙이기
    for id, title,body in topics: 
        contents += '<li><a href="/read/'+str(id)+'">'+title+'</a></li>'    
        contents += '</ol>'
        contents +='<h2>Welcome</h2>Hello, WEB'
    return contents





app.run(debug=True) #debug->파일수정할 때마다 flask 재부팅



#에러 핸들링
#Address already in use: flask실행중 또는 해당포트(5000) 이용중



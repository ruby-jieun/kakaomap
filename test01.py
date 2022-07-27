#pymssql 패키지 import
import pymssql

#DB(MSSQL)연결(접속)
#conn = pymssql.connect(server="", user="", password="", database="")
connect = pymssql.connect(server="localhost", database="sip")

#connection으로부터 cursor생성
cursor = connect.cursor()

#SQL문 실행(쿼리작성)
cursor.execute("SELECT * FROM ruby00")

#데이터 하나씩 Fetch하여 출력
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
    
#연결 끊기
connect.close()
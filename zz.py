import pymssql

# DB 서버 주소
server = 'localhost'
# 데이터 베이스 이름
database = 'sip'
# 접속 유저명
user = 'test01'
# 접속 유저 패스워드
password = 'test'
# 날 제일 골썩인 놈
charset = 'CP936'

# MSSQL 접속
conn = pymssql.connect(server, user, password, database, charset)
cursor = conn.cursor()

# SQL문 실행
cursor.execute('SELECT * FROM TEST;')

# 데이터를 하나씩 Fetch하여 출력
row = cursor.fetchone()

while row:
    print(row[0], row[1], row[2])
    print('database connected')
    row = cursor.fetchone()

# 연결 끊기
conn.close()
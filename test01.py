import pymssql
import requests
from pprint import pprint


def search_custcode(a):
    db = pymssql.connect(server='localhost', user='test01', password='test', database='sip', charset='CP936')
    # MSSQL 접속
    cursor = db.cursor()
    # SQL문 실행
    sql = "SELECT custcode, custname, ceoname, addr1, LATITUDE, LONGITUDE FROM ruby00 where custcode = '" + a + "'"
    # 데이터를 하나씩 Fetch하여 출력
    row = cursor.fetchone()
    cursor.execute(sql)
    db.commit()
    db.close()


def search_add():
    data = request.get_data()
    query = json.loads(data, encoding='utf-8')['query']
    # query = request.json.get('query')
    return jsonify(search_address(query))


def search_address(query):
    """
    사용자가 검색 창에 직접 주소를 입력했을 때, 카카오맵 api 를 통해 주소를 위도경도로 변환합니다.\n
    :param query: 찾고자 하는 주소
    :return: doc(dict) {
        address: 찾고자 하는 주소 도로명 주소,
        lat: 찾고자 하는 지역의 x좌표,
        long: 찾고자 하는 지역의 y 좌표
    }
    """
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + query
    _header = {
        'Host': 'dapi.kakao.com',
        'Authorization': 'KakaoAK 3c431343f5fc968c79ed82276f9a9bcd'}
    req = requests.get(url, headers=_header)
    result = req.json()
    pprint(result)
    documents = result['documents'][0]
    address = documents['address_name']
    lat = documents['y']
    lng = documents['x']
    doc = {
        "address": address,
        "lat": lat,
        "long": lng
    }
    return doc

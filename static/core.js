let user = null;
let latitude = null;
let longitude = null;
let isMobile = false;
let Screen = "Full Wide"
// 유저의 값을 글로벌하게 사용하기 위해 초기화한다.

headers = {
    accept: "*/*",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

// 위도와 경도를 받아서 지도에 표시해주는 함수
function drawMap(mapContainer, lat, lng) {
    mapOption = {
        center: new kakao.maps.LatLng(lat, lng), // 지도의 중심좌표
        level: 3, // 지도의 확대 레벨
        mapTypeId: kakao.maps.MapTypeId.ROADMAP // 지도종류
    };
    // 지도를 생성한다
    let map = new kakao.maps.Map(mapContainer, mapOption);
    // 지도에 마커를 생성하고 표시한다
    let markerPosition = new kakao.maps.LatLng(lat, lng);
    // 마커를 생성합니다
    let marker = new kakao.maps.Marker({
        position: markerPosition
    });
    // 마커가 지도 위에 표시되도록 설정합니다
    marker.setMap(map);
}

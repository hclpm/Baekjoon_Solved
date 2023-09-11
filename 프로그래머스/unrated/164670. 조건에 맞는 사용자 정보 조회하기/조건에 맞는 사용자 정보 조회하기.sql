-- 중고 거래 게시물을 3건 이상 등록한 사용자
-- 사용자 ID, 닉네임, 전체주소, 전화번호
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력
-- 전화번호의 경우 xxx-xxxx-xxxx
-- 회원 ID를 기준으로 내림차순

SELECT USERS.USER_ID, USERS.NICKNAME,
(CITY ||' '||STREET_ADDRESS1) ||' '||STREET_ADDRESS2 AS "전체주소",
SUBSTR(TLNO, 1, 3)||'-'||SUBSTR(TLNO, 4, 4) ||'-'||SUBSTR(TLNO, 8, 4) AS "전화번호"
FROM
    (SELECT WRITER_ID, COUNT(BOARD_ID) AS COUNT
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(BOARD_ID) >= 3) T1 
    JOIN USED_GOODS_USER USERS
ON USERS.USER_ID = T1.WRITER_ID
ORDER BY USER_ID DESC;
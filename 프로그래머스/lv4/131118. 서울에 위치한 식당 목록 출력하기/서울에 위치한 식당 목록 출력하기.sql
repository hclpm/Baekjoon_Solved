-- 식당 ID, 1식당 이름, 1음식 종류, 1즐겨찾기수, 1주소, 2리뷰 평균 점수를 조회
-- 서울에 위치한 식당
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
-- 평균점수를 기준으로 내림차순 -> 즐겨찾기수를 기준으로 내림차순
-- REST_INFO 1 // REST_REVIEW 2

SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, A.AVG
FROM(
    SELECT REST_ID, ROUND(AVG(REVIEW_SCORE), 2) AS AVG
    FROM REST_REVIEW
    GROUP BY REST_ID
    ORDER BY AVG) A JOIN REST_INFO B
    ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE '서울%' 
ORDER BY AVG DESC, FAVORITES DESC
-- 코드를 입력하세요
-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만
-- 식품 가격을 기준으로 내림차순

SELECT T1.CATEGORY, T1.MAX_PRICE, F.PRODUCT_NAME
FROM(
SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
FROM FOOD_PRODUCT
WHERE CATEGORY IN('식용유', '과자', '국', '김치')
GROUP BY CATEGORY
) T1 JOIN FOOD_PRODUCT F
ON T1.CATEGORY = F.CATEGORY
AND T1.MAX_PRICE = F.PRICE
ORDER BY MAX_PRICE DESC
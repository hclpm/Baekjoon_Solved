-- 코드를 입력하세요
SELECT * FROM
(
    SELECT DISTINCT I.NAME, I.DATETIME
    FROM ANIMAL_INS I, ANIMAL_OUTS O
    WHERE I.ANIMAL_ID != ALL(SELECT ANIMAL_ID FROM ANIMAL_OUTS)
    ORDER BY DATETIME
)
WHERE ROWNUM <= 3    
;
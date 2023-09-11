-- 코드를 입력하세요
-- 보호소에서 중성화한 동물 정보
-- 이전 - 이후 중성화 여부 다른 동물 그룹화
-- 아이디, 동물 타입, 이름 --> 아이디 순으로
SELECT ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I JOIN ANIMAL_OUTS O USING (ANIMAL_ID)
WHERE I.SEX_UPON_INTAKE != ALL(O.SEX_UPON_OUTCOME);
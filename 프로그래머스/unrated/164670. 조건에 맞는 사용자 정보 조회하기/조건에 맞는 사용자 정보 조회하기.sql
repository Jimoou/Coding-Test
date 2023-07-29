SELECT USER_ID, NICKNAME,
(CITY || ' ' || STREET_ADDRESS1 || ' ' || STREET_ADDRESS2) AS 전체주소,
REGEXP_REPLACE(TLNO, '(.{3})(.+)(.{4})', '\1-\2-\3') AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID
IN
(SELECT WRITER_ID
FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING COUNT(*) >= 3)
ORDER BY USER_ID DESC
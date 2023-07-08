-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, to_char(R.CREATED_DATE, 'yyyy-mm-dd') created_date 
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE TO_CHAR(B.CREATED_DATE, 'YYYY-MM') = '2022-10'
ORDER BY R.CREATED_DATE, B.TITLE;
SELECT DISTINCT R.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR R
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON R.CAR_ID = H.CAR_ID
WHERE R.CAR_TYPE = '세단'
AND TO_CHAR(H.START_DATE, 'MM') = '10'
ORDER BY R.CAR_ID DESC;
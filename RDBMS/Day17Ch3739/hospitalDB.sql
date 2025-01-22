-- 환자의 생일년도를 중복 없이 표시하세요.
-- SELECT DISTINCT YEAR(birth_date) AS birth_year FROM patients ORDER BY birth_year ASC;

-- 하나의 이름만 존재하는 환자의 이름을 표시하세요.
-- SELECT first_name FROM patients group by first_name having COUNT(first_name) = 1;

-- s로 시작하고 끝나고 6자리 이상인 이름을 표시하세요
/*
SELECT patient_id,first_name FROM patients
WHERE first_name LIKE 's____%s';
*/
-- s로 시작하고 끝나고 6자리 이상인 이름을 표시하세요
/*
SELECT patient_id,first_name FROM patients
WHERE first_name LIKE 's%s' AND len(first_name) >= 6;
*/

-- 환자의 진단명이 치매(Dementia)인 사람의 번호,이름,성을 보여주세요.
/*
SELECT p.patient_id, p.first_name, p.last_name
FROM patients p
JOIN admissions a ON p.patient_id = a.patient_id
where a.diagnosis = 'Dementia';
*/

-- 환자의 이름을 길이가 짧은 순서대로 정리하고 거기서 다시 한번 이름순으로 정리하세요. 
-- SELECT first_name FROM patients order by LEN(first_name), first_name;

-- 모든 남자, 여자 환자의 숫자를 파악하세요.
/*
SELECT 
  (SELECT count(*) FROM patients WHERE gender='M') AS male_count, 
  (SELECT count(*) FROM patients WHERE gender='F') AS female_count;

SELECT
SUM(Gender = 'M') as male_count,
SUM(Gender = 'F') AS female_count
FROM patients;
*/

-- 패니실린과 모르핀에 알래르기가 있는 환자 목록
/*
SELECT first_name, last_name, allergies FROM patients
WHERE allergies = 'Penicillin' OR allergies ='Morphine'
order by allergies, first_name, last_name;

SELECT first_name, last_name, allergies FROM patients
WHERE allergies IN ('Penicillin', 'Morphine')
order by allergies, first_name, last_name;
*/

-- 같은 병명으로 진단 받은적인 환자의 숫자를 세시오.
-- SELECT patient_id, diagnosis FROM admissions GROUP BY patient_id, diagnosis HAVING count(*) > 1;

-- 가장 환자가 많은 도시 순으로 표시하세요.
-- SELECT city, COUNT(*) AS num_patients FROM patients group by city order by num_patients DEsC, city;

-- 모든 환자, 의사 목록을 표시하세요.
/*
SELECT first_name, last_name, 'Patient' AS role FROM patients
UNION ALL
SELECT first_name, last_name, 'Doctor' AS role FROM doctors;
*/
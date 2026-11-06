-- Problem: Patients With a Condition (LC #1527)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/patients-with-a-condition/
--
-- Approach:
-- conditions is a space-separated list of codes.
-- Match DIAB1 only as the start of a code:
--   at the start of the string  -> LIKE 'DIAB1%'
--   after a space               -> LIKE '% DIAB1%'
-- Avoids false matches such as 'ADIAB1'.
-- Time: O(n) | Space: O(1)
--
-- ML Connection:
-- Pattern-based filtering on text fields is a common step
-- when building cohorts and labels from raw medical records.

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';

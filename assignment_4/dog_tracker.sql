-- Dog Care Tracker Database
-- This database stores daily care activities for my dog, including walks,
-- feeding, grooming, and vet visits. It is designed to support a Python Flask API
-- where users can view activities, add new records, and manage dog care information.

DROP DATABASE IF EXISTS dog_tracker;
CREATE DATABASE dog_tracker;
USE dog_tracker;

-- ==================================================
-- TABLE CREATION
-- ==================================================

CREATE TABLE activities (
activity_id INT AUTO_INCREMENT PRIMARY KEY,
activity_type VARCHAR(50) NOT NULL,
activity_date DATE NOT NULL,
activity_description VARCHAR(255) NOT NULL
);

SHOW TABLES;
DESCRIBE activities;

-- ==================================================
-- INSERT DATA: activities (4 rows total)
-- ==================================================
INSERT INTO activities (activity_type, activity_date, activity_description)
VALUES
('Grooming', '2026-05-10', 'Care activities such as brushing fur, bathing, or nail trimming.'),
('Walk', '2026-05-11', 'Daily exercise such as a park walk or neighbourhood walk.'),
('Feeding', '2026-05-12', 'Meal given to the dog, such as breakfast or dinner.'),
('Vet Visit', '2026-05-17', 'Health check-up, vaccination, or medical appointment.');

SELECT * FROM activities;
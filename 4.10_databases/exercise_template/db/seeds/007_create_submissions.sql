INSERT INTO submissions (assignment_id, student_id, submitted_at, mark)
VALUES
(
    (SELECT id FROM assignments WHERE title = 'ERD Task'),
    (SELECT id FROM users WHERE email = 'emma.wilson5@example.com'),
    CURRENT_TIMESTAMP,
    18
),
(
    (SELECT id FROM assignments WHERE title = 'ERD Task'),
    (SELECT id FROM users WHERE email = 'frank.davies6@example.com'),
    CURRENT_TIMESTAMP,
    15
),
(
    (SELECT id FROM assignments WHERE title = 'SQL Queries Task'),
    (SELECT id FROM users WHERE email = 'grace.evans7@example.com'),
    CURRENT_TIMESTAMP,
    26
),
(
    (SELECT id FROM assignments WHERE title = 'Python Functions Task'),
    (SELECT id FROM users WHERE email = 'hannah.thomas8@example.com'),
    CURRENT_TIMESTAMP,
    22
),
(
    (SELECT id FROM assignments WHERE title = 'Refactoring Task'),
    (SELECT id FROM users WHERE email = 'jack.johnson10@example.com'),
    CURRENT_TIMESTAMP,
    21
)
ON CONFLICT (assignment_id, student_id) DO NOTHING;
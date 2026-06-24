INSERT INTO assignments (course_id, title, due_date, max_mark)
VALUES
(
    (SELECT id FROM courses WHERE course_code = 'CS101'),
    'ERD Task',
    CURRENT_DATE + INTERVAL '7 days',
    20
),
(
    (SELECT id FROM courses WHERE course_code = 'CS101'),
    'SQL Queries Task',
    CURRENT_DATE + INTERVAL '14 days',
    30
),
(
    (SELECT id FROM courses WHERE course_code = 'CS102'),
    'Python Functions Task',
    CURRENT_DATE + INTERVAL '10 days',
    25
),
(
    (SELECT id FROM courses WHERE course_code = 'CS103'),
    'Refactoring Task',
    CURRENT_DATE + INTERVAL '12 days',
    25
);

INSERT INTO enrolments (user_id, course_id, enrolled_on)
VALUES
(
    (SELECT id FROM users WHERE email = 'emma.wilson5@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS101'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'frank.davies6@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS101'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'grace.evans7@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS101'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'hannah.thomas8@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS102'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'isaac.roberts9@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS102'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'jack.johnson10@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS103'),
    CURRENT_DATE
),
(
    (SELECT id FROM users WHERE email = 'katie.lewis11@example.com'),
    (SELECT id FROM courses WHERE course_code = 'CS103'),
    CURRENT_DATE
)
ON CONFLICT (user_id, course_id) DO NOTHING;
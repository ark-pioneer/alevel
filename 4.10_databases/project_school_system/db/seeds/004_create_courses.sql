INSERT INTO courses (course_code, course_name, teacher_id)
VALUES
(
    'CS101',
    'Introduction to Databases',
    (SELECT id FROM users WHERE email = 'alice.smith1@example.com')
),
(
    'CS102',
    'Python for Data Systems',
    (SELECT id FROM users WHERE email = 'bob.jones2@example.com')
),
(
    'CS103',
    'Software Development Principles',
    (SELECT id FROM users WHERE email = 'charlie.brown3@example.com')
)
ON CONFLICT (course_code) DO NOTHING;
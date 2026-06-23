UPDATE users
SET role_id = (SELECT id FROM roles WHERE role_name = 'teacher')
WHERE email IN (
    'alice.smith1@example.com',
    'bob.jones2@example.com',
    'charlie.brown3@example.com'
);

UPDATE users
SET role_id = (SELECT id FROM roles WHERE role_name = 'admin')
WHERE email IN (
    'david.taylor4@example.com'
);

UPDATE users
SET role_id = (SELECT id FROM roles WHERE role_name = 'student')
WHERE role_id IS NULL;
INSERT INTO roles (role_name)
VALUES
    ('teacher'),
    ('student'),
    ('admin')
ON CONFLICT (role_name) DO NOTHING;

-- Migration: alter users add role id
-- Created at: 2606231426

-- Write SQL below

ALTER TABLE users
ADD COLUMN IF NOT EXISTS role_id INTEGER;

ALTER TABLE users
ADD CONSTRAINT fk_users_role
FOREIGN KEY (role_id)
REFERENCES roles(id);

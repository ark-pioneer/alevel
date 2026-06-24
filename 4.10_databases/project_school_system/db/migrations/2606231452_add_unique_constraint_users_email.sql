-- Migration: add unique constraint users email
-- Created at: 2606231452

-- Write SQL below

ALTER TABLE users
ADD CONSTRAINT uq_users_email UNIQUE (email);

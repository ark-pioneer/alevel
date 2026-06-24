-- Migration: create roles
-- Created at: 2606231425

-- Write SQL below

CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(30) NOT NULL UNIQUE
);



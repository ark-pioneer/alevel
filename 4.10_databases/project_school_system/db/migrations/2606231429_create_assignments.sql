-- Migration: create assignments
-- Created at: 2606231428

-- Write SQL below

CREATE TABLE IF NOT EXISTS assignments (
    id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    due_date DATE NOT NULL,
    max_mark INTEGER NOT NULL CHECK (max_mark > 0),
    CONSTRAINT fk_assignments_course
        FOREIGN KEY (course_id)
        REFERENCES courses(id)
        ON DELETE CASCADE
);



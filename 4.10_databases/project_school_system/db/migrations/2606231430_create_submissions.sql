-- Migration: create submissions
-- Created at: 2606231428

-- Write SQL below

CREATE TABLE IF NOT EXISTS submissions (
    id SERIAL PRIMARY KEY,
    assignment_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    submitted_at TIMESTAMP,
    mark INTEGER CHECK (mark >= 0),
    CONSTRAINT fk_submissions_assignment
        FOREIGN KEY (assignment_id)
        REFERENCES assignments(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_submissions_student
        FOREIGN KEY (student_id)
        REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT uq_submissions_assignment_student
        UNIQUE (assignment_id, student_id)
);


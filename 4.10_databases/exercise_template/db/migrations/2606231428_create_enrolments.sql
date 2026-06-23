-- Migration: create enrolments
-- Created at: 2606231427

-- Write SQL below

CREATE TABLE IF NOT EXISTS enrolments (
    user_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_on DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (user_id, course_id),
    CONSTRAINT fk_enrolments_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_enrolments_course
        FOREIGN KEY (course_id)
        REFERENCES courses(id)
        ON DELETE CASCADE
);



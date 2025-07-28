CREATE DATABASE fittracking;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(10),
    birth_date DATE,
    height_cm INTEGER,
    weight_kg NUMERIC(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    exercise_type VARCHAR(100) NOT NULL,
    duration_minutes INTEGER,
    calories_burned NUMERIC(6,2),
    notes TEXT
);


CREATE TABLE meals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    meal_type VARCHAR(20),  -- breakfast, lunch, dinner, snack
    food_name VARCHAR(100),
    calories NUMERIC(6,2),
    protein_g NUMERIC(5,2),
    carbs_g NUMERIC(5,2),
    fats_g NUMERIC(5,2)
);


CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    goal_weight NUMERIC(5,2),
    goal_date DATE,
    notes TEXT
);


CREATE TABLE progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    weight_kg NUMERIC(5,2)
);

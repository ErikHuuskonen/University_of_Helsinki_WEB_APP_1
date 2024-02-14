CREATE TABLE userinfo (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(200),
    purpose VARCHAR(50)
);

CREATE TABLE content (
    id SERIAL PRIMARY KEY, 
    user_id VARCHAR(255) NOT NULL, 
    text TEXT NOT NULL, 
    date_posted TIMESTAMP NOT NULL, 
    video_name VARCHAR(255) 
);

CREATE TABLE data (
    id SERIAL PRIMARY KEY, 
    data_posted TIMESTAMP NOT NULL, 
    purpose VARCHAR(100), 
    lenght VARCHAR(100) 
);
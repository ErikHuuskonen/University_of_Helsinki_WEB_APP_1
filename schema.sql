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

CREATE TABLE user_data (
    user_id INT NOT NULL,
    data_id INT NOT NULL,
    PRIMARY KEY (user_id, data_id),
    FOREIGN KEY (user_id) REFERENCES userinfo(id),
    FOREIGN KEY (data_id) REFERENCES data(id)
);

CREATE TABLE content_data (
    content_id INT NOT NULL,
    data_id INT NOT NULL,
    PRIMARY KEY (content_id, data_id),
    FOREIGN KEY (content_id) REFERENCES content(id),
    FOREIGN KEY (data_id) REFERENCES data(id)
);
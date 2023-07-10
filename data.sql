CREATE DATABASE bdCJR;

CREATE TABLE user {
	id VARCHAR(50),
    username VARCHAR(50),
    senha VARCHAR(250),
    gender CHAR(5),
    email VARCHAR(250),
    cargo VARCHAR(250),
    created_at TIMESTAMP
};

CREATE TABLE post {
	post_id INT,
    user_id STR,
    content VARCHAR(250),
    updated_at TIMESTAMP,
    created_at TIMESTAMP
};

CREATE TABLE comments {
	comment_id INT,
    post_id INT,
    user_id VARCHAR(50),
    content_coments VARCHAR(100)
};
-- Creating User Table
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);

-- Creating ChildProfile Table
CREATE TABLE IF NOT EXISTS child_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

-- Creating Category Table
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    icon VARCHAR(100) NOT NULL
);

-- Creating Element Table
CREATE TABLE IF NOT EXISTS element (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_file VARCHAR(100) NOT NULL,
    text_description VARCHAR(255) NOT NULL,
    category_id INTEGER,
    date_added DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category_id) REFERENCES category(id)
);

-- Creating Score Table
CREATE TABLE IF NOT EXISTS score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_id INTEGER,
    score INTEGER NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(child_id) REFERENCES child_profile(id)
);

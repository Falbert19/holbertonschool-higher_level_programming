-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Select the database
USE hbtn_0c_0;

-- Convert the table to UTF8MB4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the column "name" to UTF8MB4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

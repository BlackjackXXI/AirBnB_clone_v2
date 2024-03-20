-- Create the database if not already existing
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user hbnb_dev
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY hbnb_dev_pwd;
-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;

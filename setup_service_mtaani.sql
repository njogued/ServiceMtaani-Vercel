CREATE DATABASE IF NOT EXISTS service_mtaani;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin2023';
GRANT ALL ON `service_mtaani`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

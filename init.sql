CREATE USER administrator WITH PASSWORD 'administrator';
GRANT ALL PRIVILEGES ON DATABASE odoo TO pato;
-- ALTER USER odoo CONNECTION LIMIT 1;
-- ALTER USER odoo CONNECTION LIMIT TO '127.0.0.1/32';
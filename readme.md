docker exec -it odoo_web_1 bash
docker stop odoo_db_1 odoo_web_1 

docker volume rm odoo_odoo-db-data odoo_odoo-web-data 

docker-compose -f "docker-compose.yml" up -d --build
docker-compose -f "docker-compose.yml" down

tqcbdhnedq

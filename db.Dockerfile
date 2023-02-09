FROM postgres:13
COPY pg_hba.conf /var/lib/postgresql/data/
COPY init.sql /docker-entrypoint-initdb.d/
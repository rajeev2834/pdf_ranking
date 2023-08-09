@echo off

set PG_DB=pdfranking
set PG_PASSWORD=sa123
set PG_SERVICE_NAME=postgres
set PG_USER=postgres
set SKEY="django-insecure-0=f)5!03#ueg&vg4k1pag#wu^pu1st0k6i3#tw!&4k(1@58*zz"

Echo POSTGRES_DB=%PG_DB% > .env
Echo POSTGRES_PASSWORD=%PG_PASSWORD% >> .env
Echo POSTGRES_USER=%PG_USER% >> .env
Echo DATABASE_URL=postgres://%PG_USER%:%PG_PASSWORD%@%PG_SERVICE_NAME%:5432/%PG_DB% >> .env
Echo SECRET_KEY=%SKEY% >> .env
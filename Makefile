build:
	docker-compose build

up:
	docker-compose up -d


start:
	docker-compose start

stop:
	docker-compose stop

shell-nginx:
	docker exec -ti nz01 bash

shell-web:
	docker exec -ti dz01 bash

shell-db:
	docker exec -ti pz01 bash

log-nginx:
	docker-compose logs nginx

log-web:
	docker-compose logs web

log-db:
	docker-compose logs db

collectstatic:
	docker exec dg01 /bin/sh -c "python manage.py collectstatic --noinput"

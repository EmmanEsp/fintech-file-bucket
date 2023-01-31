up:
	test -f .env | cp .env.dist .env
	docker-compose up --build --detach

down:
	docker-compose down

create-migration:
	docker-compose run --rm migration dbmate new ${NAME}

migrate-up:
	docker-compose run --rm migration dbmate -e "DATABASE_URL" -d "./db/migrations" up

migrate-down:
	docker-compose run --rm migration dbmate -e "DATABASE_URL" -d "./db/migrations" down

test:
	poetry run coverage run -m pytest

test-report:
	poetry run coverage report

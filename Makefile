server:
	uvicorn src.main:app --reload

docker_storages:
	docker compose up --build

mongo_shell:
	docker compose exec mongodb mongosh

test:
	pytest -vv -s

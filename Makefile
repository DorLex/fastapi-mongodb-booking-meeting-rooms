server:
	uvicorn src.main:app --reload

docker_up:
	docker compose up --build

test:
	pytest -vv -s

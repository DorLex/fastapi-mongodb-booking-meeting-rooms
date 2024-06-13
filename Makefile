server:
	uvicorn src.main:app --reload

test:
	pytest -vv -s

start:
	uvicorn --host 0.0.0.0 --port 8000 source.infrastructure.fastapi:app

start-dev:
	uvicorn --host 0.0.0.0 --port 8000 --reload --reload-dir source source.infrastructure.fastapi:app

test:
	pytest -s -m "not integration"

test-integration:
	pytest -s

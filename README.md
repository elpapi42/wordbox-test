## How to run the application
0. Create .env
```bash
cp .env.example .env
```
1. Spin up the containers
```bash
docker-compose up -d --build
```
2. Run database migrations
```bash
docker exec users-service poetry run alembic upgrade head
```
4. Check the API docs on http://localhost:8001/docs

## Run the test
1. Install dependencies with poetry
```bash
poetry install
```
2. Run the basic test
```bash
poetry run make test
```
3. If you want to run integration tests, you will need a postgres database up and running, follow the "How to run the application" section
4. Run the full test suit 
```bash
poetry run make test-integration
```

## Live deployment

http://wordbox-test-93fm5.ondigitalocean.app/docs
POST http://wordbox-test-93fm5.ondigitalocean.app/users
GET http://wordbox-test-93fm5.ondigitalocean.app/users/:uuid

PD: I deployed to Digital Ocean App Platform, but for some unknow reason DO is intercepting my POST request and converting it to a GET request, weird. I do not have anymore time to solve this.

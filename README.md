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

* Docs
```
http://wordbox-test-93fm5.ondigitalocean.app/docs
```

* Create user
```bash
curl --request POST \
  --url https://wordbox-test-93fm5.ondigitalocean.app/users \
  --header 'Content-Type: application/json' \
  --data '{
        "email": "whitman@email.com",
        "name": "whitman",
        "last_name": "bohorquez",
        "phones": ["9876556432"]
}'
```

* Retrieve user
```
curl --request GET --url https://wordbox-test-93fm5.ondigitalocean.app/users/4c46288e-d09b-4e6f-95cf-baec94b5a9ae
```

## References

I recycled code from an old project i created few months ago: https://github.com/elpapi42/reactive-microservices-with-kafka-python

# script-template

In this README, we are going to provide all the necessary instructions to run the application.

# Branches

- In the `template` branch, we have a template to start any parser exercise.
- In the `main` branch, we have the very first parser exercise I made.

## Playwright setup

```bash
playwright install
```

## Set up the virtual environment

```bash
python -m venv .venv # For venv creation
source .venv/bin/activate
pip install -r requirements.txt
```

## Start the the app

```bash
python -m src.main
```
or, using the docker compose command...

```bash
docker-compose build --no-cache  # Only for building
docker-compose up --build
```

## Run the tests

```bash
pytest
```

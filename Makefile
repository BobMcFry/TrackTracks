
POETRY=poetry
POETRY_RUN=${POETRY} run

.PHONY: format
format:
	${POETRY_RUN} ruff format .

.PHONY: lint
lint:
	${POETRY_RUN} ruff check .

.PHONY: type
type:
	${POETRY_RUN} mypy .

.PHONY: requirements
requirements:
	${POETRY} export --format requirements.txt --output requirements.txt

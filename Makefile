POETRY_RUN=poetry run

.PHONY: format
format:
	${POETRY_RUN} ruff format .

.PHONY: lint
lint:
	${POETRY_RUN} ruff check .

.PHONY: type
type:
	${POETRY_RUN} mypy .

UV=uv
UV_RUN=${UV} run
.DEFAULT_GOAL := clean-up

.PHONY: clean-up
clean-up: format lint type

.PHONY: format
format:
	${UV_RUN} ruff format .

.PHONY: lint
lint:
	${UV_RUN} ruff check --fix .

.PHONY: type
type:
	${UV_RUN} mypy --install-types .

.PHONY: generate_qr_codes
generate_qr_codes:
	PYTHONPATH=. ${UV_RUN} python tracktracks/main/generate_qr_codes.py

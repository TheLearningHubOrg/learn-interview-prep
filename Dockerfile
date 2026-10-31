# Production Dockerfile for the Learn Interview Prep practice suite
#
# Stage 1 runs the JavaScript solutions' tests; the build fails if they fail.
# Stage 2 installs pytest and runs the Python suite as an unprivileged user.
#   docker build -t learn-interview-prep .
#   docker run --rm learn-interview-prep

FROM node:24-alpine AS js-tests
WORKDIR /src
COPY package.json ./
COPY practice/js/ practice/js/
RUN npm test

FROM python:3.13-slim AS runner
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements-dev.txt pyproject.toml ./
RUN pip install -r requirements-dev.txt \
 && useradd --create-home --uid 10001 runner
COPY practice/python/ practice/python/
USER runner
CMD ["python", "-m", "pytest", "-p", "no:cacheprovider"]

#!/usr/bin/env bash
# Wait for a Docker Compose service to report healthy
set -euo pipefail
SERVICE_NAME=${1:-basic-flask-server-web-1}
TIMEOUT=${2:-60}
INTERVAL=${3:-2}
echo "Waiting for container $SERVICE_NAME to be healthy (timeout=${TIMEOUT}s)"
start=$(date +%s)
while true; do
  status=$(docker inspect --format '{{.State.Health.Status}}' "$SERVICE_NAME" 2>/dev/null || echo "notfound")
  if [[ "$status" == "healthy" ]]; then
    echo "Container $SERVICE_NAME is healthy"
    exit 0
  fi
  now=$(date +%s)
  if (( now - start > TIMEOUT )); then
    echo "Timed out waiting for $SERVICE_NAME to become healthy (last status: $status)" >&2
    docker inspect "$SERVICE_NAME" --format '{{json .State.Health}}' || true
    exit 2
  fi
  echo "Status: $status; waiting..."
  sleep "$INTERVAL"
done

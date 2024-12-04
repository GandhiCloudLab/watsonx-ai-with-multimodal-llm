#!/usr/bin/env bash

echo "docker run Started ...."

DOCKER_IMAGE=gandigit/mmllm-svc

echo "Hope this is valid .... WATSONX_API_KEY --> $WATSONX_API_KEY"

podman run -d -p 3001:3001 --name mmllm-svc-mac \
    --env LOGLEVEL=DEBUG \
    --env WATSONX_API_KEY=$WATSONX_API_KEY \
    gandigit/mmllm-svc-mac:latest

echo "run completed ...."
#!/bin/bash

# Build image from Dockerfile
docker build -t edenwaters12Ilovepdf .

# Run container from the built image
docker run -it --rm edenwaters12Ilovepdf

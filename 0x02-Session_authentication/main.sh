#!/bin/bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
# task0
curl "http://0.0.0.0:5000/api/v1/status" -vvv

# task 1
curl "http://0.0.0.0:5000/api/v1/unauthorized"
curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv

# task2
curl "http://0.0.0.0:5000/api/v1/forbidden"
curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv

#!/bin/bash
curl -X POST \
  http://localhost:8280/nodejs-service-api/ \
  -H 'Content-Type: application/xml' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Harry James Potter",
	"house": "Gryffindor"
      }'

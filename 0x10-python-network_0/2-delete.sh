#!/bin/bash
# Send a DELETE request to a given URL and display the response body.
curl -sLI -X DELETE "$1"

#!/bin/bash

mjml_file="./en.mjml"

cat "$mjml_file" | tr -d '\n\r' |  sed 's/"\([^"]*\)"/'\''\1'\''/g' > ./mjml2api.mjml

text=$(<mjml2api.mjml)

curl -X POST https://api.mjml.io/v1/render \
    -H "Content-Type: application/json" \
    --user "username_token:password_token" \
    -d '{"mjml":"'"$text"'"}'


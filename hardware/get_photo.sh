#!/bin/bash

TOKEN=`curl -H "Content-Type: application/json" \`
     -X POST \
     -d '{"user":{"email":"wanjacquot@gmail.com ","password":"dycqI7-kidquh-bockir"}}' \
     https://my.farm.bot/api/tokens | jq ".token.encoded" --raw-output



IMAGES=`curl -H "Authorization: Bearer ${TOKEN}" "https://my.farm.bot/api/images" | jq 'map(.attachment_url)' | jq -r '.[]'`
for url in $IMAGES; do
  curl ${url} --remote-name;
done

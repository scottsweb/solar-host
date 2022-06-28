#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Deploy scott.ee
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📤

# Documentation:
# @raycast.description Create production build and deploy to hosts.
# @raycast.author Scott Evans
# @raycast.authorURL https://scott.ee


git clone git@github.com:scottsweb/scott.ee.git /tmp/scott-deploy
cd /tmp/scott-deploy
npm install
npm run generate
rsync -vrl --delete --progress --update --exclude 'solar.json'  /tmp/scott-deploy/dist/ pilot@host-backup.lan:~/docker/web/
## only deploy here if solar host is online?
rsync -vrl --delete --progress --update --exclude 'solar.json'  /tmp/scott-deploy/dist/ pilot@host-solar.lan:~/docker/web/
rm -rf /tmp/scott-deploy

echo "Deployed: scott.ee"

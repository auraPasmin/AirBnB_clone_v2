#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

# Update upgrade and install
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'

# make dirs
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create page
echo "Holberton School" > /data/web_static/releases/test/index.html

# link files
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu: /data/

# write default
printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;
        root /usr/share/nginx/html;
        index index.html index.htm;
        server_name localhost;
        location / {
                try_files $uri $uri/ =404;
        }
        location /hbnb_static/ {
        alias /data/web_static/current/;
        }
}" > /etc/nginx/sites-available/default


# start service
service nginx restart
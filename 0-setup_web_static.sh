#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

echo "<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>This is a test page</h1>
    <p>Holberton School</p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo sed -i '/hbnb_static/ d' /etc/nginx/sites-available/default
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart

#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx

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
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

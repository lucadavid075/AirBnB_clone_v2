#!/usr/bin/env bash
# Creating server configuration
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R root:root /data
serverblock="server_name\ _;\\n\\n\\tlocation\ \/hbnb_static\/\ {\\n\\t\\talias\ \/data\/web_static\/current\/;\\n\\t}\\n"
sudo sed -i "s/server_name _;/$serverblock/" /etc/nginx/sites-available/default
sudo service nginx restart

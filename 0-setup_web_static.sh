#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo service nginx start
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "ubuntu":"ubuntu" /data/
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
loc="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t}"
sed -i "53i $loc" /etc/nginx/sites-available/default
sudo service nginx restart

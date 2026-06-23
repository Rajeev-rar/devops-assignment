Server Security Measures

1. Firewall

sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable

2. Fail2ban

sudo apt install fail2ban

3. Disable Root Login

PermitRootLogin no
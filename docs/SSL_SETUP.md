SSL Setup

In production environment SSL can be configured using:

- Domain Name
- Let's Encrypt
- Certbot

Commands:

sudo apt install certbot python3-certbot-nginx

sudo certbot --nginx -d yourdomain.com
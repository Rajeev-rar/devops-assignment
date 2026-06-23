Backup Strategy

Database backup command:

docker exec postgres_container pg_dump -U admin appdb > backup.sql

Backups can be scheduled using cron jobs.

Restart Strategy

Docker containers use:

restart: always

Containers restart automatically after server reboot.
"""
Backup the database (MySQL example).
"""
import os
import datetime

DB_NAME = os.getenv("DB_NAME", "flowerp")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")
BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
filename = f"{BACKUP_DIR}/backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

os.system(f"mysqldump -u{DB_USER} -p{DB_PASS} {DB_NAME} > {filename}")
print(f"Backup saved to {filename}")
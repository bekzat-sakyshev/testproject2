import sqlite3

def create_backup(db_file='test.db', backup_file='backup.db'):
    conn = sqlite3.connect(db_file)
    backup_conn = sqlite3.connect(backup_file)
    with conn:
        conn.backup(backup_conn)
    conn.close()
    backup_conn.close()
    print("Резервная копия базы данных создана.")

if __name__ == "__main__":
    create_backup()


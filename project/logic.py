import sqlite3

DB_NAME = "assets.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            brand TEXT,
            status TEXT,
            purchase_date TEXT
        )
    """)
    conn.commit()
    return conn

def add_asset(asset):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO assets VALUES (?, ?, ?, ?, ?, ?)",
        (asset.asset_id, asset.name, asset.asset_type,
         asset.brand, asset.status, asset.purchase_date)
    )
    conn.commit()
    conn.close()

def delete_asset(asset_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assets WHERE id = ?", (asset_id,))
    conn.commit()
    conn.close()

def search_asset(asset_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,))
    data = cursor.fetchone()
    conn.close()
    return data

def fetch_all_assets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    data = cursor.fetchall()
    conn.close()
    return data

def dashboard_counts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM assets")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM assets WHERE status='Working'")
    working = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM assets WHERE status='In Repair'")
    repair = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM assets WHERE status='Disposed'")
    disposed = cursor.fetchone()[0]

    conn.close()
    return total, working, repair, disposed


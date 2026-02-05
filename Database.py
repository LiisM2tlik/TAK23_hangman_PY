from datetime import datetime
import sqlite3
import random


DB_FILE = "words.db"

def create_connection(db_file=DB_FILE):
    return sqlite3.connect(db_file)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            player TEXT,
            word TEXT,
            time TEXT 
        )
    """)

    conn.commit()
    conn.close()

def get_random_word():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT word FROM words")
    words = [row[0] for row in cursor.fetchall()]

    conn.close()
    if words:
         return random.choice(words)
    return None

def save_score(player,score,word):
    conn = create_connection()
    cursor = conn.cursor()

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO scores(player,score,word,time) VALUES(?,?,?,?)",
        (player, score, word, time)
    )

    conn.commit()
    conn.close()
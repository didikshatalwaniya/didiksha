import sqlite3

conn = sqlite3.connect('video_profile.db')
cursor = conn.cursor()

# Create a table for video profiles
cursor.execute('''
    CREATE TABLE IF NOT EXISTS video_profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        trending_date DATETIME,
        title TEXT,
        channel_title TEXT,
        category_id INTEGER,
        publish_time DATETIME,
        tags TEXT,
        views INTEGER,
        likes INTEGER,
        dislikes INTEGER,
        comment_count INTEGER,
        thumbnail_link TEXT,
        comments_disabled INTEGER,
        ratings_disabled INTEGER,
        video_error_or_removed INTEGER,
        description TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

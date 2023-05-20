from typing import Union

# import create_video
import sqlite3
import csv

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/update_video_content")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/upload")
async def upload_file():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()

    # Read the CSV file and insert data into the database
    with open("uploads/USvideos.csv", "r", encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row if present

        for row in reader:
            cursor.execute(
                """
                INSERT INTO video_profiles (video_id, trending_date, title, channel_title, category_id, publish_time, tags, views, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    row[14],
                    row[15],
                ),
            )  # Modify column names and number as per your CSV structure
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return {"message": "Data inserted successfully"}


@app.get("/data")
async def get_data():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM video_profiles limit 5")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        keys = [description[0] for description in cursor.description]
        values = list(row)
        data.append(dict(zip(keys, values)))
    return JSONResponse(content=data)


@app.get("/data/{column}/{value}")
async def get_data_by_condition(column: str, value: str):
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM video_profiles WHERE {column} = ?"
    cursor.execute(query, (value,))
    rows = cursor.fetchall()

    data = []
    for row in rows:
        keys = [description[0] for description in cursor.description]
        values = list(row)
        data.append(dict(zip(keys, values)))
    return JSONResponse(content=data)


@app.get("/limit/{limit}")
async def get_limited_data(limit: int):
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM video_profiles LIMIT {limit}"
    cursor.execute(query)
    rows = cursor.fetchall()

    data = []
    for row in rows:
        keys = [description[0] for description in cursor.description]
        values = list(row)
        data.append(dict(zip(keys, values)))
    return JSONResponse(content=data)


@app.get("/getbyid/{id}")
async def get_data_by_id(id: int):
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles WHERE id = ?"
    cursor.execute(query, (id,))
    row = cursor.fetchone()

    if row is None:
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    values = list(row)
    data = dict(zip(keys, values))

    return JSONResponse(content=data)


@app.get("/getbylikes")
async def get_data_by_likes():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles WHERE likes > 100000"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/getbydislikes")
async def get_data_by_dislikes():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles WHERE dislikes > 100000"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/getbycommentcount")
async def get_data_by_comment():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles WHERE comment_count < 1000"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/sortbyviews")
async def get_data_by_views():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles ORDER BY views DESC"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/topfiveviews")
async def get_data_by_topviews():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles ORDER BY views DESC LIMIT 5"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/totalvideos")
async def get_data_by_totalvideos():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM video_profiles"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/mostliked")
async def get_data_by_mostliked():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT * FROM video_profiles ORDER BY likes DESC LIMIT 1"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/avgviews")
async def get_data_by_avgviews():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = "SELECT AVG(views) FROM video_profiles"
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/totalviewsofcategory")
async def get_data_by_viewscategory():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = (
        "SELECT category_id, SUM(views) AS total_views FROM video_profiles GROUP BY"
        " category_id"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/mostpopularcategory")
async def get_data_by_bestcategory():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = (
        "SELECT category_id, SUM(views) AS total_views FROM video_profiles GROUP BY"
        " category_id ORDER BY total_views DESC LIMIT 1"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/highestengagementrate")
async def get_data_by_highestengagementrate():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = (
        "SELECT *, (likes + comment_count + dislikes) AS engagement_rate FROM"
        " video_profiles ORDER BY engagement_rate DESC LIMIT 5"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/avglikesviews")
async def get_data_by_avglikesviews():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = (
        "SELECT category_id, AVG(likes) AS avg_likes, AVG(views) AS avg_views FROM"
        " video_profiles GROUP BY category_id"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)


@app.get("/videosperchannel")
async def get_data_by_videosperchannel():
    conn = sqlite3.connect("video_profile.db")
    cursor = conn.cursor()
    query = (
        "SELECT channel_title, COUNT(*) AS total_videos FROM video_profiles GROUP BY"
        " channel_title ORDER BY total_videos DESC LIMIT 5"
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:  # Check if the rows list is empty
        return JSONResponse(content={}, status_code=404)
    keys = [description[0] for description in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return JSONResponse(content=data)

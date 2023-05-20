# Video Profile API

This API allows you to interact with a video profile database and perform various operations for data read and analysis.

## Setup

# Clone the repository

git clone https://github.com/didikshatalwaniya/didiksha.git

# Install the required dependencies

pip install -r requirements.txt

# Upload data to the database

Place your video data CSV file in the uploads directory.

# Prepare the database

Uncomment the line 3 in the main.py

# Run the following command to insert the data into the database:

uvicorn main:app --reload 

NOTE : Comment again the line 3 in main.py else it will create multiple databases.

# Access the API:

The API will be available at http://localhost:8000.

## API Endpoints

- `GET /upload`: Uploads the video data from a CSV file to the database.
- `GET /data`: Retrieves the first 5 video profiles from the database.
- `GET /data/{column}/{value}`: Retrieves video profiles based on a specific column and value.
- `GET /limit/{limit}`: Retrieves a specified number of video profiles from the database.
- `GET /getbyid/{id}`: Retrieves a video profile by its ID.
- `GET /getbylikes`: Retrieves video profiles with more than 100,000 likes.
- `GET /getbydislikes`: Retrieves video profiles with more than 100,000 dislikes.
- `GET /getbycommentcount`: Retrieves video profiles with less than 1000 comment count.
- `GET /sortbyviews`: Retrieves video profiles sorted by views in descending order.
- `GET /topfiveviews`: Retrieves the top 5 video profiles with the highest views.
- `GET /totalvideos`: Retrieves the count of the total number of videos.
- `GET /mostliked`: Retrieves the video profile with the most likes.
- `GET /avgviews`: Retrieves the average number of views across all video profiles.
- `GET /totalviewsofcategory`: Retrieves the total views of each video category.
- `GET /mostpopularcategory`: Retrieves the most popular video category based on total views.
- `GET /highestengagementrate`: Retrieves the top 5 video profiles with the highest engagement rate (likes + comment_count + dislikes).
- `GET /avglikesviews`: Retrieves the average number of likes and views per video category.
- `GET /videosperchannel`: Retrieves the total number of videos per channel.


# Technologies Used

Python
FastAPI
SQLite

# License

This project is licensed under the MIT License.

Feel free to customize the `README.md` file as per your requirements, providing more information or modifying the content according to your project.

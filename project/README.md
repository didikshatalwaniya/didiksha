# PROJECT

# ML Model Builder

This project is a Flask-based application that builds a machine learning model from CSV data and saves relevant metadata to a MongoDB instance. It consists of multiple components, including an ML component, a Flask API, and a main script.

## Components

The project consists of the following components:

- `app.py`: Flask application file that defines the API endpoints for creating tenant and project metadata records.
- `ml_component.py`: ML component file responsible for processing the CSV data and generating the machine learning model.
- `main.py`: Main script file that orchestrates the workflow by calling the ML component and saving the project metadata record.

## Prerequisites

To run this project, you need the following prerequisites:

- Python 3.x
- MongoDB installed and running
- Required Python packages installed (specified in requirements.txt)

## Installation

1. Clone this repository:

```shell
git clone <repository-url>
cd project

```
## Install the required Python packages:
pip install -r requirements.txt

## Set up the MongoDB connection:

Make sure MongoDB is installed and running on your system or provide the appropriate connection details (e.g., host, port) in app.py.

## Set up environment variables:

Specify the location of the local CSV file and the target column to predict on as environment variables.

## Example:
export CSV_FILE=/path/to/csv/file.csv
export TARGET_COLUMN=target

## Usage
Start the Flask API server:
python app.py

In a separate terminal, run the main script:
python main.py

-The ML component will process the CSV data, generate and evaluate the model.
-The Flask API will save the project metadata record to the MongoDB instance.

## Testing
To run the unit and integration tests:
python -m unittest discover tests

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

Make sure to replace `https://github.com/didikshatalwaniya/didiksha` with the URL of your actual Git repository.

If you have any more questions, please let me know!

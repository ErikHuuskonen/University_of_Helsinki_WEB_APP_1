# University_of_Helsinki_WEB_APP_1

## Python Flask and OpenAI Whisper-Based Web Application

Welcome to my first-ever web application project! This application is built using Python Flask and leverages the OpenAI Whisper library to provide a unique service: converting spoken data from MP4 video files into text. This project was initially developed locally and serves as a practical tool for extracting and storing verbal content from videos in a textual format, facilitating note-taking and content review.

## Project Overview

The core functionality of this web application revolves around processing MP4 video files to transcribe the audio content. It's an ideal solution for users looking to convert lectures, presentations, or any spoken content in videos into written form, making it easier to study, reference, and analyze the material.

### Key Features:

- **Transcription of MP4 Videos**: Utilizes the power of the OpenAI Whisper library to accurately transcribe spoken words into text.
- **Designed for English Content**: While the application primarily focuses on English content, using the Whisper library's "base" package, it sets the foundation for future enhancements to support additional languages.
- **Local Operation**: Currently, the application operates locally, providing a secure and private environment for users to process their video files.

### Inspiration and Education:

This project was inspired by my coursework at the University of Helsinki, specifically the "Databases and Web Programming" course within the Computer Science curriculum. It represents a practical application of the skills and knowledge acquired through my studies, showcasing my ability to integrate sophisticated AI technology with web development principles to create a functional and user-friendly tool.

## Future Directions

While the application currently excels at processing English content, future updates aim to expand language support and possibly include additional features based on user feedback and technological advancements. The goal is to enhance its versatility and accessibility, making it a more comprehensive tool for students, educators, and professionals alike.

Thank you for exploring my project. I look forward to developing it further and seeing the positive impact it can have on your video content analysis and note-taking processes.

# Python Flask Application Setup Guide

This guide will walk you through setting up and running the Flask application from cloning the repository to launching the app.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3
- pip
- Virtual environment (venv) package for Python

## 1. Clone the Repository

First, clone the repository to your local machine by running the following command in your terminal:

```
git clone https://github.com/ErikHuuskonen/University_of_Helsinki_WEB_APP_1
```

## 3. Install Dependencies

Install the project dependencies by running:

```
pip install -r requirements.txt
```

##  4. Using the Schema.sql File for Database Setup

To initialize your database with the required tables and any initial data, you will need to use the `schema.sql` file provided. This file contains SQL commands to create your database schema.

### Apply the Schema.sql File

Before applying the schema, make sure your PostgreSQL database is running and you have created a database that your Flask application will use.

1. **Open a terminal or command prompt.**
2. **Navigate to your project directory** where the `schema.sql` file is located.
3. **Use the `psql` command to apply the schema to your database.** You will need to replace `<yourdatabase>` with the name of your database:

    ```bash
    psql -U <yourusername> -d <yourdatabase> -a -f schema.sql
    ```

    Replace `<yourusername>` with your PostgreSQL user name. If prompted, enter your password for the PostgreSQL user.

This command executes the SQL commands in the `schema.sql` file against your database, creating the necessary tables and inserting any initial data defined in the file.

### Verify the Database Schema

After applying the `schema.sql` file, you can verify that the tables were created successfully by logging into your PostgreSQL database and listing the tables:

```bash
psql -U <yourusername> -d <yourdatabase>
\dt
```

Open the app.py file and locate the following line (around line 16):

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///yourdatabaseurl"
Replace "postgresql:///yourdatabaseurl" with your actual database connection URI. For example:
```

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///mydbname"
```

### 5. Run the Flask Application
Finally, start the Flask application by running:

```
flask run
```

This command will start the server on http://127.0.0.1:5000/. Open this URL in your browser to access the Flask application.


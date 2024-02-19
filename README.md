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

## Project Update: Third Interim Delivery
Date: February 18th
We have successfully made significant progress on our application by the third interim delivery. Below is a summary of the updates and our next steps towards the final submission.

## What's New
New Databases Added: We have integrated two new databases, content and data, into our application. The purpose of these databases is to store users' previous video translations and essential information such as video lengths and names. This feature enhances our application's ability to provide personalized and efficient service to our users.

Deployment via Render: The application is currently being deployed through Render. This step marks a significant milestone as we move from development to production, ensuring that our application is accessible to users in a real-world environment.

Session Verifications: To improve security and user experience, session verifications have been added to each template within the application. This ensures that user sessions are securely managed, protecting both the user data and the integrity of their interactions with our application.

Whisper Translation Model Option: Users now have the option to choose the Whisper translation model for their video translations. This model offers improved translation quality for Finnish language videos, albeit at a slower pace. This feature underscores our commitment to providing versatile and user-centric translation solutions.

## Next Steps
Finalizing HTML Files: Before the final submission, we will focus on defining the remaining HTML files. This involves designing and implementing the user interface components that are essential for a seamless user experience.

Sequential Translations Feature: We aim to add functionality for sequential translations, allowing users to perform multiple translations consecutively without the need to navigate back to the home page via a link. This enhancement will streamline the user workflow, making the translation process more efficient and user-friendly.

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

Make sure that for deployment is commented out and you write you own db name to "#For local" section

```python
#For local
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

#For deployment
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)
```

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///yourdatabaseurl"
Replace "postgresql:///yourdatabaseurl" with your actual database connection URI. For example:
```

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///mydbname"
```

### 5. Run the Flask Application
Finally, start the Flask application by running following command in working directories root:

```
flask run
```


This command will start the server on http://127.0.0.1:5000/. Open this URL in your browser to access the Flask application.

### 5. Run the Flask Application in web browser

The application is now accessible at:

```
https://videototext.onrender.com/
```
Due to the application operating under a free license, video conversion functionality is not available through the web server. This setup is intended for navigating the website and evaluating/testing functionalities other than video-to-text conversion. To convert your videos into text, please follow the local execution method described earlier in this document.

This revised text provides a clearer and more direct explanation, emphasizing the limitations imposed by the free license but still offering clear guidance on how users can utilize the video-to-text conversion feature locally.
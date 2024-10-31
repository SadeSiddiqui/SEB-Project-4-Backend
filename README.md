# Helping Hands (Backend) 


#### Table of Contents
- Introduction
- Project Goals
- Features
- Technologies Used
- Architecture Overview
- Installation
- Environment Variables
- Database Structure
- Authentication & Security
- Error Handling
- Testing
- Deployment
- Future Enhancements
- Contributions
- License
- Contact 


## Introduction 

Helping Hands is an open forum full application it allows people to speard information about physical and mental health conditions, psot comments, and interact with a community. The backend handles user accounts, database management using SQL and PostgreSQL, and ensures secure data interactions. 


## Project Goals 

- Ensure secure user authentication and data storage.
- Handle CRUD operations for conditions and comments

## Features 

- User Authentication (Signup, Login)
- CRUD Operations for Conditions and Comments
- Database Management (PostgreSQL)
- Error Handling and Validation 
- Real-time Feedback with Axios: All API requests (to the backend) for actions like posting or commenting are managed by Axios, ensuring asynchronous, real-time updates, enhancing user interactivity

## Technologies Used

- Node.js and Express: for handling server-side operations 
- PostgreSQL: for the database
- TablePlus: as the GUI for database management
- bcrypt.js: for password hashing
- JWT (JSON Web Tokens): for user authentication and session management
- Axios: for making HTTP requests from the frontend 

  
## Architecture Overview

- ```config/```: Stores app configuration (e.g., environment settings).
- ```controllers/```: Handles logic for requests (e.g., fetching and sending condition data).
- ```middleware/```: Provides a layer for security checks and additional processing.
- ```models/```: Defines the structure of your data in the database.
- ```serializers/```: Converts data between formats for easy backend-frontend communication.
- ```.vscode/```: Contains development-specific settings for VSCode.

## Installation  

1) Clone the repository 

Use ```git clone git@github.com:SadeSiddiqui/SEB-Project-4-Backend.git``` this will download the backend into the users local server but if you are unfamiliar with SSH keys then use the following HTTP code instead ```git clone https://github.com/SadeSiddiqui/SEB-Project-4-Backend.git```

2) Navigate to the repository 

Then In git use this command ```cd git@github.com:SadeSiddiqui/SEB-Project-4-Backend.git``` this will move you into the project directory that the use rnow has a copy of in their computer now.

3) Install the Dependencies 

Before installing the dependencies you have to create a virtual environment to store the dependencies ```pip install pipenv``` 
You also need to set up your virtual environment you do that with this command ```pipenv install``` running this command pipenv will access the pipfile from the project you have cloned scan all the packages and libraries listed in the pipfile and automatically install all the required dependencie. However, if or any situation it doesn't work you can run the following commands to manually install are the dependencies needed. 

```pipenv install flask```

```pipenv install flask-sqlalchemy```

```pipenv install psycopg2-binary```

```pipenv install flask-marshmallow```

```pipenv install marshmallow-sqlalchemy```

```pipenv install flask-bcrypt```

```pipenv install pyjwt```

```pipenv install pytest```

```pipenv install flask-cors```

```pipenv install gunicorn```


## Environment Variables

1) Create a .env file in the root directory of the project if it doesn’t exist already.

2) Add the following variables:

```FLASK_ENV=development```

```FLASK_SKIP_DOTENV=1```

```FLASK_RUN_PORT=4000```

```FLASK_DEBUG=1```

```DATABASE_URL=postgresql://localhost:5432/conditions_db```

```SECRET=correcthorsebatterystaple```

## Database Structure

The database for Helping Hands consists of three main tables: Users, Conditions, and Comments. These tables are related to each other through foreign keys and represent the relationships between users, the conditions they post, and the comments left by users on different conditions.

Users Table

Purpose: Stores information about registered users.

Columns:
- id (Primary Key, Integer): A unique identifier for each user.
- username (Text): The user's login name, which must be unique.
- email (Text): The user's email address, also unique.
- password_hash (Text): The hashed version of the user's password for secure storage.

Relationships:

- A one-to-many relationship with the Conditions table. A single user can create multiple conditions.
- A one-to-many relationship with the Comments table, meaning a single user can leave multiple comments on different conditions.

2. Conditions Table
   
Purpose: Stores information about various physical and mental health conditions.

Columns:
- id (Primary Key, Integer): A unique identifier for each condition.
- name (Text): The name of the condition, which must be unique.
- about (Text): A description of the condition.
- info (Text): Further details and information regarding symptoms, treatments, etc.
- advice (Text): Advice or suggestions for managing the condition.
- user_id (Foreign Key, Integer): Links each condition to the user who created it.

Relationships:
- A one-to-many relationship with the Comments table. Each condition can have multiple comments.
- A many-to-one relationship with the Users table, linking each condition to the user who created it.
  
3. Comments Table
   
Purpose: Stores user-generated comments on specific health conditions.

Columns:
- id (Primary Key, Integer): A unique identifier for each comment.
- content (Text): The body of the comment.
- title (Text): The title or subject of the comment.
- conditions_id (Foreign Key, Integer): Links each comment to a specific condition.
- user_id (Foreign Key, Integer): Links each comment to the user who posted it.
  
Relationships:
- A many-to-one relationship with the Conditions table, meaning each comment is linked to one condition.
- A many-to-one relationship with the Users table, meaning each comment is linked to one user.

Relationships Overview
- Users & Conditions: One user can create multiple conditions.
- Conditions & Comments: Each condition can have multiple comments, but each comment belongs to only one condition.
- Users & Comments: Each user can leave multiple comments, but each comment belongs to one user.

Explanation of the Structure:

- Users Table: Manages all user-related data, including login credentials and relationships with conditions and comments.
- Conditions Table: Stores details about health conditions, with each condition linked to the user who created it.
- Comments Table: Allows users to comment on conditions, each linked to a specific condition and user.

This structure reflects how the data flows between users, conditions, and comments in the backend, allowing for a clear understanding of how CRUD operations work in your application.

## Authentication & Security

The backend of Helping Hands includes the following security measures to protect user data:

User Authentication: Uses JSON Web Tokens (JWT) for secure user authentication. Upon successful login, users are issued a token, which is required for accessing protected endpoints.

Password Hashing: User passwords are hashed using bcrypt, which ensures that passwords are stored securely in the database.

Environment Variables: Sensitive information, such as database URLs and JWT secret keys, are stored in environment variables. These variables are managed securely and excluded from the codebase using .env. 

These security practices ensure secure data handling and maintain user privacy, protecting the system from unauthorized access.

## Error Handling


## Testing


## Deployment


## Future Enhancements

- Suicidal Keywords Detection: The application will monitor for language related to suicide. If detected, a modal window will appear with the message, "We've identified language that may indicate distress related to suicide." This will provide users with immediate access to resources such as the Samaritans helpline, emergency mental health numbers, available therapist contact details, and contact information for users who have opted into the "emergency call list."
- Emergency Call List: Users of the application can volunteer to be part of an "emergency call list," allowing their contact information to be displayed when the suicidal keywords detection system is triggered. This provides peer support options in addition to professional resources.
- Community Support: Each health condition on the platform will feature a "Community" button, leading to a dedicated page for users living with that specific condition, fostering a sense of connection and support among those with shared experiences.

## Contributions


## License

Licensing: This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Acknowledgements: A big thank you to collaborator Evyn-Rose Goldstein [evynrose](https://github.com/evynrose) with her help in this project. 

## Contact 

Feel free to reach out for questions or collaboration opportunities: 

Syed Siddiqui: 

[LinkedIn](https://www.linkedin.com/in/syed-siddiqui/)

[Email](syedsiddiqui1@gmail.com)

Evyn-Rose Goldstein: 

[LinkedIn](https://www.linkedin.com/in/evynrose/)












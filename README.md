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


## Authentication & Security


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












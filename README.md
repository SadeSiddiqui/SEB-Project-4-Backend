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


## Environment Variables


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












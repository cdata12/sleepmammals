# SleepMammals Application - Setup Guide
This README provides detailed instructions for setting up and deploying the SleepMammals Streamlit application, which is designed to showcase machine learning models. The application setup is tailored for an Ubuntu environment running in VMware Workstation 17 Player, with Visual Studio Code as the recommended IDE.

[streamlit application link](https://sleepmammals-app-76bb33805c34.herokuapp.com/)

## Prerequisites

- **IDE**: Visual Studio Code
- **OS**: Ubuntu (VMware Workstation 17 Player)

## Setup Instructions

### Initial Setup

1. **Launch the Ubuntu VM** and open a terminal.

2. **Install Python**:
    ```bash
    $pip install python=="3.9.12"
    ```

### Account Creation

3. **Sign up for a Heroku account** at [Heroku Sign Up](https://signup.heroku.com/). Students can link their account to GitHub for a potential $160 credit, which may take a few days to process.

4. **Sign up for a Docker account** at [Docker Sign In](https://login.docker.com/).

### Project Setup

5. **Clone the project repository**:
    ```bash
    git clone https://github.com/cdouadi/sleepmammals.git
    ```

6. **Change to the project directory**:
    ```bash
    cd sleepmammals/webapp
    ```

7. **Create a virtual environment**:
    ```bash
    python3 -m venv sleepmammals-env
    ```

8. **Activate the virtual environment**:
    ```bash
    source sleepmammals-env/bin/activate
    ```

9. **Install required dependencies** (if you plan to test locally):
    ```bash
    pip install -r requirements.txt
    ```

### Testing Locally

10. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

### Dockerization

11. **Build the Docker image**:
    ```bash
    docker build . -t sleepmammals-app
    ```

12. **Run the Docker container** (enables live code updates):
    ```bash
    docker run -it -v "$(pwd):/home/app" -e PORT=4000 -p 4000:4000 sleepmammals-app
    ```
    Access the app at: `http://0.0.0.0:4000`

### Deployment to Heroku

13. **Log in to Docker**:
    ```bash
    docker login
    ```

14. **Log in to Heroku and authenticate**:
    ```bash
    heroku login
    heroku container:login
    ```

15. **Create a Heroku application**:
    ```bash
    heroku create sleepmammals-app
    ```

16. **Deploy the application on Heroku**:
    ```bash
    heroku container:push web -a sleepmammals-app
    heroku container:release web -a sleepmammals-app
    ```

17. **Open your deployed application**:
    ```bash
    heroku open -a sleepmammals-app
    ```
    If the application doesn't open directly, use the provided URL, such as `https://sleepmammals-app-76bb33805c34.herokuapp.com/`.

18. **Manage your application** via the Heroku dashboard: [Heroku Dashboard](https://dashboard.heroku.com/apps/sleepmammals-app)

### Cleanup

19. **Deactivate the virtual environment** once finished:
    ```bash
    deactivate
    ```

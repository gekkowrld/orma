# Rent Management System

Welcome to the Rent Management System! This project is a simple backend API for managing rental properties. This guide will help you set up and run the project on your local machine, even if you're new to Python and programming.

## Getting Started

### 1. Clone the Repository

If you don't have the code on your machine yet, you can get it by cloning the repository from GitHub. Open your terminal or command prompt and run the following command:

```sh
git clone https://github.com/gekkowrld/orma.git
```

This will create a local copy of the project in a folder named `orma`.

### 2. Navigate to the Project Directory

Move into the project directory where the `README.md` file is located:

```sh
cd orma
```

### 3. Set Up Your Environment

Before you start, you'll need to install Python and set up a virtual environment. Here’s how:

#### Install Python

If you don’t have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/). Make sure to check the box that says **"Add Python to PATH"** during the installation process.

#### Create a Virtual Environment

A virtual environment is a self-contained directory where you can install dependencies for this project without affecting other projects or your system’s global Python environment.

1. **Open your terminal or command prompt.**

2. **Navigate to the project directory** (where you just cloned the repository):

   ```sh
   cd orma
   ```

3. **Create a virtual environment** using the following command:

   ```sh
   python -m venv orma
   ```

   This creates a directory named `orma` that contains the virtual environment.

4. **Activate the virtual environment**:

   - **On Windows:**
     ```sh
     orma\Scripts\activate
     ```

   - **On macOS or Linux:**
     ```sh
     source orma/bin/activate
     ```

   When the virtual environment is activated, you should see `(orma)` at the beginning of your command line prompt.

### 4. Install Dependencies

Once your virtual environment is activated, you need to install the required packages for the project. These packages are listed in the `requirements.txt` file.

Run the following command:

```sh
pip install -r requirements.txt
```

This command will download and install all the necessary packages for the project.

### 5. Configure the Environment

Create a file named `.env` in the root of the project directory (where this README is located). Add the following line to the `.env` file:

```env
DB_NAME="orma.db" # You can use any name you like for your database file
```

This file is used to store configuration settings for your application.

### 6. Run the Program

You can run the application in two different modes:

- **For Development:** This mode is for testing and development. It includes tools for debugging and automatically reloading the server.

  ```sh
  fastapi dev main.py
  ```

- **For Production:** This mode is for deploying the application for real use. It’s optimized for performance and stability.

  ```sh
  fastapi run
  ```

  The application will be accessible on port `8000`. You can view it in your web browser:

  - **Development:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
  - **Production:** [http://0.0.0.0:8000](http://0.0.0.0:8000) (this allows access from any IP address)

### 7. Access the API Documentation

Once the application is running, you can access the API documentation at:

- **Development:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Production:** [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

This page will show you the available API endpoints and allow you to test them.

## Troubleshooting

If you encounter any issues, here are some things you can check:

- **Python is not recognized:** Make sure you have Python installed and added to your PATH.
- **Command not found:** Ensure your virtual environment is activated.
- **Dependencies not installing:** Check for errors during `pip install` and make sure `requirements.txt` is up-to-date.

If you need more help, try searching for the error message you see online or ask for help in programming communities.

## Resources

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Official Python guide on virtual environments
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - FastAPI’s official documentation for more details on using the API

Happy coding!

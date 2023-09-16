# Catfish.IO

This is a FastAPI application that provides a REST API for the Catfish.IO project.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Development](#development)
  - [Running Locally](#running-locally)
  - [Testing](#testing)
  - [Linting](#linting)
- [Deployment](#deployment)
  - [Using Docker Compose](#using-docker-compose)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://www.docker.com/get-started) installed on your system.
- [Poetry](https://python-poetry.org/docs/) for managing Python dependencies.
- [Pre-commit](https://pre-commit.com/) for linting and formatting.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/danisc23/catfish-io.git
   ```

2. Change to the project directory:

   ```bash
   cd catfish-io
   ```

3. Install the project dependencies using Poetry:

   ```bash
   poetry install
   ```

4. Install pre-commit hooks to ensure consistent code style:

   ```bash
   pre-commit install
   ```

## Development

### Running Locally

To run the application locally, use Poetry's virtual environment:

```bash
poetry shell
uvicorn catfishio.main:app --host=0.0.0.0 --port=8080 --reload
```

The application will be available at `http://localhost:8080`.

In this early version, the application is not connected to a database. Instead, it uses the url to set the username, so you can test it by opening two different browsers and using the following urls:

`localhost:8080/web/chat/yoursusername` and `localhost:8080/web/chat/otherusername`


### Testing

We use pytest for testing the application. To run the tests, execute the following command:

```bash
poetry run pytest .
```

### Linting

Linting is done using pre-commit hooks. Before committing your code, linting and formatting checks will run automatically. If there are any issues, pre-commit will prevent the commit and inform you of the problems that need to be fixed.

You can also run the pre-commit checks manually using the following command:

```bash
pre-commit run --all-files
```

## Deployment

### Using Docker Compose

To run the application in a Docker container, follow these steps:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the Docker container:

   ```bash
   docker-compose up -d
   ```

The FastAPI application should now be accessible at `http://localhost:8080`.

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

### TODO

- [ ] Auth. Maybe we can delegate the authentication to an external service like Auth0 (github, google, etc)
- [ ] Use a database to store the messages and the users, since sessions are not persistent we can use a NoSQL database like redis
- [ ] Currently the web is just a mock to test the websocket, we can use a frontend framework like React or Vue to make it more user friendly


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

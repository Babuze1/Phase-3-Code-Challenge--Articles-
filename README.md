# Magazine Domain Project

This project implements a simple system for managing authors, articles, and magazines in a magazine domain. It allows you to create authors, magazines, and articles and establish relationships between them.

## Folder Structure

The project follows the following folder structure:

project_folder/
│
├── lib/
│ ├── Author.py
│ ├── Article.py
│ └── Magazine.py
│ └── main.py
│
├── Pipfile
└── README.md

- `classes/`: Contains the Python class files `Author.py`, `Article.py`, and `Magazine.py` that define the project's data model and methods.
- `tools/`: Contains the `debug.py` script for testing and debugging the classes and methods.
- `Pipfile`: Specifies the project's Python version and potential dependencies.
- `README.md`: The file you're currently reading, providing an overview of the project.

## Usage

1. Clone the repository:

git clone https://github.com/Babuze1/Phase-3-Code-Challenge--Articles-

2. Navigate to the project folder:

cd magazine-domain-project

3. Install Pipenv if you haven't already:

pip install pipenv

4. Install dependencies and create a virtual environment:

pipenv install

5. Run the `debug.py` script to test and interact with the implemented classes:

pipenv run python tools/debug.py

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to explore, modify, and expand upon this project as needed for your use case.

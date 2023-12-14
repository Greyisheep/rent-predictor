# Rent Predictor
This project helps people get started with pen source by makin contribution easier, but yet following best prectices as it is a relatable project. Rent predictor looks to help students with apartment serach as it provides search functions as well as easily accessible databases in form of spreadsheets. The model package gives in sights on prices of apartments in different areas to help students get an idea of what apartment prices in differnt areas are helping the student streamline their search location. As the data collection is open-source, it is easily accessible, usable and verifiable by the end users.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Project Setup](#project-setup)
3. [Data](#data)
4. [Goals](#goals)
5. [Next Steps](#next-steps)
6. [Contributing](#contributing)
7. [Happy Coding!!!](#happy-coding)

## Built with
![python](https://img.shields.io/badge/python-%232b5b84?logo=python&logoColor=white&link=https%3A%2F%2Fwww.python.org%2F)
![jupyter](https://img.shields.io/badge/jupyter-%23e46e2e?logo=jupyter&logoColor=white&link=https%3A%2F%2Fjupyter.org%2F)
![FastAPI](https://img.shields.io/badge/FastAPI-grey?logo=fastapi&logoColor=white&color=%23007a6c&link=https%3A%2F%2Ffastapi.tiangolo.com%2F)
![NumPy](https://img.shields.io/badge/NumPy-%234d77cf?logo=numpy&logoColor=white&link=https%3A%2F%2Fnumpy.org%2F)
![pandas](https://img.shields.io/badge/pandas-%236f42c1?logo=pandas&logoColor=white&link=https%3A%2F%2Fpandas.pydata.org%2F)
![Pydantic](https://img.shields.io/badge/Pydantic-%23e92063?logo=pydantic&logoColor=white&link=https%3A%2F%2Fdocs.pydantic.dev%2Flatest%2F)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23FF9C34?logo=scikitlearn&logoColor=white&link=https%3A%2F%2Fscikit-learn.org%2Fstable%2F)
![pytest](https://img.shields.io/badge/pytest-rgb(0%2C%20159%2C%20227)?logo=pytest&logoColor=white&link=https%3A%2F%2Fdocs.pytest.org%2Fen%2F7.4.x%2F)
![React](https://img.shields.io/badge/React-%23087ea4?logo=react&logoColor=white&link=https%3A%2F%2Freact.dev%2F)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow?logo=javascript&logoColor=white&link=https%3A%2F%2Fwww.javascript.com%2F)

## License
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL_v2.1-blue.svg)](https://www.gnu.org/licenses/lgpl-2.1)

## Installation

Follow these steps to set up and run rent-predictor on your local machine.

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

**Optional (The README is written with this set of Prerequisites in mind)**

- [git](https://git-scm.com/downloads) (Distributed Version Control System, and terminal)
- [VSCode](https://code.visualstudio.com/download) (integrated development environment)
- [Node.Js](https://nodejs.org/en/download) (JavaScript runtime environment)


### Clone the Repository

1. Open the git bash terminal by searching for it
2. [Navigate to choice of location for project](https://www.nobledesktop.com/learn/git/command-line-basics#:~:text=Commands%20such%20as%20cd%20are,the%20contents%20of%20a%20folder.)
3. Clone the repository with:

```bash
git clone https://github.com/Greyisheep/rent-predictor
cd rent-predictor/house_prices_api
```


### Create a Virtual Environment

4. Type `code .` and hit `enter` button; this takes you to vscode
5. In vscode, press `ctrl` + ` ; which opens up a terminal, [navigate to the gitbash terminal](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#:~:text=If%20you%20want%20to%20set,be%20opened%20with%20Git%20Bash.)
6. Create a Virtual Environment with:


```bash
python -m venv venv
```

### Activate the Virtual Environment

#### For Windows:

```bash
source venv/Scripts/activate
```

#### For MacOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### For the Front-end setup
7. Navigate to the react-frontend directory

```bash
cd ../simple_frontend/react-frontend/
```

## Using npm
8. Run the following command to install the dependencies:
```bash
npm install
```

## Using yarn
8. Run the following command to install the dependencies:
```bash
yarn install
```

## Data
If you want your apartment to be displayed in our database. Kindly fill out the following Google form:

[Google Form Link](https://forms.gle/xHqq2mQ4yi1C6sTR8)

The data for this project is available in a Google Sheets spreadsheet. The spreadsheet contains data on rent prices and apartment features for different locations in Nigeria. To access the spreadsheet, click on the following link:

[Spreadsheet Link](https://docs.google.com/spreadsheets/d/1l4Ea9PXEXv_GwcIWTORX_oK6TgZds7yTrek-fGLbJq8/edit?usp=sharing)

## Goals

The goals of this project are to:

* Create an open-source apartment search and prediction web app for students in Nigeria.
* Make it easier for students to find affordable apartments that meet their needs.
* Help students to save money on rent.

## Next Steps

The next steps for this project are to:

1. Design and integrate a dashboard for good data visualization.
2. Package the model for production.
3. Serve and deploy the model via FASTAPI.
4. Set up continuous integration and deployment pipelines.
5. Deploy the ML API with containers.
6. Set up differential testing.
7. Set up other backend protocols for user authentication, search, etc.
8. Build a React-based front end for the application.
9. Conduct full integration testing.

## Contributing

We welcome contributions to this project! To contribute, please fork the repo and create a pull request with your changes. Please make sure to test your changes and include a clear and concise description of what your changes do.

## Happy Coding!!!

We hope you enjoy working on this project!


---
## If you see this, it means you are an awesome person, showing interest in this project. This README.md file is undergoing a reconstruction to keep it up to date, hence its minor discontinuity.

1. **Title and Description:**
   - Start with a clear and concise title for your project.
   - Provide a brief description of what your project does.

2. **Table of Contents:**
   - Include a table of contents to help users quickly navigate through different sections of the README.

3. **Badges:**
   - Add relevant badges (e.g., build status, version, license) to provide additional information at a glance.

4. **Installation:**
   - Clearly outline the steps required to install your project. Include dependencies, environment setup, and any other necessary instructions.

5. **Usage:**
   - Explain how to use your project. Include code examples, command-line instructions, and screenshots if applicable.
   - Provide a list of features and functionality.

6. **Configuration:**
   - If your project requires configuration, explain how users can configure it. Include information about configuration files or environment variables.

7. **Contributing:**
   - Specify guidelines for contributing to your project. Include information about how to report issues, suggest improvements, and submit pull requests.
   - If you have a code of conduct, mention it in this section.

8. **Testing:**
   - Provide instructions on how to run tests if applicable.
   - Include information about the testing framework used.

9. **Documentation:**
   - Link to any additional documentation, such as API documentation or user manuals.

10. **License:**
    - Clearly state the license under which your project is distributed. This is important for users and potential contributors to understand the terms under which they can use, modify, and distribute your code.

11. **Acknowledgements:**
    - Give credit to any third-party libraries, tools, or resources that your project relies on.

12. **FAQ or Troubleshooting:**
    - Anticipate common questions or issues and address them in this section.

13. **Contact Information:**
    - Provide a way for users and contributors to get in touch with you.

14. **Changelog:**
    - Keep a changelog to document the changes made in each version of your project.

15. **Demo or Screenshots:**
    - Include links to demos or add screenshots to showcase the project.

16. **Example:**
    - Provide a simple example of how your project can be used.

17. **Dependencies:**
    - List the major dependencies with their version numbers.

18. **Badge for Build Status:**
    - If your project has continuous integration, display a badge for the build status (e.g., Travis CI, CircleCI).

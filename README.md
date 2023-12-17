# Rent Predictor

Rent Predictor is an open-source project designed to simplify contributions for those new to open source, adhering to best practices while addressing a common and relatable issue—apartment searching for students. The project offers search functionalities and easily accessible databases in the form of spreadsheets. The model package provides insights into apartment prices in different areas, aiding students in streamlining their search locations. The open-source nature of the data collection ensures accessibility, usability, and verifiability for end-users.

## Table of Contents

1. [Built with](#built-with)
2. [License](#license)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Data](#data)
7. [Goals](#goals)
8. [Next Steps](#next-steps)
9. [Contributing](#contributing)
10. [Contact Information](#contact-information)

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

Follow these steps to set up and run Rent Predictor on your local machine.

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

**Optional (The README is written with this set of Prerequisites in mind)**

- [git](https://git-scm.com/downloads) (Distributed Version Control System, and terminal)
- [VSCode](https://code.visualstudio.com/download) (integrated development environment)
- [Node.Js](https://nodejs.org/en/download) (JavaScript runtime environment)


### Clone the Repository

1. Open the Git Bash terminal by searching for it
2. [Navigate to the choice of location for the project](https://www.nobledesktop.com/learn/git/command-line-basics#:~:text=Commands%20such%20as%20cd%20are,the%20contents%20of%20a%20folder.)
3. Clone the repository with:

```bash
git clone https://github.com/Greyisheep/rent-predictor
cd rent-predictor/house_prices_api
```

### Create a Virtual Environment

4. Type `code .` and hit the `enter` button; this takes you to VSCode
5. In VSCode, press `ctrl` + ` which opens up a terminal, [navigate to the Git Bash terminal](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#:~:text=If%20you%20want%20to%20set,be%20opened%20with%20Git%20Bash.)
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

### Install the Dependencies

#### Using npm
8. Run the following command to install the dependencies:
```bash
npm install
```

#### Using yarn
8. Run the following command to install the dependencies:
```bash
yarn install
```

## Usage
**To try out functionalities of the API, change the directory into `house_prices_api`**

### Functionalities available:
- Train the pipeline by running:
```python
python model_package/regression_model/train_pipeline.py
```
- Start Uvicorn server by running:
```python
python app/main.py
```
![README2](https://github.com/Greyisheep/rent-predictor/assets/97015429/f58aa3a6-5b99-44d6-a728-5c124b6b7565)

- Test the API by running:
`pytest`
![README3](https://github.com/Greyisheep/rent-predictor/assets/97015429/e6c121e3-fb91-4656-a0e1-0ea47856504b)
![README4](https://github.com/Greyisheep/rent-predictor/assets/97015429/94b774b4-0c95-43ed-ad7d-27a3bc341260)

- Run all tests, checks and start the Uvicorn server with one command:
`tox`

**To use the project from the React frontend, navigate to the `react-frontend directory` (Run on a separate terminal, and make sure the API port is running) and follow these commands**
- Start the frontend app by running:
```bash
npm start
```
![READMEnpm](https://github.com/Greyisheep/rent-predictor/assets/97015429/37033b50-e76a-468c-a522-29340fd733db)

- To try out the frontend, open `http://localhost:3000`
To get a prediction output: Fill the form, and press the `Submit` button

**This can be used as a prediction input:**

![prediction_input](https://github.com/Greyisheep/rent-predictor/assets/97015429/5fb1b0f4-a51d-4fa6-9ee7-594c72fa3168)

**This is the result on the fastapi server:**

![READMEpred](https://github.com/Greyisheep/rent-predictor/assets/97015429/3c0f324b-f019-40df-9a98-124392e3e2b4)

## Configuration
This project is ready to use as is, but if you wish to configure it, i.e., adjust some of the variables, data source, etc., navigate to the `config.yml` file in the `house_prices_api/model_package/regression_model/`. This config file is intentionally heavily commented, to aid adjustments and understanding.

## Data
If you want your apartment to be displayed in our database, kindly fill out the following Google form:

[Google Form Link](https://forms.gle/xHqq2mQ4yi1C6sTR8)

The data for this project is available in a Google Sheets spreadsheet. The spreadsheet contains data on rent prices and apartment features for different locations in Nigeria. To access the spreadsheet, click on the following link:

[Spreadsheet Link](https://docs.google.com/spreadsheets/d/1l4Ea9PXEXv_GwcIWTORX_oK6TgZds7yTrek-fGLbJq8/edit?usp=sharing)

## Goals

The goals of this project are to:

* Create an open-source apartment search and prediction web app for students in Nigeria.
* Make it easier for students to find affordable apartments that meet their needs.
* Help students save money on rent.

## Next Steps

The next steps for this project are to:

- Set up continuous integration and deployment pipelines.
- Deploy the ML API with containers.
- Set up differential testing.
- Set up other backend protocols for user authentication, search, etc.
- Build a React-based front end for the application.
- Conduct full integration testing.
- Create tutorial videos and blogs

## Contributing

We welcome contributions to this project! To contribute, please fork the repo and create a pull request with your changes. Please make sure to test your changes and include a clear and concise description of what your changes do.

## Contact Information

**Reach me on the following platforms:**
![Gmail](https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white&link=ibeawuchiclaret%40gmail.com)
![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&link=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fclaret-ibeawuchi%2F)
![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white&link=https%3A%2F%2Ftwitter.com%2FGreyisheepai)

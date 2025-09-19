# FastAPI Filtering

The goal of this project is to implement a simplified SQL query creation system that can be used for the front end of the application.

To do this, a class system is being implemented to ensure the security of the input data using Pydantic.

The project is mainly based on the Dto/filterDtos folder; the common folder shows how the skeleton is implemented.
There is also an implementation of these concepts in the productFilterDtos file. A README.md file explains how to implement a filter on a new table and how to extend the filtering system by adding operators and functions to verify input values.

## 1 Go further

Go to ./Dto/filterDtos/README.md and understand how a filter is made.

## 2 Get Started

Un fichier sqllite est fourni avec des produits préremplis pour pouvoir tester les filtres. Pour se faire on peut lancer un serveur FastApi et tester l'ensemble des routes décrite dans ./routers/productPresentationRouter.py

1. Create a Virtual Environment
Open your terminal or command prompt and navigate to your project's directory. Then, run the following command. It will create a new folder (named myenv in this example) that holds the isolated Python environment

```bash

python3 -m venv myenv
```
2. Activate the Environment
You must activate the environment to ensure that any packages you install are added to this specific project and not to your system's global Python installation.

Linux/ macOs:

```bash

source myenv/bin/activate
```

Windows:

```bash

.\myenv\Scripts\activate
```
3. Install Dependencies from requirements.txt
Use the next command line to install the requirements listed in the file.

```bash

pip install -r requirements.txt
```

4. Start the FastAPI Server

```bash

uvicorn main:app --reload
```

5. Go to the Documentation
Access the interactive API documentation at this address:

```bash

 http://127.0.0.1:8000/docs
```

# ReadMe
This repo follows the guideline below to learn how to use FastAPI.

[Source: FastAPI Example](https://dev.to/ronnymedina/fastapi-example-9n8)


# How to run the code 

1. Download the repo
2. Create & activate virtual environment
   ```
    python -m venv .venv
    .venv\Scripts\activate.bat     #windowns cmd
    source .venv/scripts/activate  #gitbash
   ```
3. Install the package in your local environment

   ```
   pip install fastapi
   pip install uvicorn[standard]
   ```

   **OR**

    ```
    pip install -r requirements.txt
    ```


1. Run the app via command

    `uvicorn app.main:app --reload`
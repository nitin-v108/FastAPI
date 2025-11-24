# FastAPI
FastAPI code for beginner 

# Setup
python -m venv env1

# Power Shell
.\env1\Scripts\Activate.ps1 

# CMD
D:\Python\Python\fastenv\Scripts\activate.bat

# Deactivate
deactivate

pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt
pip install requests
pip install fastapi # Python Framework for backend
pip install uvicorn # Python Framework for frontend
pip install sqlalchemy # SQLAlchemy Driver
pip install psycopg2 # postgresql Driver

# Run
uvicorn main:app --reload

# Browser
http://127.0.0.1:8000/products

# Database Creds
user: postgres
pass: postgres
port: 5432

# Doc
http://127.0.0.1:8000/docs

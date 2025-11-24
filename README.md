# FastAPI
FastAPI code for beginner 

> Free Learning Tutorials : 
1. Python for Beginners (Full Course) | Programming Tutorial : https://youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&si=msTZk4A5CckyiZjU
2. Python for Beginners (Full Course) | #100DaysOfCode Programming Tutorial in Hindi : https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
3. Paid: https://www.udemy.com/course/codewithharry-python/


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

from fastapi import FastAPI, Form
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def index():
    with open("templates/login.html", "r") as f:
        login_page = f.read()
    return Response(login_page, media_type="text/html")

@app.post("/login")
def process_login_page(username : str = Form(...), password : str = Form(...)):
    return Response(f"{username} and {password}", media_type="text/html")
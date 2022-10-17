from fastapi import FastAPI, Form
from fastapi.responses import Response


app = FastAPI()

users = {
    "zh.zhumabekov@psa.kz" : {
        "name": "Zhomart",
        "password": "some_password_0",
        "balance": 100_000
    },
    "guliya@gmail.com" : {
        "name": "Guliya",
        "password": "some_password_1",
        "balance": 500_100
    }
}

@app.get("/")
def index():
    with open("templates/login.html", "r") as f:
        login_page = f.read()
    return Response(login_page, media_type="text/html")


@app.post("/login")
def process_login_page(username : str = Form(...), password : str = Form(...)):
    user = users.get(username)
    if not user or user["password"] != password:
        return Response("ИДИ НАХЕР!", media_type="text/html")

    response = Response(f"Hello { user['name'] }, your balance { user['balance'] }", media_type="text/html")
    response.set_cookie(key="username", value=username)

    return response
from typing import Optional

from fastapi import FastAPI, Form, Cookie
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
def index(username : Optional[str] = Cookie(default=None)):
    with open("templates/login.html", "r") as f:
        login_page = f.read()
    if username:
        try:
            user = users[username]
        except KeyError:
            response = Response(login_page, media_type="text/html")
            response.delete_cookie(key="username")
            return response
        return Response(f"Hello, {user['name']}", media_type="text/html")
    return Response(login_page, media_type="text/html")


@app.post("/login")
def process_login_page(username : str = Form(...), password : str = Form(...)):
    user = users.get(username)
    if not user or user["password"] != password:
        return Response("ИДИ НАХЕР!", media_type="text/html")

    response = Response(f"Hello { user['name'] }, your balance { user['balance'] }", media_type="text/html")
    response.set_cookie(key="username", value=username)

    return response 
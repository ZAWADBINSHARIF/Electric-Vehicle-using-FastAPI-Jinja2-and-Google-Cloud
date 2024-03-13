# external import
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from google.auth.transport import requests
import google.oauth2.id_token

# internal import
from config.databaseConnection import db
from models.authModels import SignUpModel, LoginModel


authRoute = APIRouter()

firebase_request_adapter = requests.Request()


@authRoute.post("/signup")
async def create_an_account(user_data: SignUpModel):
    email = user_data.email
    password = user_data.password

    # try:

    #     user = firebase.auth().create_user_with_email_and_password(
    #         email=email, password=password
    #     )

    #     return JSONResponse(
    #         content={"msg": "New user account has been created", "signup_info": user},
    #         status_code=201,
    #     )
    # except Exception as err:
    #     errors = getErrorsDict(err)

    #     raise HTTPException(
    #         status_code=errors["code"], detail={"message": errors["message"]}
    #     )


@authRoute.post("/login")
async def login(user_data: LoginModel):
    email = user_data.email
    password = user_data.password

    # try:
    #     user = firebase.auth().sign_in_with_email_and_password(
    #         email=email, password=password
    #     )

    #     return JSONResponse(
    #         content={"msg": "Login successfully", "login_info": user},
    #         status_code=200,
    #     )

    # except Exception as err:
    #     errors = getErrorsDict(err)
    #     raise HTTPException(
    #         status_code=errors["code"], detail={"error": errors["message"]}
    #     )


@authRoute.post("/refresh")
async def get_new_access_token(refreshToken: str):
    # user = firebase.auth().refresh(refreshToken)

    # return JSONResponse(
    #     content={"msg": "Login successfully", "login_info": user},
    #     status_code=200,
    # )

    pass


@authRoute.post("/logout")
async def logout():
    pass

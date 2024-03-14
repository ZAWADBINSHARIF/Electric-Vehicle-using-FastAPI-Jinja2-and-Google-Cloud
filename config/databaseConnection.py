# external import
from google.cloud import firestore
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file(
    "config/electric-vehicles-7f208-firebase-adminsdk-cwb25-0984aac04d.json"
)
db = firestore.Client(credentials=credentials)


# import firebase_admin
# from firebase_admin import credentials, auth, firestore

# cred = credentials.Certificate(
#     "config/electric-vehicles-7f208-firebase-adminsdk-cwb25-0984aac04d.json"
# )
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# external import
import pyrebase

import firebase_admin
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate(
    "config/electric-vehicles-7f208-firebase-adminsdk-cwb25-0984aac04d.json"
)
firebase_admin.initialize_app(cred)

db = firestore.client()

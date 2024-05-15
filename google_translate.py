import io
from google.cloud import translate_v2 as translate
import os
from os import environ
import json
import streamlit as st

GSC_CREDS_TYPE_PROJECT_ID = st.secrets.GSC_CREDS_TYPE_PROJECT_ID
GSC_CREDS_PRIVATE_KEY_ID = st.secrets.GSC_CREDS_PRIVATE_KEY_ID
GSC_CREDS_PRIVATE_KEY = st.secrets.GSC_CREDS_PRIVATE_KEY.replace("\\n", "\n")
GSC_CREDS_CLIENT_EMAIL = st.secrets.GSC_CREDS_CLIENT_EMAIL
GSC_CREDS_CLIENT_ID = st.secrets.GSC_CREDS_CLIENT_ID
GSC_CREDS_CLIENT_X509_CERT_URL = st.secrets.GSC_CREDS_CLIENT_X509_CERT_URL

gsc_credentials_dict = {
    "type": "service_account",
    "project_id": GSC_CREDS_TYPE_PROJECT_ID,
    "private_key_id": GSC_CREDS_PRIVATE_KEY_ID,
    "private_key": GSC_CREDS_PRIVATE_KEY,
    "client_email": GSC_CREDS_CLIENT_EMAIL,
    "client_id": GSC_CREDS_CLIENT_ID,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": GSC_CREDS_CLIENT_X509_CERT_URL,
    "universe_domain": "googleapis.com",
}

json_data = json.dumps(gsc_credentials_dict, indent=4)
json_bytes = json_data.encode("utf-8")

with open("gsc_creds.json", mode="wb") as f:
    f.write(json_bytes)


client_file = "gsc_creds.json"
environ["GOOGLE_APPLICATION_CREDENTIALS"] = client_file


def translate_english_to(text, countryISO='yo'):
    translate_client = translate.Client()
    target = countryISO
    output = translate_client.translate(text, target_language=target)["translatedText"]
    return output


# yoruba = translate_english_to("Awọn abajade wiwa ti pese awọn oye sinu itan kan ti o kan eniyan kan ti a npè ni Liz ti o yi ipadabọ ẹgbẹ rẹ pada si iṣowo aṣeyọri, Atunṣe Ajọpọ, aaye iṣẹlẹ iṣẹlẹ ti o ṣẹda ni Brooklyn, New York. Liz dojukọ lori kikọ agbegbe ẹda nipasẹ ọpọlọpọ awọn iṣẹlẹ iṣẹ ọna ati awọn ifowosowopo, gẹgẹbi Knit Club pẹlu Ella Emhoff. Iṣowo yii ti jẹ ere ti olowo, pẹlu Liz ti n mu owo-wiwọle pataki wa lati igba ti o bẹrẹ iṣowo ni Oṣu Kẹta to kọja [3]. Irin-ajo Liz ṣe afihan bi ijakadi ẹgbẹ kan ṣe le yipada si iṣẹ ala, ti n tẹnu mọ pataki ti ẹda, agbegbe, ati iṣowo ni ṣiṣe aṣeyọri [2].", 'en')
# print(yoruba)

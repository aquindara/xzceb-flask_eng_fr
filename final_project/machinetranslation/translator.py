import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('Md28QWVX4CsSO0N4BQw1j7ozeFLJCQBYEf581dd9ZYUe')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/45bf4e7d-fe95-43fb-a282-590633521580')

def englishToFrench(englishText):
    translation= language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation= language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText
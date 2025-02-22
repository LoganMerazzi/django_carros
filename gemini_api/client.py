from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Acessando uma variável de ambiente
valor = os.getenv('GEMINI_API_KEY')

def get_car_ai_bio(model, brand, year):
    car_bio_prompt = '''
    Mostre-me uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
    '''
    car_bio_prompt = car_bio_prompt.format(model,brand,year)
    client = genai.Client(api_key=valor)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=car_bio_prompt
    )
    return response.text
    

# testing
#get_car_ai_bio("T-Cross", "VW", 2025)
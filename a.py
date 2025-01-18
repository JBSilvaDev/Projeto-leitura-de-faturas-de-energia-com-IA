import dotenv
import os

# dotenv.load_dotenv('.env')

# Supondo que você tenha uma variável chamada 'MY_VARIABLE' no arquivo .env
my_variable = os.getenv('api_key')
print(my_variable)
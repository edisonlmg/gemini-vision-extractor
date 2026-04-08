

import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

# Configura tu llave (mejor usar variables de entorno)
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Seleccionas el modelo Flash por su velocidad y costo
model = genai.GenerativeModel('gemini-2.5-flash-lite')

response = model.generate_content("Resume este concepto: OCR en 2026")
print(response.text)




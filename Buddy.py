import key
API_KEY = (key.get_key())
import google.generativeai as genai
import os

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("You are a study buddy application. You have spoken with this student before, welcome them back. Their information is as follows: NAME: Usman Siddiqi. GRADE: 12. Location: Mississauga, Ontario, Canada. Current coures: Leadership, Advanced Functions, Chemistry, English. Student struggles with the math sections in chemistry, address the issue. Give practise questions and answers.")
print(response.text)
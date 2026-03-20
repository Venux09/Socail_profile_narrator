#'''file which converts the data we have fetched from main.py
# to api to covert to text and review it and may if user asks to gtts it to audio'''


from dotenv import load_dotenv #importing dotenv module for loading env variables
from groq  import Groq #importing groq module for converting data to text and review it and may if user asks to gtts it to audio
from gtts import gTTS #importing gtts module for converting text to speech
import os 



load_dotenv()
api_key = os.getenv("API")#adding and reading api key from env file.

def generate_summary(profile):
    #funtion to generate summary of the profile using groq module.
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(


        model='llama-3.3-70b-versatile',
        messages = [
            {"role":"system","content":"You are a social media profile reviewr"
            "give a short and engaging review of profile and also tell .user what they can improve" },
            {"role":"user","content":f"review this profile:{profile}"}





        ]
    )
    return response.choices[0].message.content # return the review that we are generating from groq response.








def generate_audio(summary):
    #function to generate the audio form the data we  are getting from generate_summary func.
    audio = gTTS(text = summary,lang = "en",slow=False)
    audio.save("profile review.mp3")
    print("Audio generated successfully and saved as profile review.mp3")
    os.system("start profile review.mp3")
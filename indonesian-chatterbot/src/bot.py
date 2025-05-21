from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from gtts import gTTS
import wikipedia
chatbot = ChatBot('AI Indonesia')

trainer = ChatterBotCorpusTrainer(chatbot)

training_data_path = os.path.join(os.path.dirname(__file__), 'training_data', 'indonesian_corpus.yml')

trainer.train(training_data_path)

def speak(text):
    tts = gTTS(text=text, lang='id')
    tts.save("response.mp3")
    if os.name == 'nt':
        os.system("start response.mp3")
    else:
        os.system("xdg-open response.mp3")
    os.remove("response.mp3")
def start_conversation():
    print("Halo! Saya adalah AI Indonesia. Ketik 'keluar' atau 'exit' untuk mengakhiri.")
    prefix = "apakah kamu tau tentang "
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'exit' or user_input.lower() == 'keluar':
            print("Bot: Sampai jumpa!")
            speak("Sampai jumpa!")
            break
        elif user_input.startswith(prefix):
            query = user_input[len(prefix):]
            try:
                wikipedia.set_lang("id")
                summary = wikipedia.summary(query, sentences=1)
                print(f"Bot: {summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Bot: Ada beberapa pilihan untuk '{query}': {e.options}")
                speak(f"Ada beberapa pilihan untuk '{query}': {e.options}")
            except wikipedia.exceptions.PageError:
                print(f"Bot: Maaf, saya tidak menemukan informasi tentang '{query}'.")
                speak(f"Maaf, saya tidak menemukan informasi tentang '{query}'.")
            continue
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
        speak(str(response))

if __name__ == "__main__":
    start_conversation()
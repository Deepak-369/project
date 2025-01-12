import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#it recognise what we said.
recognizer = sr.Recognizer() 
#initialise pyttsx3 to speak what you have written.
engine = pyttsx3.init()   
 
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   print(c)
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "youtube" in c.lower():
      webbrowser.open("https://www.youtube.com/")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkin.com/")
   elif "facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "github" in c.lower():
      webbrowser.open("https://github.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musicLibrary.music[song]
      webbrowser.open(link)  
   # elif c.lower().startswith("play"):
   #    song1 = c.lower().split(" ")[2]
   #    link1 = musicLibrary.music[song1]
   #    webbrowser.open(link1)  
   elif "Abhijeet full name" in c:
      speak("wakanda panda and he always gives two kg of andaa")    

if __name__ == "__main__":
   speak("initializing Jarvis.......")
   while True:
      # listen for the wake word Jarvis 
      # recognize speech using Sphinx
      try:
         with sr.Microphone() as source:       # obtain audio from the microphone
            print("listining.....")
            audio = recognizer.listen(source,timeout = 2,phrase_time_limit = 2)
         word = recognizer.recognize_google(audio)
         print("recognizing.....")
         print(word)
         if(word.lower() == "jarvis"):
            speak("yes,what can i help you")
         # Listen for command:-
            with sr.Microphone() as source:
               print("jarvis active...")
               audio = recognizer.listen(source)
               command = recognizer.recognize_google(audio)

               processCommand(command)
      except Exception as e:
         print("Error; {0}".format(e))



# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary

# # Initialize recognizer and pyttsx3 engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def process_command(command):
#     print(command)
#     command = command.lower()
#     if "open google" in command:
#         webbrowser.open("https://google.com")
#     elif "open youtube" in command:
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in command:
#         webbrowser.open("https://linkedin.com")
#     elif "open facebook" in command:
#         webbrowser.open("https://facebook.com")
#     elif "open github" in command:
#         webbrowser.open("https://github.com")
#     elif command.startswith("play"):
#         try:
#             song = command.split(" ")[1]
#             link = musicLibrary.music[song]
#             webbrowser.open(link)
#         except KeyError:
#             speak("Sorry, I could not find the song in the music library.")
#         except IndexError:
#             speak("Please specify a song to play.")
#     elif "what is abhijit full name" in command:
#         speak("Wakanda Panda and he always gives two kg of andaa")

# if __name__ == "__main__":
#     speak("Initializing Jarvis.......")
    
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening for command...")
#                 audio = recognizer.listen(source, timeout=4, phrase_time_limit=5)
#                 print(audio)
            
#             command = recognizer.recognize_google(audio)
#             print("You said:", command)
            
#             if command.lower() == "hello":
#                 speak("Yes, what can I help you with?")
#             else:
#                 process_command(command)
        
# #         except sr.UnknownValueError:
# #             print("Sorry, I did not understand the command.")
# #         except sr.RequestError:
# #             print("Sorry, there was an error with the speech recognition service.")
#         except Exception as e:
#             print(f"An error occurred: {e}")

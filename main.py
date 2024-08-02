# print "HEllo OWrld"
print("Hello World")


# a function that returns the sum of the cosine of three integer inputs
def sum_of_cosines(a, b, c):
    import math

    return math.cos(a) + math.cos(b) + math.cos(c)


# a function that returns the sum of the sine of three integer inputs
def sum_of_sines(a, b, c):
    import math

    return math.sin(a) + math.sin(b) + math.sin(c)


# a function that returns the sum of the tangent of three integer inputs
def sum_of_tangents(a, b, c):
    import math

    return math.tan(a) + math.tan(b) + math.tan(c)


# print hello in serbian
def hello_serbian():
    print("Zdravo svete")


# use the cli to prompt the user for favourite meal and city, store these in an .ini file
def favourite_meal_and_city():
    import configparser

    config = configparser.ConfigParser()
    config["favourites"] = {}
    config["favourites"]["meal"] = input("What is your favourite meal? ")
    config["favourites"]["city"] = input("What is your favourite city? ")
    with open("favourites.ini", "w") as configfile:
        config.write(configfile)


import configparser
import pyttsx3
import speech_recognition as sr
import time
import wikipedia
import pdfkit


def read_favourite_meal_and_city():
    """Read the .ini file and print the favourite meal and city."""
    config = configparser.ConfigParser()
    config.read("favourites.ini")
    print("Your favourite meal is: " + config["favourites"]["meal"])
    print("Your favourite city is: " + config["favourites"]["city"])


def chat_bot():
    """Use a chat bot to converse with a user via the CLI."""
    engine = pyttsx3.init()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something")
        audio = r.listen(source)
        print("Recognizing now")
        try:
            recognized_text = r.recognize_google(audio)
            print("You said: " + recognized_text)
            engine.say("You said: " + recognized_text)
            engine.runAndWait()
        except Exception as e:
            print("Error: " + str(e))
            engine.say("Error: " + str(e))
            engine.runAndWait()


def scrape_wikipedia():
    """Scrape a random article from Wikipedia and save it as a PDF file."""
    wikipedia.set_lang("en")
    random_page = wikipedia.random()
    page = wikipedia.page(random_page)
    pdfkit.from_url(page.url, random_page + ".pdf")


# a script to read the .ini file and print the favourite meal and city
def read_favourite_meal_and_city():
    import configparser

    config = configparser.ConfigParser()
    config.read("favourites.ini")
    print("Your favourite meal is: " + config["favourites"]["meal"])
    print("Your favourite city is: " + config["favourites"]["city"])


# a script to use a chat bot to converse with a user via the cli
def chat_bot():
    import pyttsx3
    import speech_recognition as sr
    import time

    engine = pyttsx3.init()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something")
        audio = r.listen(source)
        print("Recognizing now")
        try:
            print("You said: " + r.recognize_google(audio))
            engine.say("You said: " + r.recognize_google(audio))
            engine.runAndWait()
        except Exception as e:
            print("Error: " + str(e))
            engine.say("Error: " + str(e))
            engine.runAndWait()


# a script to scrape a random article from https://en.wikipedia.org/ and saves this as a .pdf file
def scrape_wikipedia():
    import wikipedia  # OMG! I thought, this is nonsense, there's no wikipedia module! But there is!
    import pdfkit

    wikipedia.set_lang("en")
    random_page = wikipedia.random()
    page = wikipedia.page(random_page)
    pdfkit.from_url(page.url, random_page + ".pdf")

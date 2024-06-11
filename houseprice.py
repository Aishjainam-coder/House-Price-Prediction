from tkinter import *
import pyttsx3
from PyDictionary import PyDictionary


def speak(audio):
    # Initialize pyttsx3 with sapi5
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def meaning():
    dic = PyDictionary()
    query = str(text.get())
    word = dic.meaning(query)
    if word:
        res = ""
        for state in word:
            res += str(word[state][0]) + "\n"
        spokenText.set(res)
        speak("The meaning is " + res)
    else:
        res = "Sorry, I couldn't find the meaning of the word."
        spokenText.set(res)
        speak(res)


# Create the window
wn = Tk()
wn.title("WRITE WORD WILL I GIVE MEANING")
wn.geometry("700x500")
wn.config(bg="SlateGray1")

# Create the variables to get the word and set the correct word
text = StringVar(wn)
spokenText = StringVar(wn)

# The main label
Label(
    wn,
    text="WRITE WORD WILL I  GIVE MEANING",
    bg="SlateGray1",
    fg="gray30",
    font=("Times", 20, "bold"),
).place(x=100, y=10)

# Getting the input of the word from the user
Label(
    wn,
    text="Please enter the word",
    bg="SlateGray1",
    font=("calibre", 13, "normal"),
    anchor="e",
    justify=LEFT,
).place(x=20, y=70)

Entry(wn, textvariable=text, width=35, font=("calibre", 13, "normal")).place(
    x=20, y=110
)

# Label to show the correct word
Label(
    wn,
    textvariable=spokenText,
    bg="SlateGray1",
    anchor="e",
    font=("calibre", 13, "normal"),
    justify=LEFT,
    wraplength=500,
).place(x=20, y=130)
spokenText.set("Which word do you want to find the meaning of,MAM?")
speak("Which word do you want to find the meaning of, sir or madam")

# Button to do the spell check
Button(
    wn, text="Speak Meaning", bg="SlateGray4", font=("calibre", 13), command=meaning
).place(x=230, y=350)

# Run the window until it is closed by the user
wn.mainloop()

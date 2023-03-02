import PySimpleGUI as gui


layout = [[
            gui.Text("Znaki: ", size=(10, 1)), gui.Text("0", key="znaki"),
            gui.Text("Słowa: ", size=(10, 1)), gui.Text("0" , key="slowa"),
            gui.Text("Samogłoski: ", size=(10, 1)), gui.Text("0", key="samogloski"),
            gui.Text("Linie: ", size=(10, 1)), gui.Text("0", key="linie"),
    ],
    [
            gui.Multiline(size=(70, 10), enable_events=True, key="text")
    ],
        [gui.Button("Clear", key="clear")]


    ]
def count_characters(text):
        znaki = 0
        for i in text:
                znaki += 1
        return znaki
def count_words(text):
        slowa = 0
        for i in text:
                if i == " " or i == "\n":
                        slowa += 1
        return slowa
def count_vowels(text):
        samogloski = 0
        for i in text:
                if i in "aeiouy":
                        samogloski += 1
        return samogloski

#to jest ponad programem
def count_lines(text):
        linie = 0
        for i in text:
                if i == "\n":
                        linie += 1
        return linie



window = gui.Window("Text Counter", layout)
while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
                break
        if event == "text":
                window["znaki"].update(count_characters(values["text"]))
                window["slowa"].update(count_words(values["text"]))
                window["samogloski"].update(count_vowels(values["text"]))
                window["linie"].update(count_lines(values["text"]))
                
#to w sumie też
        if event == "clear":
                window["text"].update("")
                window["znaki"].update("0")
                window["slowa"].update("0")
                window["samogloski"].update("0")
                window["linie"].update("0")
window.close()




import requests

name = input("Введите имя")

while True:
    text = input("Введите текст: ")
    requests.post("https://127.0.0.1:5000/send",
    json={'name':'Alice', 'text':'text'}
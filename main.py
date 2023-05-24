import requests
import telebot
from bs4 import BeautifulSoup
import random
import time

token = "6161725848:AAHv7-TMi6dXhA-4Cu2lQOkljAHmKiFZbGU"
TG_CHAT_ID = "184934817"
url = 'https://datki.net/komplimenti/zhene/'

bot = telebot.TeleBot(token)



def parse_words_from_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    words = []
    for p in soup.find_all('p'):  # Replace 'p' with the correct element or class
        words.append(p.text)
    return words

def choose():
    words = parse_words_from_site(url)
    words = [sentence for sentence in words if any(word.isalpha() for word in sentence.split())]
    unique_sentences = list(set(words))
    unique_sentences = [sentence for sentence in unique_sentences if "Авторские комплименты любимой" not in sentence]

    while True:
        if not unique_sentences:
            # If all unique sentences have been sent, fetch new ones
            unique_sentences = list(set(words))
            unique_sentences = [sentence for sentence in unique_sentences if "Авторские комплименты любимой" not in sentence]

        choice = random.choice(unique_sentences)
        bot.send_message(TG_CHAT_ID, choice)
        unique_sentences.remove(choice)
        time.sleep(1)

if __name__ == '__main__':
    choose()
    bot.polling()

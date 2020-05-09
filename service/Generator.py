import random
import requests
from bs4 import BeautifulSoup
from random_words import RandomWords

sentences_counter = 30


class Generator:
    def __init__(self):
        random_words = RandomWords()
        self.WORDS = random_words.random_words(count=400)

    def get_random_word(self):
        return random.choice(self.WORDS)

    # Web scrapping to get random sentences
    def get_random_sentences(self):
        sentences = list()
        for _ in range(round(sentences_counter/30)):
            url = 'http://www.englishinuse.net'
            source = requests.get(url)

            if source.ok:
                soup = BeautifulSoup(source.text, 'html.parser')
                body = soup.find_all('tr', class_='font1')
                for box in body:
                    sentence = " " + box.find_all('td')[1].text + "\n"
                    if len(sentence) <= 80:
                        sentences.append(sentence)
            else:
                raise ConnectionError("Could not connect to sentences generator")

        return sentences

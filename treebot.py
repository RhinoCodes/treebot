import requests

words = request.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').text
words = eval(words)
for k in words.keys():
  requests.get(f'https://ecosia.org/search?q={k}')

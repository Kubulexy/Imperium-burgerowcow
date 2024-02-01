meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "Odpowiedź na żart",
            "SHEESH": "Lekka dezaprobata",
            "CREEPY": "Straszny,złowieszczy",
            "AGGRO": "Stać się agresywnym/zły"
            }

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Słowo nie zostało znalezione")

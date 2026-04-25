n = int(input("Количество видеокарт: "))
cards = []

for i in range(1, n + 1):
    card = int(input(f"{i} Видеокарта: "))
    cards.append(card)

max_card = cards[0]
for card in cards:
    if card > max_card:
        max_card = card

new_cards = []
for card in cards:
    if card != max_card:
        new_cards.append(card)

print(f"Старый список видеокарт: [ {' '.join(str(c) for c in cards)} ]")
print(f"Новый список видеокарт: [ {' '.join(str(c) for c in new_cards)} ]")

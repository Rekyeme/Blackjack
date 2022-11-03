import random

player_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
npc_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


def mix(player_deck, npc_deck):
    random.shuffle(player_deck)
    random.shuffle(npc_deck)


def compare(hand):
    soma = 0
    for card in hand:
        if card == "J":
            soma = soma + 11
        elif card == "Q":
            soma = soma + 12
        elif card == "K":
            soma = soma + 13
        elif card == "A":
            soma = soma + 14
        else:
            soma = soma + card
    return soma

mix(player_deck, npc_deck)


def show_d(player_deck, npc_deck):
    print("Deck da Casa: " + str(npc_deck))
    print("Deck do Player: " + str(player_deck))


show_d(player_deck, npc_deck)


def fish(deck):
    myhand = [deck[-1], deck[-2]]
    return myhand


npchand = fish(npc_deck)
playerhand = fish(player_deck)


print("Cartas da Casa: " + str(npchand))
print("Cartas do Player: " + str(playerhand))
print("A soma das cartas da Casa: " + str(compare(npchand)))
print("A soma das cartas do Player: "+ str(compare(playerhand)))

if compare(npchand) > compare(playerhand):
    print("Vitória da Casa!")
else:
    print("Vitória do Player!")

commmand = ""
while (commmand != "No"):
    print("Continuar? Yes/No")
    commmand = input()
    if commmand == "Yes":
        random.shuffle(npchand)
        random.shuffle(playerhand)
        print(npchand,playerhand)






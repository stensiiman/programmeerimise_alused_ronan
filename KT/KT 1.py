"""Kt 1.

1.       Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda kasutaja vastas õigesti."""


def ask_number():
    a = int(input("Sisesta esimene arv: "))
    b = int(input("Sisesta teine arv: "))
    c = int(input("Sisesta kolmas arv: "))
    smallest = min(a, b, c)
    limit = smallest * 2

    correct_answers = 0
    current = 1
    while current <= limit:
        answer = int(input(f"Mis on arvu {current} ruut? "))
        if answer == current ** 2:
            print ("Õige vastus!")
            correct_answers += 1
        else:
            print("Valesti!")
        current += 1
    print(f"Sa vastasid õigesti {correct_answers} korda.")


if __name__ == "__main__":
    ask_number()
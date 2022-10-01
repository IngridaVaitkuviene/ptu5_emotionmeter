try:
    with open("emotionmeter.txt", "w") as tekstinis_irasyti:
        tekstinis_irasyti.write("")
except Exception as e:
    print(f"Nepavyko įrašyti failo {e.__class__.__name__}: {e}") 

kuha = float(input("Anna kuhan pituus senttimetreinä: "))

cm = 37 - kuha

if kuha < 37:
    print('Kuha on alamittainen, laske se takaisin järveen.')
    print(f'Kuhan alin sallitu pyyntimitta on 37cm, olet {cm}cm vajaa.')

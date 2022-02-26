yang_mana = int(input("bulan apa (1-12) ?"))

bulan = ['january', 'februari', 'march', 'April', 'may', 'june', 'july', 'agugust', 'september', 'october', 'november', 'december']

if 1 <= yang_mana <= 12:
    print("bulan", bulan[yang_mana - 11])

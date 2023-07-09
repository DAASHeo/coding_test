
array = [500, 100, 50, 10]
def change_money(change):
    for coin in array:
        count = 0
        count += change // coin
        change %= coin
        print("화폐 종류:",coin,"반환 갯수",count)
    return 0


change_money(1260)
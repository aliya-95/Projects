money = 100000
deposit = [5600, 5900, 4280, 4000]
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money= int(input("Введите сумму, которую планируете положить под проценты:"))
tkb = money * (per_cent.get('ТКБ')/100)
skb = money * (per_cent.get('СКБ')/100)
vtb = money * (per_cent.get('ВТБ')/100)
sber = money * (per_cent.get('СБЕР')/100)
deposit = [round(tkb), round(skb), round(vtb), round(sber)]
print("Накопленные средства за год вклада в каждом из банков =",deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))
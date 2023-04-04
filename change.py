#자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보세요
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원 짜리 동전을 사용할 수 있다.
# 물건 값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면
# 거스름돈을 계싼하여서 동전으로 반환한다

price = int(input("물건 값을 입력하세요: "))

paper_1000 = int(input("가지고 계신 1000원짜리 지폐의 개수를 입력해주세요: "))
coin_500 = int(input("가지고 계신 500원짜리 동전의 개수를 입력해주세요: "))
coin_100 = int(input("가지고 계신 100원짜리 동전의 개수를 입력해주세요: "))

change = 1000*paper_1000 + 500*coin_500 + 100*coin_100 - price

npaper_1000 = change // 1000
change = change % 1000

ncoin_500 = change // 500
change = change % 500

ncoin_100 = change //100
change = change % 100

print("거스름돈??")
print("1000원=", npaper_1000, "500원=", ncoin_500, "100원=", ncoin_100)


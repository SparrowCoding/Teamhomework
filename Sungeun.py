S = input("이름을 입력하세요 :")
print("그래 과제 켰구나 "+ S+"아")
a = int(input("오늘 날짜를 입력하시오 ex 5월 30일= 530 =="))

if a <= 522:
    print("적당한 시기에 과제를 마쳤네용")
elif a > 522 and a < 526:
    print("좀 늦게 과제를 마쳤네요 다음부턴 서둘러주세요")
else:
    print("과제가 너무 늦게 끝났는데용")

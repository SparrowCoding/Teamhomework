기업들 = []
총_수익들 = []
총_비용들 = []
순이익들 = []

기업_수 = int(input("기업의 수를 입력하세요: "))

for i in range(기업_수):
    기업명 = input(f"{i+1}번째 기업의 이름을 입력하세요: ")
    총_수익 = float(input(f"{기업명}의 총 수익을 입력하세요: "))
    총_비용 = float(input(f"{기업명}의 총 비용을 입력하세요: "))
    
    기업들.append(기업명)
    총_수익들.append(총_수익)
    총_비용들.append(총_비용)

for i in range(기업_수):
    순이익 = 총_수익들[i] - 총_비용들[i]
    순이익들.append((기업들[i], 순이익))

for i in range(len(순이익들)):
    for j in range(i + 1, len(순이익들)):
        if 순이익들[i][1] < 순이익들[j][1]:
            순이익들[i], 순이익들[j] = 순이익들[j], 순이익들[i]

print("기업별 순이익 :")
for 기업명, 순이익 in 순이익들:
    print(f"{기업명}: {순이익}")
   

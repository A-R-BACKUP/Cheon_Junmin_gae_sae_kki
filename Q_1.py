# 1. 양의 정수 리스트를 입력 받아서 짝수만 출력하는 함수를 작성하고, 그 함수를 호출하여 결과를 확인하시오.

Evenlst = []

Numlst = list(map(int, input("양의 정수 리스트를 입력하시오. \n").split()))

print("입력 받은 리스트는 아래와 같습니다.")
print(Numlst)
print("\n")

def dispEvenNum(Numlst):
    for i in Numlst:
        if i % 2 == 0:
            Evenlst.append(i)
    print(Evenlst)

print("리스트 중에 짝수는...")
dispEvenNum(Numlst)
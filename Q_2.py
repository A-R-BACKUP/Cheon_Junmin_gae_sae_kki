# 2. 양의 정수 리스트를 입력 받아서 짝수만 추출하여 반환하는 함수를 작성하고, 그 함수를 호출하여 결과를 확인하시옿.

Evenlst = []

Numlst = list(map(int, input("양의 정수 리스트를 입력하시오. \n").split()))

print("입력 받은 리스트는 아래와 같습니다.")
print(Numlst)
print("\n")

def detectEvenNum(Numlst):
    for i in Numlst:
        if i % 2 == 0:
            Evenlst.append(i)
    return Evenlst


print("반환된 짝수 리스트는...")
x = detectEvenNum(Numlst)
print(x)

# 1번 코드에 살짝 변형만 해서 return 받아서 출력 하라는건지 잘 몰겠으나 이게 반환 정공법이긴함...

# 반환 받은 값을 변수에 넘겨주고 프린트 한다는 점을 뺴면 1번과 다를게 없는 문제라서 애매미묘...

# 틀렸다카믄 천준민 탓.
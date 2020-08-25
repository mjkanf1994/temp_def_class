# main py 에서 calulation.py 함수 불러오기

import calulation as cal
a=3
b=4

def main():
    print("안녕하세요, main()입니다")
    print("a+b=",cal.subtract(a,b))
    print("a-b",cal.plus(a,b))


if __name__=="__main__":
    main()


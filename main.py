# main py 에서 calulation.py 함수 불러오기

#import calulation as cal

from arithmetic import plus
from arithmetic import subtract
from dataprocessing import processing
from dataprocessing import importData

a = 3
b = 4

def main():
    print("~~ 사칙 연산을 시작합니다 ~~ ")
    print("a+b",plus.add(a,b))
    print("a-b",subtract.minus(a,b))
    print("~~ 사칙 연산을 종료합니다 ~~ ")

## 데이터 전처리 시작
data = importData.readData()
processing.process_data(data)

if __name__=="__main__":
    main()
import os
import sys
 
 #원하는 곳에 만들고 싶을 때 경로 지정하는 방법
 #ex) C:/Users/사용자명/Desktop/test.txt 이렇게 하면 바탕화면에 저장됨
sys.stdout = open('test.txt', mode='w', encoding='utf-8')

def search(dir):
        files = os.listdir(dir)
        for file in files:
                print(file)

#추출 원하는 곳 경로 지정
print(search("./"))
#1예제1) 리턴문도 없고 인자도 없는 함수
def printHello():
    print("Hello, cutiepie")

printHello()

#2예제2) 리턴문이 없고 인자는 있는 함ㄱ수
def printHi(name):
    print("Hi",name)

#name=input("당신의 이름은? ")
#printHi(name)

#3예제3) 리턴문이 있는 함수
def printWelcome(user):
    word="Welcome, "+str(user)
    return word

user=input("당신의 이름은?" )#input을 받을때 부터 문자열이라서 넵 
#print(printWelcome(user))

#4예제4) 세개의 값을 동시에 리턴하는 함수
def func_mul(x):
    y1=x*10
    y2=x*20
    y3=x*30
    #return y1, y2, y3
    return [y1, y2, y3]

#a,b,c=func_mul(10)
#print(a,b,c)

# a=func_mul(10)
# print(type(a),a)

 #문자열안에 우리가 우너하는 값을 쉽게 삽입해보자 
 #파이썬에는 여러문자열 포매팅방법이 있습니다
 #여기서는 format함수를 사용한 포매팅만 알고 넘어 갑시다
 #더자세한 포매팅방법을 알고싶다면 https://wikidocs.net/13참고


 #1_문자열에 숫자를 바로 대입하기
 print("저는 덕성멋사{}기 입니다.".format(9))



 



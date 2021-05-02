def is_prime(num):
# 들어온 num이 소수이면 True를 반환하고
# 소수가 아니면 False를 반환하는 함수
  
  if(num<2):
    return False
  for i in range(2,num):
    if(num%i==0):
      return False
  return True

# print(is_prime(4))
# print(is_prime(5))

#num = int(input(" 들어온 숫자 : "))

#for i in range(num+1):  
#  if(is_prime(i)):
#    print(i)

def calculate_prime_number(length):
    # 소수를 2부터 length개만큼 담고 있는 배열을 반환하는 함수
    # 예를 들어 length에 2를 입력하면 [2, 3]을 반환하고
    # length에 5를 입력하면 [2, 3, 5, 7, 11]을 반환해야 함
    # is_prime 함수를 사용하면 편하게 코딩할 수 있음

  li = []

  y = 1

  while(True):
    y += 1
    if(is_prime(y)==True):
      li.append(y)

    if length == len(li):
      break
  return li
      
n = int(input('소수 몇 개를 알고 싶니? 숫자를 입력하렴 : '))
print(calculate_prime_number(n))    
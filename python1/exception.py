#예외처리
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    #num1 = int(input("첫번째 숫자를 입력하세요 : "))
    #num2 = int(input("두번째 숫자를 입력하세요 : "))
    #print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")    
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
    
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")    
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")    
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")    
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

class BigNumberError(Exception):
    def __init__(self, msg):
        return self.msg
    

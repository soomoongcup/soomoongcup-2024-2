import oj

class LoanProblem(oj.Problem):
   def __answer__(self, stdin, stdout):
       def custom_round(x):
           # 0.5 이상일 경우 올림, 미만일 경우 내림
           if x - int(x) >= 0.5:
               return int(x) + 1
           return int(x)
       
       T = int(stdin.readline())
       for _ in range(T):
           R, B, M = map(float, stdin.readline().split())
           months = 0
           debt = B
           initial_debt = B
           
           while debt > 0:
               months += 1
               if months > 1200:
                   stdout.write("impossible\n")
                   break
               
               # 매월 초 이자 계산 (원 단위 반올림)
               interest = custom_round(debt * R / 100)
               debt += interest
               
               # 매월 말 상환
               debt -= M
               debt = custom_round(debt)
               
               if debt >= initial_debt:
                   stdout.write("impossible\n")
                   break
           else:
               stdout.write(f"{months}\n")

problem = LoanProblem()

# 1. 기본 테스트 케이스
with problem.testcase('1') as sys:
   sys.stdin.write("11\n")
   sys.stdin.write("2.00 100.00 105.50\n")
   sys.stdin.write("2.00 100.00 102.00\n")
   sys.stdin.write("2.00 100.00 100.00\n")
   sys.stdin.write("2.00 100.00 4.00\n")
   sys.stdin.write("2.00 100.00 3.00\n")
   sys.stdin.write("2.00 100.00 1.00\n")
   sys.stdin.write("2.00 100.00 2.00\n")
   sys.stdin.write("9.56 5462.50 522.22\n")
   sys.stdin.write("12.50 29876.44 33610.99\n")
   sys.stdin.write("5.50 1.00 1.05\n")
   sys.stdin.write("14.78 40181.09 46119.86\n")

# 2. 소수점 관련 엣지 케이스
with problem.testcase('2') as sys:
   sys.stdin.write("10\n")
   # 정확히 0.5 케이스들
   sys.stdin.write("2.50 100.00 10.50\n")    
   sys.stdin.write("3.50 200.00 20.50\n")    
   # 0.5 근처 케이스들
   sys.stdin.write("2.49 100.00 10.50\n")    
   sys.stdin.write("2.51 100.00 10.50\n")    
   # 복잡한 소수점 케이스
   sys.stdin.write("3.33 150.33 15.33\n")    
   sys.stdin.write("4.67 167.67 16.76\n")    
   # 매우 작은 차이 케이스
   sys.stdin.write("1.001 100.00 10.00\n")   
   sys.stdin.write("1.999 100.00 10.00\n")   
   # 누적 오차 테스트
   sys.stdin.write("2.505 1000.00 100.00\n")
   sys.stdin.write("4.995 2000.00 200.00\n") 

# 3. 이자와 상환금이 근접
with problem.testcase('3') as sys:
    sys.stdin.write("5\n")
    sys.stdin.write("5.00 100.00 5.50\n")    
    sys.stdin.write("5.00 100.00 6.00\n")    
    sys.stdin.write("5.00 1000.00 55.00\n")  
    sys.stdin.write("2.50 1000.00 15.00\n")  
    sys.stdin.write("3.00 500.00 20.00\n")   

# 1. 0값 테스트 케이스
with problem.testcase('4') as sys:
    sys.stdin.write("10\n")
    sys.stdin.write("0.00 1000.00 100.00\n")    # 무이자 대출
    sys.stdin.write("5.00 0.00 100.00\n")       # 무대출
    sys.stdin.write("5.00 1000.00 0.00\n")      # 무월급
    sys.stdin.write("0.00 0.00 0.00\n")         # 모두 0
    sys.stdin.write("0.00 100.00 0.00\n")       # 무이자 + 무월급
    sys.stdin.write("0.00 0.00 100.00\n")       # 무이자 + 무대출
    sys.stdin.write("5.00 0.00 0.00\n")         # 이자만 있음
    sys.stdin.write("0.01 1000.00 1.00\n")      # 최소 이자 + 최소 월급
    sys.stdin.write("0.00 1000.00 1000.00\n")   # 무이자 + 한번에 상환
    sys.stdin.write("0.00 1000.00 1.00\n")      # 무이자 + 천천히 상환

with problem.testcase('5') as sys:
    sys.stdin.write("10\n")
    sys.stdin.write("50.00 50000.00 50000.00\n")  # 모두 최대값
    sys.stdin.write("0.01 0.01 0.01\n")           # 모두 최소값(0제외)
    sys.stdin.write("50.00 0.01 50000.00\n")      # 최대 이자 + 최소 대출
    sys.stdin.write("0.01 50000.00 0.01\n")       # 최소 이자 + 최대 대출
    sys.stdin.write("25.00 25000.00 25000.00\n")  # 중간값
    sys.stdin.write("49.99 49999.99 49999.99\n")  # 최대값 바로 전
    sys.stdin.write("0.02 0.02 0.02\n")           # 최소값 바로 다음
    sys.stdin.write("50.00 50000.00 0.01\n")      # 최대값 + 최소 상환
    sys.stdin.write("0.01 50000.00 50000.00\n")   # 최소 이자 + 최대값들
    sys.stdin.write("50.00 0.01 0.01\n")          # 최대 이자 + 최소값들


with problem.testcase('6') as sys:
    sys.stdin.write("5\n")
    sys.stdin.write("0.01 1200.00 1.00\n")    
    sys.stdin.write("0.01 2400.00 2.00\n")    
    sys.stdin.write("0.02 1200.00 1.10\n")    
    sys.stdin.write("0.01 1000.00 0.85\n")    
    sys.stdin.write("0.01 5000.00 4.20\n")    

# 효율성 테스트 (T=1000)
with problem.testcase('7') as sys:
    sys.stdin.write("1000\n")
    for i in range(1000):
        # 다양한 케이스 생성
        R = round(min(50.00, i * 0.05), 2)        # 0.00 ~ 50.00
        B = round(min(50000.00, i * 50), 2)       # 0.00 ~ 50000.00
        M = round(min(50000.00, (i + 1) * 50), 2) # 50.00 ~ 50000.00
        sys.stdin.write(f"{R:.2f} {B:.2f} {M:.2f}\n")

problem.save('loan_problem_tests.zip')
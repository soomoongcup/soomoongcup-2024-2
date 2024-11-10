## 문제
고등학생 수뭉이는 평소 영어 수업 시간마다 교과서에 낙서를 하며 시간을 보낸다.
그걸 안 좋게 본 수뭉이의 담임은 수뭉이한테 책을 읽어서 낙서를 세어 오라고 한다.

책 속에서 낙서와 영어 글자의 분별해서 낙서의 숫자를 셀 수 있는 프로그램을 만들어보자!


## 입력
첫 번째 줄에 $100$보다 작거나 같은 자연수 $N$이 주어진다.
두 번째 줄에 길이가 N인 문자열 S이 주어진다.
- S는 교과서에 적힌 내용을 의미한다.
- S는 ASCII 코드 중에서만 주어진다.
- 낙서는 아스키 코드 상에서 영문자를 제외한 것을 말하며, 공백 문자는 낙서에 포함 되지 않는다.


## 출력
낙서의 수를 출력한다.


## 예제 입력 1

```text
14
Hello, World! 
```

## 예제 출력 1

```text
2
```

## 예제 입력 2

```text
174
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
```

## 예제 출력 2

```text
30
```

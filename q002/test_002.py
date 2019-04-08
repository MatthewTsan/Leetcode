import q002 as code

if __name__ == '__main__':
    for i in range(0, 10000):
        for j in range(0, 10000):
            number1 = code.num2Forms().num2ListNode(i)
            number2 = code.num2Forms().num2ListNode(j)
            result = code.Solution().addTwoNumbers(number1, number2)
            if i % 50 == 0 and j == 0:
                print(i, " ", j, " ", i+j, " ", result)
            if result != code.num2Forms.num2List(i+j) :
                print("%d + %d, expect: %d" % (i, j, i+j))
                print("get:", result)
                exit()
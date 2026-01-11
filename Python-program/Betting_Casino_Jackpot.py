#wap to make a casino jackpot.
import random
print("======WELCOME TO CASINO======")
print("Instructions:")
print("1.If two numbers are same then the amount will be doubled.")
print("2.If three numbers are same then the amount will be 5 times.")
print("3.If none of the numbers are same then you will lose your bet amount.")
print("4.If your Bet is zero then the game will end.")
print("--==play at your own risk==--")
balance=int(input("choose your balance: "))
initial_balance=balance
while True:
    if balance>0:
        Bet=int(input("How much do you bet?"))
        if Bet>balance:
            print("Aukaat me reh!")
            continue
        elif Bet==0:
            if balance>=initial_balance*2:
                print("Malamal ho gaye Miya!")
                break
            elif balance>=initial_balance*5:
                print("paisa hi paisa hai Miya!")
                break
            elif balance<initial_balance:
                print("Nuksaan ho gaya Miya!")
                break
        else:
            balance-=Bet
            print("!!Spinning!!")
            num1=random.randint(1,10)
            num2=random.randint(1,10)
            num3=random.randint(1,10)
            print("     <Result>")
            print(f"| [{num1}] | [{num2}] | [{num3}] |")
            if num1==num2==num3:
                balance=balance*5
                print("+-+-+-Jackpot! You won 5 times your bet!+-+-+-")
            elif num1==num2 or num2==num3 or num1==num3:
                balance=balance*2
                print("+-+-+-You won double your bet!+-+-+-")
            print("Total amount:",balance)
    else:
        print("Lut gaye Miya!")
        break

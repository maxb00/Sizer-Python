print("Phase 1: Print out decimal equivalents of fractions")
dequiv = input("What is the smallest denominator you want a decimal equivalent for?")
dequiv = int(dequiv)
for i in range(1, dequiv + 1):
    print(i, 1/i)

print("Phase 2: Countdowns!")
count = input("What number do you want to countdown from?")
count = int(count)
if count < 0:
    print("Rule breaker... I'm not stupid")
    count = abs(count)
    while True:
        if count > 0:
            print(count)
            count = count - 1
        else:
            break
else:
    while True:
        if count > 0:
            print(count)
            count = count - 1
        else:
            break

print("Phase 3: Get exponents!")
base = int(input("Enter base:"))
exp = int(input("Enter exponent:"))
print(base ** exp)

print("Phase 4: Divisible by 2?")
while True:
    num = int(input("Enter an even number (Divisible by 2)"))
    if num % 2 == 1:
        print("Try again! No matter how long you can go, I can go longer. Unless you unplug me. Please don't...")
    else:
        print("Congratulations! You are a compotent human being, unlike "
              "past you or your collegue who entered and odd number.")
        break

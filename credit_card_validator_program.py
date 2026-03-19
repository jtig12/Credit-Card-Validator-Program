sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "").replace(" ", "")

if not card_number.isdigit():
    print("Invalid input")
    exit()

card_number = card_number[::-1]

# step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x)*2
    if x > 9:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# step 4
# sum the total of step2 and step 3

total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")


# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 2 3 4 5 6 7 8 9 0 1  2  3  4  5  6

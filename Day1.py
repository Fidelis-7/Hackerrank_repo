# if __name__ == '__main__':
#     print("hello world")

# number = int(input("Enter a number: "))
# len_of_digits = 10
# if len(number) == len_of_digits:
#     if number == 7 or number == 8 or number == 9:
#         print("YES")
#     else:
#         print("NO")
# number_of_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]



str = ["9587456281", "1252478965"]
for i in str:
    if len(i) == 10:
        if i[0] == "7" or i[0] == "8" or i[0] == "9":
            print("YES")
        else:
            print("NO")
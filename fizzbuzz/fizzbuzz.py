def fizzbuzz (value):
    result = "";
    if value % 3 == 0:
        result = "fizz"
    if value % 5 == 0:
        result += "buzz"
    if result == "":
        result = str(value)
    return result


if __name__ == "__main__":
    for i in range(101):
        print (fizzbuzz(i))

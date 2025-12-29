#function to convert a hexadecimal string (up to three characters long) to a decimal integer

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
  hexNum = hexNum.upper()

  for num in hexNum:
    if num in hexNumbers:
      continue
    else:
      return None

  if len(hexNum) <= 0 or len(hexNum) > 3:
    return None

  decimal_value = 0
  power = 0

  for i in range(len(hexNum)-1, -1, -1):
    digit = hexNum[i]
    decimal_value = decimal_value + hexNumbers[digit] * (16 ** power)
    power += 1

  return decimal_value

# Usage of hexToDec function
if __name__ == "__main__":
    hex_value = input("Enter a hexadecimal number (up to 3 characters): ")
    result = hexToDec(hex_value)
    if result is not None:
        print(f"The decimal value of {hex_value} is {result}.")
    else:
        print("Invalid hexadecimal input.")
#some shit
def Distance_from_zero(a_number):
  if a_number.isdigit():
    if len(a_number.split(".")) > 1:
        return abs(float(a_number))
    return abs(int(a_number))

  return "nope"

number = input("enter a number:")

print(Distance_from_zero(number))

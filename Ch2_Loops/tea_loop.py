for x in range(4):
    y = 115 - x
    print(y)
    if y <= 112:
        break


temp = 115
temp_target = 112
ice_chip = 1

while temp > temp_target:
    print(temp)
    temp -= ice_chip

print("Congratulations, your tea is now", temp, "degrees!")
print("Your target temperature was", temp_target, "degrees.")

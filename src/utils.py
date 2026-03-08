a=44
b=23
print(a+b)
print(a-b)




# Simple Distance Converter

print("Distance Converter")
print("1. Kilometer to Meter")
print("2. Meter to Kilometer")
print("3. Kilometer to Mile")

choice = int(input("Choose an option (1-3): "))
value = float(input("Enter the distance: "))

if choice == 1:
    result = value * 1000
    print("Result:", result, "meters")

elif choice == 2:
    result = value / 1000
    print("Result:", result, "kilometers")

elif choice == 3:
    result = value * 0.621371
    print("Result:", result, "miles")

else:
    print("Invalid choice")
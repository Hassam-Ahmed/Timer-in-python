import time

print("Your time starts now:")
#"time.sleep() is being used when you want to take a break"
#"before the line of code executes"
time.sleep(1)
#"Example: After the output of ("Your time starts now")"
#"Program will start counting after 1 second break because of" time.sleep(1)

for seconds in range(10,0,-1):
#"if you want program to count from 1 to 10 : change the range to :"
# range(0,11,1):
#"remember last number is not included."
#"if you want to count from 0 to 10 : you must write :" range(11,0,-1)
    print(seconds)
    time.sleep(1)
time.sleep(1)
print("Your Times up")

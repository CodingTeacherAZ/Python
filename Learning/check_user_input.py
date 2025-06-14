##yes_list = ['Y', 'y','YES','yes']
##answer = input("Do you want to play a game? ")
##if answer in yes_list:
##    print("Let's go")
##else:
##    print("goodbye")

answer = input("Do you want to play a game? y/n  ").lower() in ['yes','y']
print(answer)
if answer:
    print("Howdy doody")
else:
    print("go home")

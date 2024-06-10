
# command=input('enter the command')
# while command != 'quit':
#     if command == 'start':
#         print('car started.....ready to go')
#     elif command == 'stop':
#         print('car stopped')
#     elif command == 'help':
#         print("""
#               start-to start the car 
#               stop-to stop the car 
#                quit- to quit the game 
#                """)
#     else:
#         print('maa chuda')


command = input('Enter the command: ').lower()
startflag=False
stopflag=False

while 1:
    if command == 'start':
        if startflag == True:
            print('the car is already started')
        else:
            startflag=True
            print('Car started...ready to go.')
    elif command == 'stop':
        if stopflag == True:
            print('the car is already at hault')
        else:
            stopflag=True
            print('Car stopped.')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
    command = input('Enter the command: ').lower()

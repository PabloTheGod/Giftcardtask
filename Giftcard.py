giftcard = input("what is your name for the gift card ")
giftcard = 50
game = 35
answer = input("you wanna buy some games yes or no ")
if answer == "no":
    print("ok goodbye")
else:
    print("ok then you wanna get a game for 35 dollars")
    order_1 = giftcard - game
    print("ok the money left on your gift is: {}".format(order_1))
    

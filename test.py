sigma = True
humble = False
if sigma == True:
    print("You are a Sigma")
    que = input("Are you a Sigma? ")
    if que == "No":
        humble = True
    elif que == "Yes":
        humble = False
    elif que != "Yes" or "No":
        print("either you didn't answer with Yes or No or you didn't use a capital Which is not Sigma")
        humble = False
if humble == True:
    print("You are humble which makes you a Sigma")
elif humble == False:
    print("You are NOT humble or you suck at typing so you art NOT a Sigma")
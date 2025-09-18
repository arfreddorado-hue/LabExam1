mobileNum = str(input("Enter mobile number: "))

# Check if the mobile number is valid
if len(mobileNum) != 11:
    print("Invalid number")
elif mobileNum[0:2] != "09":
    print("Invalid number")

# Check the network based on the mobile number prefix
elif mobileNum[0:4] == "0913" or mobileNum[0:4] == "0914" or mobileNum[0:4] == "0920" or mobileNum[0:4] == "0921" or mobileNum[0:4] == "0922" or mobileNum[0:4] == "0923" or mobileNum[0:4] == "0924" or mobileNum[0:4] == "0925" or mobileNum[0:4] == "0926" or mobileNum[0:4] == "0927" or mobileNum[0:4] == "0928" or mobileNum[0:4] == "0929" or mobileNum[0:4] == "0930":
    print("The network of the mobile # is Smart")
elif mobileNum[0:4] == "0909" or mobileNum[0:4] == "0910" or mobileNum[0:4] == "0911" or mobileNum[0:4] == "0912" or mobileNum[0:4] == "0913" or mobileNum[0:4] == "0914" or mobileNum[0:4] == "0915" or mobileNum[0:4] == "0916" or mobileNum[0:4] == "0917" or mobileNum[0:4] == "0918" or mobileNum[0:4] == "0919":
    print("The network of the mobile # is TNT")
elif mobileNum[0:4] == "0922" or mobileNum[0:4] == "0923" or mobileNum[0:4] == "0932" or mobileNum[0:4] == "0933":
    print("The network of the mobile # is Sun")
elif mobileNum[0:4] == "0915" or mobileNum[0:4] == "0916" or mobileNum[0:4] == "0917" or mobileNum[0:4] == "0925" or mobileNum[0:4] == "0926" or mobileNum[0:4] == "0927":
    print("The network of the mobile # is Globe")
elif mobileNum[0:4] == "0903" or mobileNum[0:4] == "0904" or mobileNum[0:4] == "0905" or mobileNum[0:4] == "0906" or mobileNum[0:4] == "0907":
    print("The network of the mobile # is TM")
elif mobileNum[0:4] == "0901" or mobileNum[0:4] == "0902" or mobileNum[0:4] == "0904":
    print("The network of the mobile # is Red")
elif mobileNum[0:4] == "0991" or mobileNum[0:4] == "0992" or mobileNum[0:4] == "0993" or mobileNum[0:4] == "0994" or mobileNum[0:4] == "0995" or mobileNum[0:4] == "0996" or mobileNum[0:4] == "0997" or mobileNum[0:4] == "0998":
    print("The network of the mobile # is Dito")
else:
    print("Unknown Network")

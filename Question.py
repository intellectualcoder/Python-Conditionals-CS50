response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
response = response.strip()
response = response.lower()

if response == "fifty two":
    print("Yes")
elif response == "fifty-two":
    print("Yes")
elif response == "52":
    print("Yes")
else:
    print("No")


def main():

    bankergreeting = input("Banker greeting: ")
    bankergreeting = bankergreeting.strip().lower()

    if bankergreeting.startswith("hello"):
        print("$0")
    elif bankergreeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()

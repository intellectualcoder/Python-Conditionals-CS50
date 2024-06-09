def main():
    question = input("What time is it? ")
    time = convert(question)

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print("No food")

def convert(time):
    hours, minutes = time.split(":")
    shorthour = float(minutes) / 60
    return float(hours) + shorthour

if __name__ == "__main__":
    main()

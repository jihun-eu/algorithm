def main():
    ccc_day = 218
    month = input()
    day = input()
    if len(day) == 1:
        day = "0" + day
    current_date = int(month + day)

    if current_date == ccc_day:
        print("Special")
    elif current_date < ccc_day:
        print("Before")
    else:
        print("After")


if __name__ == "__main__":
    main()

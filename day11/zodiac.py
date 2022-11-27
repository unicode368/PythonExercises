predictions = {"Aries": ["it's your lucky day!", "rose"],
               "Taurus": ["what a wonderful day to go outside and meet some new people!", "star"],
               "Gemini": ["try something new!", "ball"],
               "Cancer": ["woah! careful on the roads!", "umbrella"],
               "Sagittarius": ["you'll be surprised!", "keychain"],
               "Aquarius": ["take your time todsy, don't rush", "cup"],
               "Pisces": ["don't miss a chance!", "ticket"],
               "Leo": ["have a cup of tea and some good rest, bud", "book"],
               "Virgo": ["a great success awaits you soon", "folder"],
               "Libra": ["you'll discover some unexpected things today", "duvet"],
               "Scorpio": ["wonderful day to take a stroll!", "boots"],
               "Capricorn": ["time to be creative!", "paper"],}

full_months = [1, 3, 5, 7, 8, 9, 12]


def check_dob(dob):
    if len(dob) != 3 and (int(dob[0]) < 1900 or int(dob[0]) > 2016) and \
            (int(dob[1]) < 1 or int(dob[1]) > 12):
        return False
    else:
        if (int(dob[1]) in full_months and 1 <= int(dob[2]) <= 31) or \
                (int(dob[1]) not in full_months and 1 <= int(dob[2]) <= 30) or \
                (int(dob[1]) == 2 and int(dob[2]) % 4 == 0 and 1 <= int(dob[2]) <= 29) or \
                (int(dob[1]) == 2 and int(dob[2]) % 4 == 0 and 1 <= int(dob[2]) <= 29) or \
                (int(dob[1]) == 2 and int(dob[2]) % 4 != 0 and 1 <= int(dob[2]) <= 28):
            return True
        else:
            return False


def get_sign(dob):
    month = int(dob[1])
    day = int(dob[2])

    if month == 12:
        return 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        return 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        return 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        return 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        return 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        return 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        return 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        return 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        return 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        return 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        return 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        return 'Scorpio' if (day < 22) else 'Sagittarius'


dob = input("Enter your DOB (yyyy-mm-dd):").split('-')
sign = get_sign(dob)
print("Your sign is: " + sign)
print("Divination for you:")
print("\x1B[3m" + predictions[sign][0] + "\x1B[0m")
print("Lucky item: " + predictions[sign][1])

while not check_dob(dob):
    dob = input("Invalid input. Please, re-enter your DOB (yyyy-mm-dd):").split()



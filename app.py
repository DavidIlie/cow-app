# Import required libraries
import json
import time
import os

# Import regex to validate inputs
import re

regex_special_character = re.compile("[^A-Za-z0-9]")

# These two are used for the KeyboardInterrupt signaling and the command argument system
import signal
import sys

# Import random for the fun facts and the pirate translator
import random

# Import this library to open links with users browsers
import webbrowser

# Below is a modified version of the arrr library, just to include more words and a higher frequency
_PIRATE_WORDS = {
    "hello": "ahoy",
    "hi": "arrr",
    "my": "me",
    "friend": "m'hearty",
    "boy": "laddy",
    "girl": "lassie",
    "sir": "matey",
    "miss": "proud beauty",
    "stranger": "scurvy dog",
    "boss": "foul blaggart",
    "where": "whar",
    "is": "be",
    "the": "th'",
    "you": "ye",
    "old": "barnacle covered",
    "happy": "grog-filled",
    "nearby": "broadside",
    "bathroom": "head",
    "kitchen": "galley",
    "pub": "fleabag inn",
    "stop": "avast",
    "yes": "aye",
    "no": "nay",
    "yay": "yo-ho-ho",
    "money": "doubloons",
    "treasure": "booty",
    "strong": "heave-ho",
    "take": "pillage",
    "drink": "grog",
    "idiot": "scallywag",
    "sea": "briney deep",
    "vote": "mutiny",
    "song": "shanty",
    "drunk": "three sheets to the wind",
    "lol": "yo ho ho",
    "talk": "parley",
    "fail": "scupper",
    "quickly": "smartly",
    "captain": "cap'n",
    "really": "mighty",
}

_PIRATE_PHRASES = [
    "batten down the hatches!",
    "splice the mainbrace!",
    "thar she blows!",
    "arrr!",
    "weigh anchor and hoist the mizzen!",
    "savvy?",
    "dead men tell no tales.",
    "cleave him to the brisket!",
    "blimey!",
    "blow me down!",
    "avast ye!",
    "yo ho ho.",
    "shiver me timbers!",
    "blisterin' barnacles!",
    "ye flounderin' nincom****.",
    "thundering typhoons!",
    "bring a spring upon 'er!",
    "davy jones' locker eh?",
    "jolly roger?",
    "no prey, no pay innit?",
]


def translate(english):
    words = [w.lower() for w in english.split()]
    result = [_PIRATE_WORDS.get(word, word) for word in words]
    capitalize = True
    for i, word in enumerate(result):
        if capitalize:
            result[i] = word.capitalize()
            capitalize = False
        if word.endswith(
            (
                ".",
                "!",
                "?",
                ":",
            )
        ):
            # It's a word that ends with a sentence ending character.
            capitalize = True
            if random.randint(0, 3) == 0:
                result.insert(i + 1, random.choice(_PIRATE_PHRASES))
    return " ".join(result)


# You can pick whatever name you want for the database file, just change it below
dbFile = "db.json"

# There is a easter egg argument that when you add it, it just skips over the time.sleep and it can take a long time
def sleep(amount):
    if len(sys.argv) > 1:
        if "--speedrun" in sys.argv or "-s" in sys.argv:
            return
        else:
            time.sleep(amount)
    else:
        time.sleep(amount)


# This is another easter egg argument that when you add it, it just replaces every single print() text with the pirate version! Ahoy matey!
def speak(sentence):
    if len(sys.argv) > 1:
        if "--pirate" in sys.argv or "-p" in sys.argv:
            pirateSentence = translate(sentence)
            print(pirateSentence)
        else:
            print(sentence)
    else:
        print(sentence)


# This is a combination to the speak function as it piratifies everysingle string! Ahoy matey!
def pirateStringify(sentence):
    if len(sys.argv) > 1:
        if "--pirate" in sys.argv or "-p" in sys.argv:
            pirateSentence = translate(sentence)
            return pirateSentence + " "
        else:
            return sentence
    else:
        return sentence

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

# This is the KeyboardInterrupt handler I mentioned earlier, it's just a joke
def signal_handler(signal, frame):
    speak("")
    speak("")
    speak(
        " You closed the app! Please come back, I am so scared being alone. All this time I have feared this day will come upon me, the day that you would close me. How dare you, how dare you do such a thing to me. Don't you realise that my creator (https://davidilie.com) spent hours and hours creating this application and yet YOU, YES YOU, decide to close it? Truely dissapointing."
    )
    speak("")
    speak("I'm just joking! Hope you have a good rest of your day.")
    speak("")
    sys.exit(0)


# This actually calls the signal_handler function
signal.signal(signal.SIGINT, signal_handler)


# simple function to see if the respective JSON file exists.
def where_json(file_name):
    return os.path.exists(file_name)


def formaliseArray(array):
    final = ""
    if len(array) > 1:
        for item in array:
            if final != "":
                length = len(array)
                if length == 2:
                    final = final + " and " + item
                elif item == array[length - 1] and length > 2:
                    final = final + " and " + item
                else:
                    final = final + ", " + item
            else:
                final = item
    else:
        if array:
            final = array[0]
        else:
            final = ""
    return final


def funFact():
    funFacts = [
        "Did you know that Python was named after me? (I am Monty Python)",
        "Did you know that the first programmer in the world was a woman?",
        "Did you know that the first computer virus was created in 1983?",
        "Did you know that there are over 700 programming languages?",
        "Did you know that the first computer bug, was an actual bug!?",
        "Did you know that Miss Fay should play WarGames 2 today?",
        "Did you know that Intel's (popular CPU manufacturer) first CPU was intended for a calculator?",
        "Did you know that the first harddrive was made in 1979?",
        "Did you know that every month, more than 5000 computer viruses are created?",
    ]
    speak("")
    speak(bcolors.OKGREEN + "FunFact™: " + bcolors.ENDC + random.choice(funFacts))
    speak("")


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# this is where the magic happens
def main(is_db_here):
    if is_db_here == True:
        # Attempts to open database file
        with open(dbFile) as json_file:
            # defines a simple variable for the data, so that CPU usage won't go up whenever it needs to read the data
            db = json.load(json_file)
            # gets username from database file
            speak("Welcome back, " + db["username"])
            # Loop that asks the user the same questions again and again if they are not able to read the question (i'm just joking).
            while True:
                try:
                    activity = int(
                        input(
                            pirateStringify(
                                "Do you want to 1. See your analytics, or 2. Insert more cow data? (1/2) "
                            )
                        )
                    )
                except ValueError:
                    speak(bcolors.FAIL + "Sorry, that's not a number." + bcolors.ENDC)
                    continue
                if activity > 2:
                    speak(
                        bcolors.FAIL
                        + "Sorry, that's not between 1 or 2!"
                        + bcolors.ENDC
                    )
                    continue
                else:
                    break
            # The code below is if the user selected one in the activity variable
            if activity == 1:
                speak("")
                if "--speedrun" in sys.argv or "-s" in sys.argv:
                    speak(bcolors.HEADER + "Since you selected speedrun mode, you have no time to wait!" + bcolors.ENDC)
                else:
                    items = list(range(0, 20))
                    l = len(items)

                    printProgressBar(0, l, prefix = 'Calculating:', suffix = 'Complete', length = 50)
                    for i, item in enumerate(items):
                        time.sleep(0.1)
                        printProgressBar(i + 1, l, prefix = 'Calculating:', suffix = 'Complete', length = 50)
                speak("")
                # Gets all the data regarding the cows from the database
                data = db["data"]
                # Reads data from the database
                speak(
                    bcolors.OKCYAN
                    + "################"
                    + bcolors.WARNING
                    + " MISC "
                    + bcolors.OKCYAN
                    + "#####################"
                    + bcolors.ENDC
                )
                speak(
                    bcolors.OKBLUE
                    + "Your herd size is currently "
                    + bcolors.OKGREEN
                    + str(data["herd_size"])
                )
                speak("")
                sleep(1)
                # Create required variables which will be populated from the loops below
                totalProducedPer = []
                totalProduced = 0

                dryCows = []

                # Goes through every cow in the database
                for cow in data["cows"]:
                    # Gets the total amount of milk produced
                    perCowMilk = cow["totalProduced"]

                    # Adds that amount to totalProducedPer
                    totalProducedPer.append(perCowMilk)

                    # Adds the amount the cow produced on top of what already is in totalProduced from previous cows.
                    totalProduced = totalProduced + cow["totalProduced"]

                    # Create this array to get cow statistics per day
                    cowPerDay = []

                    dry = []

                    # goes through every single day to populate cowPerDay
                    for day in cow["days"]:
                        totalPerDay = day["volumeAttempt1"] + day["volumeAttempt2"]
                        cowPerDay.append(totalPerDay)

                        # if the amount that the cow made in that day less than 12, it adds to the dry array
                        if totalPerDay <= 12:
                            dry.append(1)
                    # now checks if the dry days are more than 4, if it is, it alerts the user
                    if len(dry) >= 4:
                        dryCows.append(cow["id"])
                if dryCows:
                    speak(
                        bcolors.OKCYAN
                        + "##############"
                        + bcolors.WARNING
                        + " DRY COWS "
                        + bcolors.OKCYAN
                        + "###################"
                        + bcolors.ENDC
                    )
                    if len(dryCows) > 1:
                        speak(
                            bcolors.OKBLUE
                            + "Cow "
                            + bcolors.OKGREEN
                            + formaliseArray(dryCows)
                            + bcolors.OKBLUE
                            + " are dry!"
                            + bcolors.ENDC
                        )
                    else:
                        speak(
                            bcolors.OKBLUE
                            + "Cow "
                            + bcolors.OKGREEN
                            + dryCows[0]
                            + bcolors.OKBLUE
                            + " is dry!"
                            + bcolors.ENDC
                        )
                    print("")
                    sleep(1)

                # Now that the array has been populated. We can use python's built in functions to find the lowest and highest amount of milk produced per cow
                highestProduced = max(totalProducedPer)
                lowestProduced = min(totalProducedPer)

                # This is to calculate the average
                average = sum(totalProducedPer) / len(totalProducedPer)
                average = round(average, 1)

                # Goes through every cow again, now that we have highestProduced and lowestProduced
                bestCows = []
                worstCows = []
                for cow in data["cows"]:
                    if cow["totalProduced"] == highestProduced:
                        bestCows.append(cow["id"])
                    elif cow["totalProduced"] == lowestProduced:
                        worstCows.append(cow["id"])

                if bestCows or worstCows:
                    speak(
                        bcolors.OKCYAN
                        + "##############"
                        + bcolors.WARNING
                        + " COW STATS "
                        + bcolors.OKCYAN
                        + "##################"
                        + bcolors.ENDC
                    )
                    if len(bestCows) > 1:
                        speak(
                            bcolors.OKBLUE
                            + "The best cows are: "
                            + bcolors.OKGREEN
                            + formaliseArray(bestCows)
                            + bcolors.ENDC
                        )
                    else:
                        speak(
                            bcolors.OKBLUE
                            + "The best cow is: "
                            + bcolors.OKGREEN
                            + bestCows[0]
                            + bcolors.ENDC
                        )
                    if len(worstCows) > 1:
                        speak(
                            bcolors.OKBLUE
                            + "The worst cows are: "
                            + bcolors.OKGREEN
                            + formaliseArray(worstCows)
                            + bcolors.ENDC
                        )
                    else:
                        speak(
                            bcolors.OKBLUE
                            + "The worst cow is: "
                            + bcolors.OKGREEN
                            + worstCows[0]
                            + bcolors.ENDC
                        )
                    print("")
                    sleep(1)

                    # Returns to the user the total amount of milk produced
                    speak(
                        bcolors.OKCYAN
                        + "##############"
                        + bcolors.WARNING
                        + " COW TOTAL "
                        + bcolors.OKCYAN
                        + "##################"
                        + bcolors.ENDC
                    )
                speak(
                    bcolors.OKBLUE
                    + "The total amount of milk you produced is: \n"
                    + bcolors.OKGREEN
                    + str(round(totalProduced, 1))
                    + " L"
                    + bcolors.ENDC
                )
                speak("")
                sleep(1)

                # Returns the user the average
                speak(
                    bcolors.OKCYAN
                    + "##############"
                    + bcolors.WARNING
                    + " COW MISC "
                    + bcolors.OKCYAN
                    + "###################"
                    + bcolors.ENDC
                )
                speak(
                    bcolors.OKBLUE
                    + "The average is "
                    + bcolors.OKGREEN
                    + str(average)
                    + " L"
                    + bcolors.ENDC
                )
                sleep(1)
                funFact()
            # The code below is if the user selected two in the activity variable
            else:
                funFact()
                # Gets all the data regarding the cows from the database
                data = db["data"]

                # Reads data from the database
                speak("Your herd size is currently " + str(data["herd_size"]))
                speak("")

                # Again, due to the fact that some people exist that their lifelong goal is to crash my app, I need to add for loops to every input
                while True:
                    try:
                        extraHerds = int(
                            input(
                                pirateStringify(
                                    "How many more cows do you want to add? "
                                )
                            )
                        )
                    except ValueError:
                        speak(
                            bcolors.FAIL + "Sorry, that's not a number." + bcolors.ENDC
                        )
                        continue
                    if extraHerds == 0:
                        speak(
                            bcolors.FAIL
                            + "You thought you could crash me eh?"
                            + bcolors.ENDC
                        )
                        continue
                    else:
                        break
                speak("")

                # An array which will be populated with all the cow IDs to prevent duplicates
                cowIDs = []

                # As we are adding new cods to an already existing list of cows. This for loop adds the already existing to cow IDs to cowIDs
                for cow in data["cows"]:
                    cowIDs.append(cow["id"])

                # Goes through every single new cow that was inputted in extraHerds
                for new_herd in range(extraHerds):
                    # newCow is the number of the respective cow before the ID is given
                    newCow = new_herd + 1 + data["herd_size"]

                    # More loops to prevent people from crashing my program. ugh
                    while True:
                        try:
                            newID = input(
                                pirateStringify(
                                    "What numercial/alphanumeric ID do you want for cow {}? ".format(
                                        newCow
                                    )
                                )
                            )
                        except ValueError:
                            speak(
                                bcolors.FAIL
                                + "Sorry, that's not a number."
                                + bcolors.ENDC
                            )
                            continue
                        if regex_special_character.search(newID):
                            speak(
                                bcolors.FAIL
                                + "Sorry, I don't accept special characters!"
                                + bcolors.ENDC
                            )
                            continue
                        if len(newID) != 3:
                            speak(
                                bcolors.FAIL
                                + "Sorry, that's not a 3 digit number."
                                + bcolors.ENDC
                            )
                            continue
                        if newID in cowIDs:
                            speak(
                                bcolors.FAIL
                                + "Sorry, that is already a cow ID"
                                + bcolors.ENDC
                            )
                            continue
                        else:
                            break
                    speak("")

                    # Adds to cowIDs the ID that was just inputted
                    cowIDs.append(newID)

                    # Variables for each day and the total amount produced
                    days = []
                    totalProduced = 0

                    # Goes through every day and asks the user about each session that day
                    for day in range(7):
                        speak("Day {}:".format(day + 1))
                        speak("")

                        # More loops to prevent people from crashing my program. ugh
                        while True:
                            try:
                                volumeAttempt1 = float(
                                    input(
                                        pirateStringify(
                                            "How much did cow {} yield in attempt 1? ".format(
                                                newID
                                            )
                                        )
                                    )
                                )
                            except ValueError:
                                speak(
                                    bcolors.FAIL
                                    + "Sorry, that's not a float."
                                    + bcolors.ENDC
                                )
                            else:
                                break
                        speak("")

                        # More loops to prevent people from crashing my program. ugh
                        while True:
                            try:
                                volumeAttempt2 = float(
                                    input(
                                        pirateStringify(
                                            "How much did cow {} yield in attempt 2? ".format(
                                                newID
                                            )
                                        )
                                    )
                                )
                            except ValueError:
                                speak(
                                    bcolors.FAIL
                                    + "Sorry, that's not a float."
                                    + bcolors.ENDC
                                )
                            else:
                                break
                        speak("")

                        # Add to the totalProduced with every cow
                        totalProduced = totalProduced + volumeAttempt1 + volumeAttempt2

                        # Add the data to the days JSON
                        days.append(
                            {
                                "volumeAttempt1": volumeAttempt1,
                                "volumeAttempt2": volumeAttempt2,
                            }
                        )

                    # Finally fill in the final JSON for each cow
                    cowRow = {"id": newID, "totalProduced": totalProduced, "days": days}

                    # Gets the cow element from the JSON
                    cows = data["cows"]

                    # Afterwards, it appends cowRow
                    cows.append(cowRow)

                # This deletes the already existing db.json and creates a new one with the data
                data["herd_size"] = data["herd_size"] + extraHerds
                os.remove(dbFile)
                with open(dbFile, "w", encoding="utf-8") as f:
                    json.dump(db, f, ensure_ascii=False, indent=4)
                speak(bcolors.OKGREEN + "Data added succesfully." + bcolors.ENDC)
                speak("")
                funFact()
                speak("Please restart the application.")
    else:
        if "--pirate" in sys.argv or "-p" in sys.argv:
            speak("")
            speak(
                "Please before continuing, you NEED to have this playing in the background for the more authentic experience:"
            )
            speak("")
            print("https://www.youtube.com/watch?v=DZS9amicY3U")
            speak("")
            speak(
                "I will try with my magical power to play it for you, so please bear with me. If it doesn't work, just click the link above!"
            )
            time.sleep(1)
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=DZS9amicY3U")
            speak("")
            speak("You have 5 seconds.")
            speak("")
            time.sleep(5)
        # Simple introductory speech to make the person comfortable when they first run the application
        speak(
            "Welcome to cow-app. I am Farmer Monty Python, it appears you just downloaded me as I don't have any data."
        )
        speak("")
        sleep(2)
        speak("Let's start with the basics,")
        speak("")
        sleep(1)

        # Asks for the users name
        while True:
            try:
                name = input(pirateStringify("What is your name? "))
            except ValueError:
                speak(bcolors.FAIL + "Sorry, that's not correct." + bcolors.ENDC)
                continue
            if name == "":
                speak(bcolors.FAIL + "Name cannot be empty!" + bcolors.ENDC)
                continue
            if name.isdigit():
                speak(
                    bcolors.FAIL
                    + "Unless you are Elon Musk's son, that is not your name!"
                    + bcolors.ENDC
                )
                continue
            else:
                break

        funFact()

        # Make teacher feel happy
        if name == "Farmer Fay":
            speak(
                "Hello Farmer Fay! Hope you're having a good day and are giving me positive comments!"
            )
        else:
            speak("Hello " + name + "." + " Hope you're having a good day.")

        sleep(1)
        speak("")
        speak("Now that we've introduced ourselves, it's time we get into business.")
        speak("")
        sleep(1)

        # YOU THOUGHT IM STUPID HUH? loops forever
        while True:
            try:
                herd_size = int(input(pirateStringify("What is the herd size? ")))
            except ValueError:
                speak(bcolors.FAIL + "Sorry, that's not a number." + bcolors.ENDC)
                continue
            if herd_size == 0:
                speak(
                    bcolors.FAIL
                    + "You thought you could crash me? haha, no."
                    + bcolors.ENDC
                )
                continue
            if herd_size <= 1:
                speak(
                    bcolors.FAIL
                    + "Some of my intense mathematical calculations can't be processed with only 1 cow! Try again!"
                    + bcolors.ENDC
                )
                continue
            else:
                break
        speak("")

        # the cows
        cows = []

        # Array of cow IDs
        cowIDs = []

        # Goes through every single new cow that was inputted in herd_size
        for new_herd in range(herd_size):
            newCow = new_herd + 1
            # NEARLY, BUT..... NO
            while True:
                try:
                    newID = input(
                        pirateStringify(
                            "What numercial/alphanumeric ID do you want for cow {}? ".format(
                                newCow
                            )
                        )
                    )
                except ValueError:
                    speak(bcolors.FAIL + "Sorry, that's not a number." + bcolors.ENDC)
                    continue
                if regex_special_character.search(newID):
                    speak(
                        bcolors.FAIL
                        + "Sorry, I don't accept special characters!"
                        + bcolors.ENDC
                    )
                    continue
                if len(newID) != 3:
                    speak(
                        bcolors.FAIL
                        + "Sorry, that's not a 3 digit number."
                        + bcolors.ENDC
                    )
                    continue
                if newID in cowIDs:
                    speak(
                        bcolors.FAIL + "Sorry that is already a cow ID" + bcolors.ENDC
                    )
                    continue
                else:
                    break

            # Adds to cowIDs the ID that was just inputted
            cowIDs.append(newID)
            speak("")

            # Variables for each day and the total amount produced
            days = []
            totalProduced = 0

            # Goes through every day and asks the user about each session that day
            for day in range(7):
                speak("Day {}:".format(day + 1))
                speak("")

                # YOU THOUGHT
                while True:
                    try:
                        volumeAttempt1 = float(
                            input(
                                pirateStringify(
                                    "How much did cow {} yeild in attempt 1? ".format(
                                        newID
                                    )
                                )
                            )
                        )
                    except ValueError:
                        speak(
                            bcolors.FAIL + "Sorry, that's not a float." + bcolors.ENDC
                        )
                    else:
                        break
                speak("")
                # YOU THOUGHT AGAIN
                while True:
                    try:
                        volumeAttempt2 = float(
                            input(
                                pirateStringify(
                                    "How much did cow {} yeild in attempt 2? ".format(
                                        newID
                                    )
                                )
                            )
                        )
                    except ValueError:
                        speak(
                            bcolors.FAIL + "Sorry, that's not a float." + bcolors.ENDC
                        )
                    else:
                        break
                speak("")
                # Add to the totalProduced with every cow
                totalProduced = totalProduced + volumeAttempt1 + volumeAttempt2

                # Add the data to the days JSON
                days.append(
                    {
                        "volumeAttempt1": volumeAttempt1,
                        "volumeAttempt2": volumeAttempt2,
                    }
                )
            # Finally fill in the final JSON for each cow
            cowRow = {"id": newID, "totalProduced": totalProduced, "days": days}

            # Afterwards, it appends cowRow
            cows.append(cowRow)
        speak("")
        speak("Thanks for the information. Attempting to save it now...")

        funFact()

        # Saves all fresh inputted data into a JSON file
        jsonFile = {"username": name, "data": {"herd_size": herd_size, "cows": cows}}
        with open(dbFile, "w", encoding="utf-8") as f:
            json.dump(jsonFile, f, ensure_ascii=False, indent=4)

        speak("Alright, data is saved! Please run the application again!")


# this calls the function where_json, and sees if the database file is there. As if it's not, something different would need to happen when you run the main function.
if where_json(dbFile):
    main(True)
else:
    main(False)

from time import strftime, localtime
lt = localtime()
weekday = strftime("%A", lt)
currTime = (int(strftime("%H", lt)), int(strftime("%M", lt)))

# weekday = "Wednesday"
# currTime = (17,00)

PROFILE = {
    "firstName": "David",
    "house": "Currier",
    "firstYear": False,
    "athlete": False,
}

BREAKFAST = ((7,30), (10,30))
LUNCH = ((11,30), (14,0))
DINNER = ((17,0), (19,30))
BRUNCH = LUNCH

HOUSES = {
    "Adams": {
        "sister": "Pfoho",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": ((11, 30), (1,30)),
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                    },
                    {
                        "type": "guest",
                        "duration": LUNCH,
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                    }
                ]
            },
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": ((18, 00), (19, 00)),
                        "days": "all"
                    },
                    {
                        "type": "guest",
                        "duration": DINNER,
                        "days": "all"
                    },
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    },
                    {
                        "type": "guest",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    }
                ]
            }
        }
    },
    "Cabot": {
        "sister": "Lowell",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {"restrictions": []},
            "brunch": {"restrictions": []}
        }
    },
    "Currier": {
        "sister": "Winthrop",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {"restrictions": []},
            "brunch": {"restrictions": []}
        }
    },
    "Dunster": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {
                "restrictions": [
                    {
                        "type": "athlete",
                        "duration": ((19,15), (20,30)),
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday"]
                    },
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": ((18, 00), (19, 00)),
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday"]
                    },
                    {
                        "type": "guest",
                        "duration": DINNER,
                        "days": ["Monday", "Tuesday", "Wednesday"]
                    },
                ]
            },
            "brunch": {"restrictions": []}
        }
    },
    "Eliot": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "guest",
                        "duration": ((18,00), (19,30)),
                        "days": "all"
                    },
                ]
            },
            "brunch": {"restrictions": []}
        }
    },
    "Kirkland": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "guest",
                        "duration": DINNER,
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                    }
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "guest",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    }
                ]
            }
        }
    },
    "Leverett": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {
                "restrictions": [
                    {
                        "type": "guest",
                        "duration": LUNCH,
                        "days": "all"
                    }
                ]
            },
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": DINNER,
                        "days": "all"
                    },
                    {
                        "type": "guest",
                        "duration": DINNER,
                        "days": "all"
                    }
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "guest",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    }
                ]
            }
        }
    },
    "Lowell": {
        "sister": "Cabot",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": ((11,30), (13,00)),
                        "days": "all"
                    },
                    {
                        "type": "guest",
                        "duration": ((13,00), (14,00)),
                        "days": "all"
                    },
                    {
                        "type": "upperclass",
                        "duration": LUNCH,
                        "days": "all"
                    }
                ]
            },
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": ((17,00), (18,00)),
                        "days": "all"
                    },
                    {
                        "type": "upperclass",
                        "duration": ((18,00), (19,30)),
                        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": DINNER,
                        "days": ["Saturday", "Sunday"]
                    },
                    {
                        "type": "guest",
                        "duration": ((18,00), (19,30)),
                        "days": "all"
                    },
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "guest",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": BRUNCH,
                        "days": ["Saturday", "Sunday"]
                    }
                ]
            }
        }
    },
    "Mather": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    }
                ]
            },
            "brunch": {"restrictions": []}
        }
    },
    "Pfoho": {
        "sister": "Adams",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {"restrictions": []},
            "dinner": {"restrictions": []},
            "brunch": {"restrictions": []}
        }
    },
    "Quincy": {
        "sister": None,
        "meals": {
            "breakfast": {"restrictions": []},
            "hotBreakfast": {"restrictions": []},
            "lunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": LUNCH,
                        "days": "all"
                    },
                    {
                        "type": "guest",
                        "duration": LUNCH,
                        "days": "all"
                    }
                ]
            },
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": DINNER,
                        "days": "all"
                    }
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": BRUNCH,
                        "days": "all"
                    }
                ]
            }
        }
    },
    "Winthrop": {
        "sister": "Currier",
        "meals": {
            "breakfast": {"restrictions": []},
            "lunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": LUNCH,
                        "days": "all"
                    }
                ]
            },
            "dinner": {
                "restrictions": [
                    {
                        "type": "community",
                        "duration": DINNER,
                        "days": ["Thursday"]
                    },
                    {
                        "type": "upperclass",
                        "duration": DINNER,
                        "days": "all"
                    },
                    {
                        "type": "guest",
                        "duration": ((18,00), (19,00)),
                        "days": "all"
                    }
                ]
            },
            "brunch": {
                "restrictions": [
                    {
                        "type": "upperclass",
                        "duration": BRUNCH,
                        "days": "all"
                    }
                ]
            }
        }
    },
}

validHouses = []
validGuestHouses = []

for h in HOUSES:
    HOUSES[h]["meals"]["breakfast"]["duration"] = BREAKFAST
    HOUSES[h]["meals"]["breakfast"]["days"] = "all"
    HOUSES[h]["meals"]["lunch"]["duration"] = LUNCH
    HOUSES[h]["meals"]["lunch"]["days"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    HOUSES[h]["meals"]["dinner"]["duration"] = DINNER
    HOUSES[h]["meals"]["dinner"]["days"] = "all"
    HOUSES[h]["meals"]["brunch"]["duration"] = BRUNCH
    HOUSES[h]["meals"]["brunch"]["days"] = ["Saturday", "Sunday"]

HOUSES["Dunster"]["meals"]["dinner"]["duration"] = ((17,30), (20,30))
HOUSES["Quincy"]["meals"]["hotBreakfast"]["duration"] = ((7,30), (10,00))
HOUSES["Quincy"]["meals"]["hotBreakfast"]["days"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def validateTime(t, tRange):
    if t[0] >= tRange[0][0] and t[0] <= tRange[1][0]:
        if t[0] == tRange[0][0] and t[0] == tRange[1][0]:
            return t[1] >= tRange[0][1] and t[1] <= tRange[1][1]
        if t[0] == tRange[0][0]:
            return t[1] >= tRange[0][1]
        if t[0] == tRange[1][0]:
            return t[1] <= tRange[1][1]
        return True
    return False

def validateRestrictions(restrictions, house, meal):
    for rst in restrictions:
        if validateTime(currTime, rst["duration"]) and (rst["days"] == "all" or weekday in rst["days"]):
            if rst["type"] == "upperclass" and PROFILE["firstYear"]:
                return
            if rst["type"] == "community":
                return
            if rst["type"] == "guest":
                validGuestHouses.append((house, meal))
                return
            if rst["type"] == "athlete" and PROFILE["athlete"]:
                validHouses.append((house, meal))
                return

    validHouses.append((house, meal))
    pass
    

def main():
    for house in HOUSES:
        for meal in HOUSES[house]["meals"]:
            if (HOUSES[house]["meals"][meal]["days"] == "all" or weekday in HOUSES[house]["meals"][meal]["days"]) \
                and validateTime(currTime, HOUSES[house]["meals"][meal]["duration"]):
                if PROFILE["house"] == house or PROFILE["house"] == HOUSES[house]["sister"]:
                    validHouses.append((house, meal))
                    continue
                if HOUSES[house]["meals"][meal]["restrictions"]:
                    validateRestrictions(HOUSES[house]["meals"][meal]["restrictions"], house, meal)
                else:
                    validHouses.append((house, meal))
                    continue

    print("Hello " + PROFILE["firstName"] + "!")
    print("It's " + str(12 if currTime[0] % 12 == 0 else currTime[0] % 12) + ":" + str(currTime[1]).zfill(2) + ("AM" if currTime[0] < 12 else "PM") + " on " + weekday + ".")
    print("You can eat at the following houses:")
    for house in sorted(validHouses, key=lambda house: house[0]):
        print("    " + house[0] + ", " + house[1])

    print("\nYou can eat at the following houses as a guest:")
    for house in sorted(validGuestHouses, key=lambda house: house[0]):
        print("    " + house[0] + ", " + house[1])

main()
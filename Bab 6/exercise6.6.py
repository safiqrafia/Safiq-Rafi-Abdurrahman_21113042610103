
poll = ["jen", "sarah", "edward", "phil", "james", "linda"]

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",

}

for person in poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.capitalize()}!")
    else:
        print(f"{person.capitalize()}, please take the poll!")    
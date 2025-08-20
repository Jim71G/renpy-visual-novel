label start:
   label start:
    scene black
    "Booting up the Vault..."
    jump onboarding

label onboarding:
    $ player_name = renpy.input("What’s your name, apprentice?")
    $ player_name = player_name.strip()

    $ player_age = renpy.input("How old are you?")
    $ player_age = int(player_age)

    menu:
        "Which hand do you favor for wiring and typing?":
            "Right-handed":
                $ handedness = "Right"
            "Left-handed":
                $ handedness = "Left"

    "Welcome, [player_name], age [player_age], [handedness]-handed. Let’s calibrate your skills."
    jump typing_test

    return

label typing_test:
    $ start_time = renpy.get_time()
    $ typed_phrase = renpy.input("Type this exactly: Mount the slice, log the lore.")
    $ end_time = renpy.get_time()
    $ typing_speed = end_time - start_time

    if typed_phrase.strip() == "Mount the slice, log the lore.":
        "Nice work. Your fingers are badge-ready."
    else:
        "Hmm... a few typos. Let’s try again later."

    "Typing speed: [typing_speed] seconds"
    return

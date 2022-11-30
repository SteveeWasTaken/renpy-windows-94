# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mon
    $ k_name = "Windows"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kis 1 at tcommon(1000)
    $ b_name = "b"
    b "Fuck you!"
    k "What?!"
    show b 1 at tcommon(400)
    b "I said fuck you!"
    menu:
        "No, fuck you!":
            k "No, fuck you!"
            b "Alright."
            "Good Ending"
            return
        "Okay.":
            k "Okay."
            b "Haha, I win!"
            "Bad Ending"
    return

screen select_character_screen():
    textbutton _("\u21e6"):
        xalign 0.25 ypos 0.5
        text_size 70
        action Call("change_to_next_left")

    textbutton _("\u21e8"):
        xalign 0.75 ypos 0.5
        text_size 70
        action Call("change_to_next_right")

    textbutton _("Поехали!"):
        xalign 0.5 ypos 0.9
        text_size 40
        action Jump("talk_with_bot")

label change_to_next_left:
    hide girl
    with moveoutleft

    python:
        if character_kind == "fm01":
            character_kind = "m01"
        else:
            character_kind = "fm01"

    show girl grin at center
    with moveinleft

    return

label change_to_next_right:
    hide girl
    with moveoutright

    python:
        if character_kind == "fm01":
            character_kind = "m01"
        else:
            character_kind = "fm01"

    show girl grin at center
    with moveinright

    return

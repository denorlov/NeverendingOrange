define hero = Character("[hero_name]")

# Игра начинается здесь:
label start:
    play music "audio/Земляне - Земля в иллюминаторе.mp3"
    show sky at rool_sky
    show shi at shine
    show sta at rain_stars1
    show sta2 at rain_stars2
    show gro

    show girl grin at center
    window hide

label select_character:
    show screen select_character_screen
    pause
    jump select_character

label talk_with_bot:
    hide screen select_character_screen
    window show

    show girl at left
    with move

    python:
        hero_name = renpy.input("Привет! Тебя как звать?")
        hero_name = hero_name.strip().capitalize()

    show girl

    "Ну здравствуй, {b}[hero_name]{/b}."

    python:
        reason = renpy.input("Как тебя сюда занесло, {b}[hero_name]{/b}?")

    show girl

    "А ты ничего так, {i}[hero_name]{/i}, вроде не глупый..."

    show girl

    "{b}[hero_name]{/b}, да ты даже, походу, умный..."

    show girl

    menu:
        "{i}[hero_name]{/i}, а ты Python знаешь?"

        "да":
            $character_mood = "smile"
            show girl
        "нет":
            show girl wow

    menu:
        "{i}[hero_name]{/i}, у тебя свой сайт есть?"

        "есть":
            jump has_site
        "неа, нет":
            jump dont_have_site

label has_site:
    show girl grin

    python:
        hero_site_url = renpy.input("Скажи адрес, я посмотрю")
        hero_site_url = hero_site_url.strip()

    $character_mood = "smile"
    show girl
    "{b}[hero_name]{/b}, я сходила посмотреть {a=[hero_site_url]}на твой сайт{/a}, он ничего, интересный..."
    show girl
    "Какой же ты {color=#f00}классый{/color}, {b}[hero_name]{/b}!"
    show girl
    "Погоди, что я только что сказала? Ты не классый, ты просто {s}крутой{/s} {size=+10}супер-крутой{/size}!"

    stop music fadeout 1.0
    return

label dont_have_site:
    $character_mood = "upset"
    show girl

    "{i}[hero_name]{/i}, учи python и html, потом поговорим..."

    stop music
    return
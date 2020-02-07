image gro = "ground.png"
image shi = "shine.png"
image sta = "star.png"
image sta2 = "star.png"

transform rool_sky: # «rool_sky» - ваше название трансформации
    xalign .5 # расположение изображения по оси X, меняйте под себя
    yalign .37 # расположение изображения по оси Y, меняйте под себя
    linear 400 rotate 360 # где 100- количество секунд, а 360 – количество градусов поворота
    rotate 0 # возвращает значение поворота к исходному
    repeat # повторяет трансформацию

transform shine: # «shine» - ваше название трансформации
    alpha 0 # где 0.1- стартовая непрозрачность при появлении
    linear 25.5 alpha 1.0 # 5.5 - количество секунд на присвоение следующего значения непрозрачности,
                         # alpha 1.0 - следующее значение непрозрачности
    linear 1.0 alpha 0.7
    linear 1.0 alpha 1.0
    linear 0.4 alpha 0.5
    linear 1.0 alpha 1.0
    linear 2.0 alpha 0.5
    linear 0.5 alpha 0.7
    linear 1.5 alpha 0.4
    linear 0.5 alpha 0.1
    repeat # повторяет трансформацию

transform rain_stars1:
    alpha 0.3 # где 0.3- стартовая непрозрачность при появлении
    xpos 1920 ypos 0 #начальное расположение изображения
    linear 0.5 xpos 50 ypos 750 #где 0.5 количество секунд на перемещение в координаты х50 y750
    pause (5) #пауза на 5 секунд
    repeat # повторяет трансформацию

transform rain_stars2:
    alpha 0.3
    xpos 620 ypos 0
    linear 0.5 xpos -1050 ypos 750
    pause (3)
    repeat

define hero = Character("[hero_name]")

# Игра начинается здесь:
label start:
    play music "audio/Земляне - Земля в иллюминаторе.mp3"

    show sky at rool_sky
    show shi at shine
    show sta at rain_stars1
    show sta2 at rain_stars2
    show gro

    show girl at left with dissolve

    python:
        hero_name = renpy.input("Привет! Тебя как звать?")
        hero_name = hero_name.strip().capitalize()

    "Ну здравствуй, {b}[hero_name]{/b}.
     Как тебя сюда занесло, {b}[hero_name]{/b}?"

    "А ты ничего так, {i}[hero_name]{/i}, вроде не глупый..."
    "{b}[hero_name]{/b}, да ты даже, походу, умный..."

    menu:
        "{i}[hero_name]{/i}, а ты Python знаешь?"

        "да":
            $know_python = True
        "нет":
            $know_python = False

    menu:
        "{i}[hero_name]{/i}, у тебя свой сайт есть?"

        "да":
            jump has_site
        "нет":
            jump dont_have_site

label has_site:
    python:
        hero_site_url = renpy.input("Скажи адрес, я посмотрю")
        hero_site_url = hero_site_url.strip()

    "{b}[hero_name]{/b}, я сходил посмотреть {a=[hero_site_url]}на твой сайт{/a}, он ничего, интересный..."
    "Какой же ты {color=#f00}классый{/color}, {b}[hero_name]{/b}!"
    "Погоди, что я только что сказала? Ты не классый, ты просто {s}крутой{/s} {size=+10}супер-крутой{/size}!"

    stop music fadeout 1.0
    return

label dont_have_site:
    "{i}[hero_name]{/i}, учи python и html, потом поговорим..."

    stop music
    return
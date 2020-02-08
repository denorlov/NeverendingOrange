image gro = "ground.png"
image shi = "shine.png"
image sta = "star.png"
image sta2 = "star.png"

transform rool_sky: # «rool_sky» - ваше название трансформации
    xalign .5 # расположение изображения по оси X, меняйте под себя
    yalign .37 # расположение изображения по оси Y, меняйте под себя
    linear 200 rotate 360 # где 100- количество секунд, а 360 – количество градусов поворота
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


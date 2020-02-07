define girl_wow = False
define girl_grin = False
define girl_talking = False
define girl_mood = "soft"
# soft, upset, grin, smile, serious

image girl mouth grin:
    "fm01/fm01-mouth-grin00.png"
    zoom 0.3

image girl body:
    "fm01/fm01-body.png"
    zoom 0.3

image girl mouth talking 00:
    "fm01/fm01-mouth-[girl_mood]00.png"
    zoom 0.3

image girl mouth talking 01:
    "fm01/fm01-mouth-[girl_mood]01.png"
    zoom 0.3

image girl mouth talking:
    "fm01/fm01-mouth-[girl_mood]00.png"
    zoom 0.3
    pause .2
    "fm01/fm01-mouth-[girl_mood]01.png"
    zoom 0.3
    choice:
        pause 1.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    repeat

image girl mouth wow = "fm01/fm01-mouth-wow01.png"

image girl eyes:
    "fm01/fm01-eyes-[girl_mood].png"
    zoom 0.3

image girl = Composite((400, 720),
    (0,0), "girl body",
    (0,0), "girl mouth grin",
    (0,0), "girl eyes",
)
define girl_mood = "soft"
# soft, upset, smile

image girl body:
    "fm01/fm01-body.png"
    zoom 0.3

image girl mouth talking:
    "fm01/fm01-mouth-[girl_mood]00.png"
    zoom 0.3
    pause .1
    "fm01/fm01-mouth-[girl_mood]01.png"
    zoom 0.3
    choice:
        pause 0.2
    choice:
        pause 0.3
    choice:
        pause 0.4
    repeat 5

image girl mouth wow:
    "fm01/fm01-mouth-wow01.png"
    zoom 0.3

image girl mouth grin:
    "fm01/fm01-mouth-grin00.png"
    zoom 0.3

image girl eyes:
    "fm01/fm01-eyes-[girl_mood].png"
    zoom 0.3

image girl eyes grin:
    "fm01/fm01-eyes-grin.png"
    zoom 0.3

image girl eyes wow:
    "fm01/fm01-eyes-wow.png"
    zoom 0.3

image girl = Composite(
    (400, 720),
    (0,0), "girl body",
    (0,0), "girl mouth talking",
    (0,0), "girl eyes",
)

image girl wow = Composite(
    (400, 720),
    (0,0), "girl body",
    (0,0), "girl mouth wow",
    (0,0), "girl eyes wow",
)

image girl grin:
    Composite((400, 720),
        (0,0), "girl body",
        (0,0), "girl mouth grin",
        (0,0), "girl eyes grin",
    )

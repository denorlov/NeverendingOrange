define character_kind = "m01" # fm01, fm02, m01

define character_mood = "soft" # soft, upset, smile

image girl body:
    "[character_kind]/[character_kind]-body.png"
    zoom 0.3

image girl mouth talking:
    "[character_kind]/[character_kind]-mouth-[character_mood]01.png"
    zoom 0.3
    pause .1
    "[character_kind]/[character_kind]-mouth-[character_mood]00.png"
    zoom 0.3
    choice:
        pause 0.2
    choice:
        pause 0.3
    choice:
        pause 0.4
    repeat 5

image girl mouth wow:
    "[character_kind]/[character_kind]-mouth-wow01.png"
    zoom 0.3

image girl mouth grin:
    "[character_kind]/[character_kind]-mouth-grin00.png"
    zoom 0.3

image girl eyes:
    "[character_kind]/[character_kind]-eyes-[character_mood].png"
    zoom 0.3

image girl eyes grin:
    "[character_kind]/[character_kind]-eyes-grin.png"
    zoom 0.3

image girl eyes wow:
    "[character_kind]/[character_kind]-eyes-wow.png"
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

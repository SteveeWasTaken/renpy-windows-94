image kis 1 = "images/kis.png"
define k = DynamicCharacter('k_name', image='kis', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
image bg mon = "images/a.png"
define b = DynamicCharacter('b_name', image='b', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
image b 1 = "images/b.png"

transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

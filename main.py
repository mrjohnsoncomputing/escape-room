from projectio import Projectio

io = Projectio()
switched = False

while true:
    # IF main toggle is on
    if True:
        # If connection made in AB
        if io.switch_is_on(io.AB) and switched == False:
            io.LED_on()
            switched = True
        elif io.switch_is_off(io.AB) and switched == True:
            io.LED_off()
            switched = False
    


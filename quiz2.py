import time

from gpiozero import LED, Button, RGBLED

from time import sleep

# Set up buttons as pull-up inputs. Wire to ground!

# Adjust pin number if needed

red_button=Button(25)

green_button=Button(24)

blue_button=Button(23)

# Set up LEDs as output
# Adjust pin numbers if needed, use GPIO number, not pin number


red_led = LED(22)

green_led = LED(27)

blue_led = LED(17)

#rgb_led = RGBLED(red=9, green=10, blue=11)

print("Push any button to control LED!")

#Do something, ex, main()



def main():
    #red_led.off()
    #green_led.off()
    #blue_led.off()


    if red_button.is_pressed:

        print("Red is pressed")

        red_led.on()

        #led.color= (1,0,0)

    else:

        red_led.off()

        #time.sleep(0.5)

    if green_button.is_pressed:

        print("Green is Pressed")

        green_led.on()

        #led.color= (0,1,0)

    else:

        green_led.off()

        #time.sleep(0.5)

    if blue_button.is_pressed:

        print("Blue is pressed ")

        blue_led.on()

        #led.color= (0,0,1)

    else:

        blue_led.off()

        #time.sleep(0.5)
    #time.sleep(0.5)
while True:

    main()
    
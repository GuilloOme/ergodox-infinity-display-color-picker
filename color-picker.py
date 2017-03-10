import serial

from pythonzenity.python_zenity import ColorSelection

from ergodox_infinity_display import ErgodoxInterface

SERIAL = '/dev/ttyACM0'


def main():
    color = ColorSelection(show_palette=True)
    str_color = '0x' + color[1:]
    hex_color = int(str_color, 16)

    red_mask = pow(0xFF0000, 2)
    green_mask = pow(0x00FF00, 2)
    blue_mask = pow(0x0000FF, 2)

    red = (hex_color & int(red_mask)) >> (16 * 2)
    green = (hex_color & int(green_mask)) >> (8 * 2)
    blue = (hex_color & int(blue_mask))

    print('STLcdNumberXXColor = "{}, {}, {}";'.format(hex(red).upper(), hex(green).upper(), hex(blue).upper()))

    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
    ser.close()
    ser.open()
    dox = ErgodoxInterface(ser)
    dox.lcd_color(red, green, blue)
    dox.clear()
    ser.close()


if __name__ == '__main__':
    main()

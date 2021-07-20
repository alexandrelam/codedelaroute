import pyautogui as pg
import win32api
import keyboard

PLUS_X = 416
PLUS_Y = 118
PLUS_X_VALIDATE = 750
PLUS_Y_VALIDATE = 192

def calibrate():
    print('Press Ctrl-C to quit.')
    x = 0
    y = 0
    try:
        while True:
            state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
            if state_left < -127:
                break
            x, y = pg.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
    return x, y

if __name__ == "__main__":
    running = True
    calibrated = False
    printCalibrated = True
    x = 0
    y = 0
    while running:
        if calibrated == False:
            x, y = calibrate()
            calibrated = True
        
        if calibrated and printCalibrated:
            printCalibrated = False
            print('\n\n---------  Position calibrated!  ---------\n\n')
        
        if keyboard.is_pressed('c'):
            pg.click(x=x, y=y) 

        elif keyboard.is_pressed('v'):
            pg.click(x=x+PLUS_X, y=y) 
        
        elif keyboard.is_pressed('b'):
            pg.click(x=x, y=y+PLUS_Y) 

        elif keyboard.is_pressed('n'):
            pg.click(x=x+PLUS_X, y=y+PLUS_Y) 

        elif keyboard.is_pressed('enter'):
            pg.click(x=x+PLUS_X_VALIDATE, y=y+PLUS_Y_VALIDATE) 




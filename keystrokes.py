from pynput import keyboard, mouse
from datetime import datetime
import csv


keys_csv = open('keys.csv', mode='w')
mouse_csv = open('mouse.csv', mode='w')
keys_writer = csv.writer(keys_csv, delimiter = ',', quoting=csv.QUOTE_ALL)  
keys_writer.writerow(["Key Pressed", "Date", "UNIX Time"])

mouse_writer = csv.writer(mouse_csv, delimiter = ',', quoting= csv.QUOTE_ALL)
mouse_writer.writerow(["Mouse Action", "Location", "Date", "UNIX Time"])


def timestamp():
    """
    Gets the current timestamp in date and Unix time
    """
    current_time = datetime.now()
    ts = datetime.now().timestamp()
    formatted_time_day = current_time.strftime('%m/%d/%Y')
    # formatted_time_hour = current_time.strftime('%H:%M:%S.%f')

    return (formatted_time_day, ts)


def on_press(key):
    """
    Recognizes when a key is pressed and adds the key value 
    and the timestamp to the keyboard csv file.
    """
    if str(key) == 'Key.esc':
        print('Exiting...')    
        return False

    else:
        line = "{}".format(key)
        time = timestamp()
        keys_writer.writerow([line, time[0], time[1]])


def on_click(x, y, button, pressed):
    """
    For mouse usage: determines when/where the mouse has been clicked and adds to mouse csv file.
    """
    if pressed == True:
        time = timestamp()
        mouse_writer.writerow(['Pressed', (x, y), time[0], time[1]])

def on_move(x, y):
    """
    Get location of mouse whenever it moves
    """

    time = timestamp()
    mouse_writer.writerow(['Location', (x, y), time[0], time[1]])

    
def main():
    
    with keyboard.Listener(on_press=on_press) as listener:
    
        with mouse.Listener(on_click=on_click) as listener2: 
            
            listener.join()  
            if listener.running == True: 
                listener2.join()
            else:
                listener2.stop()
                keys_csv.close()
                mouse_csv.close()
            

if __name__ == "__main__":
    main()

import pyscreeze
from AppKit import NSWorkspace

from datetime import datetime
import csv
import time

apps_csv = open('apps.csv', mode='w')
apps_writer = csv.writer(apps_csv, delimiter = ',', quoting=csv.QUOTE_ALL)  
apps_writer.writerow(["App Used", "Date", "UNIX Time"])

def timestamp():
    """
    Gets the current timestamp in date and Unix time
    """
    current_time = datetime.now()
    ts = datetime.now().timestamp()
    formatted_time_day = current_time.strftime('%m/%d/%Y')
    # formatted_time_hour = current_time.strftime('%H:%M:%S.%f')

    return (formatted_time_day, ts)


def takeScreenshot(timing):

    name = str(timing[0]) + "_" + str(timing[1]) + ".jpg"
    im = pyscreeze.screenshot()
    return im


def getActiveApp(timing):


    active_app = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
    apps_writer.writerow([active_app, timing[0], timing[1]])


def main():
    start = time.time()
    elapsed = time.time()
    print(elapsed - start)

    while elapsed - start < 10:
        print(elapsed-start)
        if elapsed - start > 1: 
            print("if ", elapsed - start)
            timing = timestamp()
            takeScreenshot(timing)
            getActiveApp(timing)
            start = elapsed

        else:
            elapsed = time.time()
            print("else ", elapsed)


if __name__ == "__main__":
    main()
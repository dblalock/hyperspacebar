import pyscreeze
from AppKit import NSWorkspace

from datetime import datetime
import csv
import time

apps_csv = open('apps.csv', mode='a')
apps_writer = csv.writer(apps_csv, delimiter = ',', quoting=csv.QUOTE_ALL)  
apps_writer.writerow(["App Used", "Date", "UNIX Time"])

def timestamp():
    """
    Gets the current timestamp in date and Unix time
    """
    current_time = datetime.now()
    ts = datetime.now().timestamp()
    formatted_time_day = current_time.strftime('%m:%d:%Y')
    # formatted_time_hour = current_time.strftime('%H:%M:%S.%f')

    return (formatted_time_day, ts)


def takeScreenshot(timing):

    name = str(timing[1]) + ".png"
    im = pyscreeze.screenshot(name)
    return im


def getActiveApp(timing):


    active_app = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
    apps_writer.writerow([active_app, timing[0], timing[1]])


def main():
    start = time.time()
    elapsed = time.time()
    while elapsed - start < 100:

        if elapsed - start > 10: 

            timing = timestamp()
            im = takeScreenshot(timing)
            # im = pyscreeze.screenshot(str(timing[1]) + ".png")
            getActiveApp(timing)
            start = elapsed

        else:
            elapsed = time.time()


if __name__ == "__main__":
    main()
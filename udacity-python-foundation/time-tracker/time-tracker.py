import webbrowser
import time

print('Started counting time at '+time.ctime())
for i in range(0, 3):
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=iuwAZ-x1sAo')

import time, subprocess


timeLeft = 60
while timeLeft > 0:
    print("time %s" % timeLeft)
    # print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'alarm.wav'])

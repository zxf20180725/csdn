from TaskTimer import TaskTimer
from spider import main

timer = TaskTimer()
timer.join_task(main, [], interval=600)
timer.start()

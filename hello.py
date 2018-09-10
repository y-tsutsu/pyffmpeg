import os
import threading
from datetime import datetime

import ffmpeg
from apscheduler.schedulers.blocking import BlockingScheduler


def recording():
    filename = '{}_camera.mp4'.format(
        datetime.now().strftime('%Y%m%d_%H:%M:%S'))
    print('!!!!!!!!!! Start: {} !!!!!!!!!!'.format(filename), flush=True)
    stream = ffmpeg.input('input.mp4')
    # stream = ffmpeg.filter(stream, 'fps', fps=15)
    stream = ffmpeg.output(stream, filename, t=100)
    ffmpeg.run(stream)
    print('!!!!!!!!!! Complete: {} !!!!!!!!!!'.format(filename), flush=True)
    print(datetime.now(), flush=True)


def main():
    sc = BlockingScheduler()
    sc.add_job(recording, 'interval', minutes=1, max_instances=2)
    threading.Thread(target=recording).start()
    sc.start()


if __name__ == '__main__':
    main()

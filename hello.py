import os
import threading
from datetime import datetime

import ffmpeg
from apscheduler.schedulers.blocking import BlockingScheduler


def recording():
    filename = '{}_camera.mp4'.format(
        datetime.now().strftime('%Y%m%d_%H%M%S'))
    print('!!!!!!!!!! Start: {} !!!!!!!!!!'.format(filename), flush=True)
    stream = ffmpeg.input('rtsp://127.0.0.1:8554/rtsp', r=15)
    # stream = ffmpeg.input('input.mp4', r=15)
    stream = ffmpeg.output(stream, filename, format='mp4',
                           vcodec='copy', acodec='copy', t=70, ss=20, r=15)
    ffmpeg.run(stream)
    print('!!!!!!!!!! Complete: {} !!!!!!!!!!'.format(filename), flush=True)
    print(datetime.now(), flush=True)


# def recording2():
#     outfile = '{}_camera.mp4'.format(
#         datetime.now().strftime('%Y%m%d_%H:%M:%S'))
#     cmd = 'ffmpeg -i rtsp://127.0.0.1:8554/rtsp -t 70 -codec copy -f mp4 {}'.format(
#         outfile)
#     print('!!!!!!!!!! Start: {} !!!!!!!!!!'.format(outfile), flush=True)
#     os.system(cmd)
#     print('!!!!!!!!!! Complete: {} !!!!!!!!!!'.format(outfile), flush=True)
#     print(datetime.now(), flush=True)


# def recording3():
#     cmd = 'ffmpeg -i rtsp://127.0.0.1:8554/rtsp -codec copy -r 15 -f segment -strftime 1 -segment_time 60 -segment_format mp4 %Y%m%d_%H%M%S.mp4'
#     print('!!!!!!!!!! Start: {} !!!!!!!!!!', flush=True)
#     os.system(cmd)
#     print('!!!!!!!!!! Complete: {} !!!!!!!!!!', flush=True)
#     print(datetime.now(), flush=True)


def recording4():
    cmd = 'ffmpeg -i rtsp://127.0.0.1:8554/rtsp -r 15 -vcodec copy -acodec copy -f segment -strftime 1 -segment_time 60 -segment_format mp4 -r 15 %Y%m%d_%H%M%S.mp4'
    print('!!!!!!!!!! Start: {} !!!!!!!!!!', flush=True)
    os.system(cmd)
    print('!!!!!!!!!! Complete: {} !!!!!!!!!!', flush=True)
    print(datetime.now(), flush=True)


def main():
    # sc = BlockingScheduler()
    # action = recording
    # sc.add_job(action, 'interval', minutes=1, max_instances=2)
    # threading.Thread(target=action).start()
    # sc.start()
    recording4()


if __name__ == '__main__':
    main()

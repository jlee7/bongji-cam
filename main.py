import time
import datetime
import threading
import logging
import CameraControl
import RPi.GPIO as GPIO

class BongjiCam:
    def __init__(self):

        # GPIO Pin
        self.ObstaclePin = 23

        # Variables
        self.remaining_time = 10
        self.is_recording = False

        # CameraControl
        self.camera = CameraControl.CameraControl()
        self.camera.set_annotations()
        self.camera.set_resolution(1080, 720)
        self.camera.set_framerate(30)
        self.camera.set_annotations()

        # IRObstacleDetection
        self.setup()

    def start(self):
        # Threads
        self.thread_obstacle_loop = threading.Thread(target=self.loop, args=())
        self.thread_countdown = threading.Thread(target=self.countdown, args=())
        self.thread_countdown.start()
        self.thread_obstacle_loop.start()

    def setup(self):
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(self.ObstaclePin, GPIO.IN)
        logging.info("Setup finished.")

    def loop(self):
        logging.info("Start IRObstacle loop.")
        try:
            while True:
                if (0 == GPIO.input(self.ObstaclePin)):
                    self.remaining_time = 10

                    if not self.is_recording:
                        self.camera.start_recording(time.strftime("bongji_cam_%Y-%m-%d_%H_%M_%S") + ".h264")
                        logging.info("Start recording.")
                        self.is_recording = True

        except KeyboardInterrupt:
            self.destroy()
            logging.info("Stop IRObstacle loop.")

    def destroy(self):
        GPIO.cleanup()

    def countdown(self):
        try:
            while True:
                while self.remaining_time >= 0 and self.is_recording:
                    logging.info("remaining_time is: " + str(self.remaining_time))
                    self.remaining_time -= 1
                    time.sleep(1)

                if self.is_recording:
                    self.camera.stop_recording()
                    logging.info("Stop recording.")
                    self.is_recording = False

        except KeyboardInterrupt:
            logging.info("Stop countdown.")

if __name__ == '__main__':
    # Format log output
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    bc = BongjiCam()
    bc.start()

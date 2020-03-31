from picamera import PiCamera, Color
from time import sleep

class CameraControl:
    def __init__(self):
        self.camera = PiCamera()
        self.outfile = "video_test.h264"
        self.preview = False

    def rotate(self, degrees):
        self.camera.rotation = degrees

    def set_resolution(self, width, height):
        self.camera.resolution = (width, height)
    
    def set_framerate(self, framerate):
        self.camera.framerate = framerate
        
    def set_annotations(self):
        self.camera.annotate_background = Color('blue')
        self.camera.annotate_foreground = Color('yellow')
        self.camera.annotate_text = "Bongji Cam"
        self.camera.annotate_text_size = 50
    
    def set_outputfile(self, path):
        elf.outfile = path

    def start_recording(self, filename):
        if self.preview:
            self.camera.start_preview()
        self.camera.start_recording(filename)
    
    def stop_recording(self):
        if self.preview:
            self.camera.stop_preview()
        self.camera.stop_recording()

    def test(self):
        self.camera.resolution = (1080, 720)
        cc.start_recording(self.outfile)
        sleep(5)
        cc.stop_recording()

if __name__ == "__main__":
    cc = CameraControl()
    cc.test()


"""
Check camera modes: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
"""
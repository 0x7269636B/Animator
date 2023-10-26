import cv2

class PhotoGUI:
    def __init__(self):

        self.video_capture = cv2.VideoCapture(0)
        self.run = True
        # Check success
        if not self.video_capture.isOpened():
            raise Exception("Could not open video device")

    def snapshot(self,img_name="image.jpg"):

        try:
            # Read picture. ret === True on success
            ret, frame = self.video_capture.read()

            if ret:
                cv2.imshow("Camera View", frame)
            else:
                raise Exception("Could not read frame")

            key = cv2.waitKey(1)

            if key == ord("q"):
                self.video_capture.release()
                cv2.destroyAllWindows()
                self.run = False

            if key == ord("c") or key == ord("s"):
                print("Captured")
                cv2.imwrite(img_name, frame)
                
        except KeyboardInterrupt:
            self.video_capture.release()
            cv2.destroyAllWindows()
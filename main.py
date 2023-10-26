from animator import Animator
from photo_gui import PhotoGUI
import cv2

INPUT_IMAGE = "picture.jpg"
OUTPUT_VIDEO = "output_video.mp4"
IMAGE = "red_white.jpg"

# main program
try:

    # photo_gui = PhotoGUI()
    # while photo_gui.run:
    #     photo_gui.snapshot(IMAGE)

    # photo_gui.video_capture.release()
    # cv2.destroyAllWindows()

    animator = Animator(debug=True)

    paragraph = animator.get_text_v2(IMAGE)

    # sentences = animator.tokenize_sentences(paragraph)

    # animator.generate_video(sentences, OUTPUT_VIDEO, len(sentences), 1)

except KeyboardInterrupt:
    # photo_gui.video_capture.release()
    cv2.destroyAllWindows()
    print("\nKeyboard Interrupted")
    exit(0)
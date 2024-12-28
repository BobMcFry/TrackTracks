import logging
import sys
from time import sleep

from cv2 import VideoCapture, destroyWindow, imshow, waitKey
from qreader import QReader

CAM_PORT = 1
WAIT_FOR_CAM_WAKE_UP = 1
WINDOW_NAME = "Test"

# Configure logger to output to stdout
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def capture_image(cam_port: int) -> list[str] | None:
    # Initialize camera
    cap = VideoCapture(cam_port)
    if not cap.isOpened():
        logger.error(f"Failed to open camera on port {cam_port}")
        return None

    # Initialize QR reader
    qreader = QReader()

    # Wait for camera to initialize
    sleep(WAIT_FOR_CAM_WAKE_UP)

    try:
        while True:
            # Capture frame
            ret, frame = cap.read()
            if not ret:
                logger.error("Failed to capture frame. Exiting...")
                break

            # Detect and decode QR codes
            decoded_data = qreader.detect_and_decode(image=frame)
            if decoded_data:
                logger.info(f"Decoded QR codes: {decoded_data}")

            # Display frame
            imshow(WINDOW_NAME, frame)

            # Check for quit command
            if waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Clean up
        cap.release()
        destroyWindow(WINDOW_NAME)

    return decoded_data


def main():
    capture_image(CAM_PORT)


if __name__ == "__main__":
    main()

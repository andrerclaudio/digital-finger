import logging
import time

import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the LED is connected
LED_PIN = 17
HOLD_DELAY = 0.5

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def digital_finger():
    """
    Turn On and Off a given raspberry pi pin.
    :return: None
    """

    try:
        # Set up the GPIO pin as an output
        GPIO.setup(LED_PIN, GPIO.OUT)
        # Turn the LED on (0 means ON)
        GPIO.output(LED_PIN, GPIO.LOW)
        # Wait for HOLD_DELAY seconds
        time.sleep(HOLD_DELAY)
        # Turn the LED off (1 means OFF)
        GPIO.output(LED_PIN, GPIO.HIGH)
        logging.info('LED control successful!')

    except Exception as e:
        logging.exception(f"An error occurred: {e}", exc_info=False)

    finally:
        # Clean up GPIO and exit
        GPIO.cleanup()


if __name__ == '__main__':
    # Application is starting from here.
    digital_finger()

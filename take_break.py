"""
Set alarm to play a video
"""
import webbrowser
import time

def main():
    """
    test function
    :return: none
    """
    video_address = "https://youtu.be/mXAs7Nva7kc"
    # Delay "sleep"
    time.sleep(3)
    webbrowser.open(video_address)


if __name__== '__main__':
        main()
        exit(0)

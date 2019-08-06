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
    counter = 0
    while counter < 3:
        # Delay "sleep"
        time.sleep(10) # 1 hr
        webbrowser.open(video_address)
        counter +=1


if __name__== '__main__':
        main()
        exit(0)

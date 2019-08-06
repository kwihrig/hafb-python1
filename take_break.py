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
        time.sleep(60*60) # 1 hr
        webbrowser.open(video_address)
        counter +=1
        print ("it is time to take a break, it is ", time.ctime())


if __name__== '__main__':
        main()
        exit(0)

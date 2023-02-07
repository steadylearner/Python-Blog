<!--
  Post{
    subtitle: "Save audio files from videos with Python Moviepy",
    image: "/brand/Moviepy.png",
    image_decription: "Image from its website",
    tags: "Python, How, video, audio",
  }
-->

[YouTube]: https://www.youtube.com/channel/UCt_jsJOe91EVjd58kHpgTfw

[Moviepy]: https://zulko.github.io/moviepy/
[sys-env in Python]: https://stackoverflow.com/questions/4906977/how-do-i-access-environment-variables-from-python

[You can follow me at GitHub.]: https://github.com/steadylearner

[You can contact or hire me at Telegram.]: https://t.me/steadylearner

<!-- / -->

Before finding working **Python** code for the purpose of this post, I thought it would be easy to find working examples. But, it was not and that is the reason I write this post.

If I do not know how to use Python or other programming languages. I would repeatedly separate audio files, opening videos and waitng for software to separate audio clip and video clip for that.

Then, I should compile only audio files and wait for a long time unnecessarily.

But I would not do that. With the power of programming, we do not have to repeat what we already know.

Before you use the code below, please read these and install Python and pip first if you haven't yet.

The **pip** will be used to install and use [Moviepy]. 

You can install it with `$pip install moviepy`.
 
1. [How to install Python](https://realpython.com/installing-python/)

2. [How to install pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)

3. [Moviepy official website](https://zulko.github.io/moviepy/install.html)

4. [sys-env in Python]

## 1. Python Code to extract audios from the videos

I will assume you already prepared a video file with audio for this process. It is very simple and you can use the code below with it.

```python
# Create a file with 
# $touch extract_audio.py

# 1.
import sys
from moviepy.editor import *

video = VideoFileClip(sys.argv[1]) # 2.
audio = video.audio # 3.
audio.write_audiofile(sys.argv[2]) # 4.
```

You can save this code with **extract_audio.py** and test it with the command below.

```console
$python extract_audio.py <video_file> <audio_file>
```

For example, `$python extract_audio.py video_for_audio.mp4 audio_from_video.mp4`

It will make audio_from_video.mp4 file in your machine.

What we do here are

1. We import default Python **sys** module to use **sys.argv** later and **moviepy.editor** to extract audio files from videos.

2. In **video = VideoFileClip(sys.argv[1])** you instruct your machine which video file you want to use to extract audio.

3. Then, with **audio = video.audio**, you select audio file inside the video file. You can see that Python use **.** syntax for that.

4. Lastly, with **audio.write_audiofile(sys.argv[2])**, You end the process and assign the result audio file name.

and that is all you need to know to extract audio from the video with python.

The sys or sys.argv here is to help you automate your work with CLI params.

What comes first after **$python file.py** would be **sys.argv[1]** and others would be sys.argv[2] and more.

<br />

## 2. Conclusion

In this post, you learnt you don't need any software to extract an audio file from video and use Python instead.

You can find some of the example videos at [Steadylearner YouTube][YouTube] if you haven't any to test.

[You can follow me at GitHub.]

[You can contact or hire me at Telegram.]

**Thanks and please share this post with others.**

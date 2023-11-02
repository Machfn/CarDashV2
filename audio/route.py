import numpy as np
import pydub
import sounddevice as sd


def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y
    
def write(f, sr, x, normalized=False):
    """Numpy array to mp3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)

    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")


    # sr, x = read('test.mp3')
    # print(x)



def streamFr():

    frequency = 440
    fs = 44100
    seconds = 3
    # generating an array with seconds*xample_rate, steps
    t = np.linspace(0, seconds, seconds * fs, False)

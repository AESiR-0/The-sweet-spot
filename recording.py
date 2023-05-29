import emotions

def record(i, name):  
    # import required libraries
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio as wv
    from datetime import datetime
    import os 

    # Sampling frequency
    freq = 46100

    # Recording duration
    duration = int(i)

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)
                    
    # Record audio for the given number of seconds
    sd.wait()
    current_dateTime = datetime.now()
    current_time = str(current_dateTime.year)+"_"+str(current_dateTime.month)+"_"+str(current_dateTime.day)+"_"+str(current_dateTime.hour)+"_"+str(current_dateTime.minute)
    a_name=str(name)+" "+str(current_time)+".wav"
    wv.write(a_name, recording, freq, sampwidth=2)
    emo = emotions.audio_emo(a_name)
    return emo, current_time


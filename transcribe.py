import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf 
import numpy
import whisper


model =  whisper.load_model("base.en")
q  = queue.Queue()

def record(indata, frames, time, status):
  if status:
    print(status, file=sys.stderr)
  
  q.put(indata.copy())
  

def get_cmd(question):

  # device_info = sd.query_devices()
  # print(device_info)
    device_info = sd.query_devices(14, 'input')
    samplerate = int(device_info["default_samplerate"])
    # print(sf.available_formats())
    # print(sf.available_subtypes())

    print(sd.query_devices(14, 'input'))
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmpfp:
      try:
      
        with sf.SoundFile(tmpfp.name, mode="w+", samplerate=samplerate, format="WAV", channels=1) as sdfile:
          with sd.InputStream(samplerate=samplerate,channels=1, device=14, callback=record):
            print(question)
            print("press Ctrl+C")
            while True:
              sdfile.write(q.get())
      except KeyboardInterrupt:
        print('\nRecording finished: ', tmpfp.name)
        result = model.transcribe(tmpfp.name)
        return result["text"]
        # print(result["text"])




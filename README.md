# Audio logs

(This introduction was actually dictated over a microphone, and the script/Whisper transcribed it into an Text file)

2022 November 20, 20:20:49

Audio log idea

I wanted something where I can dump my thoughts as an audio and then have it transcribed and you know, you can fix it here and there and have it like a log journal. The reason is that I feel is a faster way to dump my thoughts. So I came across this library called or rather a machine learning model called Whisper from openAI and that can transcribe audio files to a very good extent. And yeah, so this is a test for that. The output is saved as a text file in a logs folder. How this works is it listens to your audio stream and until you press control C it continues to listen and once you press the control C it stops listening and writes it to a sound file and that file is passed to Whsiper and Whisper would then transcribe it to a text and send it back to be saved into the file. There are a few issues with this. The issue is that it takes time for the model to load. So even though the inference part is quicker, the time taken to load into the model causes a delay. So it's not like you can just quickly launch it and do something. So I would want for the transcription part to be separated from the part where I trigger the recording so that the transcription part could always be ready in the background as a daemon and always be running and only whenever I need the audio gets recorded and sent into the transcription. So that would be the probably the next step and I would also want not to use control C but some other way for me to indicate starting and ending of the recording. Yeah, and also maybe if possible some kind of in audio text editing for example, if I made a mistake, I should be able to say scratch that and maybe last sentence get completely scratched. It could be could be outputted as a markdown file. So all of those can be seen in line and make edit as needed. But I feel that's probably a bit more difficult and also maybe some way to you know segment the text into paragraphs that would probably make it much better to read. Yeah, so these are some of the ideas I have for this. So, just throw a script I wrote to test it for the test the capability today.

## Installation

Needs python version 3.6>

`python3 -m venv venv`

Activate the venv
`. venv/bin/activate`

Install whisper

`pip install pip --upgrade`

`pip install git+https://github.com/openai/whisper.git -q`

### GPU Support

`pip uninstall torch`

`pip cache purge`

`pip install torch==1.13.0+cu117 -f https://download.pytorch.org/whl/torch`

### Other dependencies

`pip install -r requirements.txt`

## Run

1. Create a directory called ./logs
2. `python main.py`

It starts listening for the log title - pressing CTRL+C makes it stop listening.
Then it starts listening for the content

import asyncio
import pyaudio
from google import genai
from google.genai import types

import AVA_config as config
import AVA_audio_handler as audio_handler

async def main():
    client = genai.Client(api_key=config.API_KEY)
    
    config_live = types.LiveConnectConfig(
        response_modalities=[types.Modality.AUDIO],
    )
    
    p = pyaudio.PyAudio()
    
    async with client.aio.live.connect(model=config.MODEL_NAME, config=config_live) as session:
        # Link tasks to the separate audio file functions
        streamer_task = asyncio.create_task(audio_handler.stream_microphone(session, p))
        receiver_task = asyncio.create_task(audio_handler.play_speaker(session, p))
        
        try:
            await asyncio.gather(streamer_task, receiver_task)
        except (Exception, asyncio.TimeoutError):
            print("\nSession ended.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping assistant. Goodbye!")
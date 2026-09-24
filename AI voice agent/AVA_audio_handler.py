import asyncio
import sys
from google.genai import types
import AVA_config as config

async def stream_microphone(session, p):
    """Captures microphone audio and streams it to Gemini live."""
    mic_stream = p.open(
        format=config.FORMAT,
        channels=config.CHANNELS,
        rate=config.RATE,
        input=True,
        frames_per_buffer=config.CHUNK
    )
    print("\n🎙️ Assistant is listening... Start speaking!")
    
    try:
        while True:
            data = mic_stream.read(config.CHUNK, exception_on_overflow=False)
            await session.send_realtime_input(
                audio=types.Blob(data=data, mime_type=f"audio/pcm;rate={config.RATE}")
            )
            await asyncio.sleep(0.001)
    except asyncio.CancelledError:
        pass
    finally:
        mic_stream.stop_stream()
        mic_stream.close()

async def play_speaker(session, p):
    """Receives audio response chunks from Gemini and plays them through speakers."""
    speaker_stream = p.open(
        format=config.FORMAT,
        channels=config.CHANNELS,
        rate=config.RATE,
        output=True
    )
    
    try:
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.model_turn:
                for part in server_content.model_turn.parts:
                    if part.inline_data and part.inline_data.data:
                        speaker_stream.write(part.inline_data.data)
                        sys.stdout.write("🔊")
                        sys.stdout.flush()
    except asyncio.CancelledError:
        pass
    finally:
        speaker_stream.stop_stream()
        speaker_stream.close()
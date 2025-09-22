# export_video.py
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import pyttsx3
import os

def tts_to_file(text, out_audio="assets/audio.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(text, out_audio)
    engine.runAndWait()
    return out_audio

def create_video(image_paths, narration_text, out_file="outputs/video_demo.mp4", fps=24, duration_per_image=4):
    # produce audio
    audio_path = tts_to_file(narration_text, out_audio="assets/narration.wav")
    audio_clip = AudioFileClip(audio_path)
    clips = []
    for p in image_paths:
        clip = ImageClip(p).set_duration(duration_per_image).resize(height=720)
        clips.append(clip)
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio_clip.set_duration(video.duration))
    video.write_videofile(out_file, fps=fps)
    return out_file

if __name__ == "__main__":
    create_video(["assets/thumbnails/poster.png"], "A trailer: the ship arrives at dawn...", "outputs/demo.mp4")

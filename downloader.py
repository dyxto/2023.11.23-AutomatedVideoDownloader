from pytube import YouTube
import os

# specify a destination folder
out_vid="D:\pytube\out_vid" # use "out_vid" to export to project directory
out_aud="D:\pytube\out_aud" # ...see above

links = open('links.txt', 'r')

for i, line in enumerate(links, start=1):
    try:
        if line.strip():
            url = line
            video = YouTube(url)
            print("Downloading...")
            print(url, end="")
            video.streams.get_highest_resolution().download(out_vid)
            # video.streams.filter(only_audio=True).first().download(out_aud) # no picture video file (audio only MP4)
            audio_MP4 = video.streams.filter(only_audio=True).first().download(out_aud)
            base, ext = os.path.splitext(audio_MP4)
            mp3_file = audio_MP4 + '.mp3'
            os.rename(audio_MP4, mp3_file)

            print(f" ...Done_{i}")

    except:
        print(f"ERROR: video {i} skipped. check url.\n")

# clear the LINKS FILE after download complete
# links = open('links.txt', 'w')

links.close
print("\nDownloading Complete")


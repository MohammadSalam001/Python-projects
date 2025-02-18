import yt_dlp

def download_youtube(url, choice):
    ydl_opts = {
        "outtmpl": "%(title)s.%(ext)s",  # Saves with the video title
    }

    if choice == "2":  # Audio only
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    else:  # Video (default)
        ydl_opts["format"] = "best"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("🔗 Enter YouTube URL: ")
    print("\nChoose download format:")
    print("1️⃣ Video (highest quality)")
    print("2️⃣ Audio (MP3 format)")

    choice = input("Enter your choice (1 or 2): ")
    while choice not in ["1", "2"]:
        choice = input("❌ Invalid choice. Please enter 1 or 2: ")

    download_youtube(video_url, choice)

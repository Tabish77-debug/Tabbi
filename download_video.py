import youtube_dl

def download_video_and_metadata(video_url):
    ydl_opts = {
        'format': 'best',  # Choose the best quality format
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title
        'writesubtitles': True,  # Download subtitles if available
        'writeautomaticsub': True,  # Download automatically generated subtitles if available
        'writeinfojson': True,  # Write video metadata to a .info.json file
        'writedescription': True,  # Write the video description to a .description file
        'writeannotations': True,  # Write video annotations to a .annotations.xml file
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Extract audio in MP3 format
            'preferredquality': '192',  # Audio quality
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("https://www.youtube.com/watch?app=desktop&si=f7SiwGdV11QpHqN8&v=9Lmm1IuCaIY&feature=youtu.be ")
    download_video_and_metadata(video_url)

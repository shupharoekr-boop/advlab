#pip install yt-dlp
import yt_dlp

def download_youtube(url):
    # กำหนด option สำหรับการดาวน์โหลด
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("URL YouTube: ")
    download_youtube(video_url)
    print("success")

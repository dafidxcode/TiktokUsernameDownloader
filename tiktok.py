import os, yt_dlp

def Download_TiktokVideos(tiktok_url, download_path='downloads'):
    # Memastikan lokasi unduhan 
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(uploader)s_%(upload_date)s_%(id)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,  # Memastikan semua daftar
        'extract_flat': True,  # Mengekstrak semua URL video
        'quiet': False,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Mengekstrak informasi video
        result = ydl.extract_info(tiktok_url, download=False)
        if 'entries' in result:
            # Membuat antrian unduhan dalam daftar
            video_urls = [entry['url'] for entry in result['entries']]
            print(f' Berhasil menemukan {len(video_urls)} video. Mulai unduhan ..')
            for video_url in video_urls:
                try:
                    ydl.download([video_url])
                except Exception as e:
                    print(f' -- Error mengunduh {video_url}: {e}')
        else:
            ydl.download([tiktok_url])

if __name__ == "__main__":
    print(" Masukan Username Tiktok Target (Without '@') ")
    username = input("➥ ")
    print(" Masukan Lokasi Unduhan (Default is 'Downloads') ") 
    download_directory = input("➥ ") or 'downloads'
    tiktok_url = 'https://www.tiktok.com/@' + username
    Download_TiktokVideos(tiktok_url, download_directory)
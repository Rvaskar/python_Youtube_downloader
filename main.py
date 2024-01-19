import os
from pytube import YouTube


def create_download_folder():
    folder_name = 'YouTubeDownloads'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name


def download_video_with_resolution_choice(url):
    try:
        yt = YouTube(url)
        print(f'Available video resolutions for {yt.title}:')
        for stream in yt.streams.filter(file_extension='mp4'):
            print(stream.resolution)

        resolution_choice = input("Enter the desired resolution (e.g., 1080p, 720p, etc.): ")
        video = yt.streams.filter(res=resolution_choice, file_extension='mp4').first()

        if video:
            download_folder = create_download_folder()
            print(f'Downloading video in {resolution_choice} resolution: {yt.title}')
            video.download(output_path=download_folder)
            print('Download completed!')
        else:
            print(f'No {resolution_choice} video available for {yt.title}')
    except Exception as e:
        print('Error:', str(e))


def download_audio(url):
    try:
        yt = YouTube(url)
        download_folder = create_download_folder()
        audio = yt.streams.filter(only_audio=True).first()

        if audio:
            print(f'Downloading audio: {yt.title}')
            audio.download(output_path=download_folder)
            print('Download completed!')
        else:
            print(f'No audio available for {yt.title}')
    except Exception as e:
        print('Error:', str(e))


if __name__ == "__main__":
    while True:
        url = input("Enter the YouTube video URL: ")
        download_choice = input("Enter 'V' to download video, 'A' to download audio, or 'B' to download both: ")

        if download_choice.upper() == 'V':
            download_video_with_resolution_choice(url)
        elif download_choice.upper() == 'A':
            download_audio(url)
        elif download_choice.upper() == 'B':
            download_video_with_resolution_choice(url)
            download_audio(url)
        else:
            print("Invalid choice. Please enter 'V', 'A', or 'B'.")

        choice = input("Do you want to download another video? (y/n): ")
        if choice.lower() != 'y':
            break

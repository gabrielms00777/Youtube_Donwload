from pytube import Playlist, YouTube

def download_audio(url):
    yt = YouTube(url)
    res = yt.streams.filter(type='audio', mime_type='audio/mp4', only_audio=True).first()
    res.download()
    return res.title


def download_playlist(url:str):
    yt = Playlist(url)
    for audio in yt.videos:
        print(audio.streams.filter(type='audio', mime_type='audio/mp4', only_audio=True).first())





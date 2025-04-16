import yt_dlp

youtube_links = [
    "https://youtu.be/TEh1gyFGgfI",
    "https://youtu.be/Nb-7PrqW-tM",
    "https://youtu.be/pTFIvfuRDe4",
    "https://youtu.be/ddoj7KUN-WU",
    "https://youtu.be/DYZBu9jdZbU",
    "https://youtu.be/dW8VpYKwltE",
    "https://youtu.be/MrTu3ndnoAo",
    "https://youtu.be/sWeUJITORko",
    "https://youtu.be/aHTuCsAFUpM",
    "https://youtu.be/uQVoXKmlqFM",
    "https://youtu.be/_ocb1UDflbE",
    "https://youtu.be/foHLbGR1atk",
    "https://youtu.be/H5fjE2LDLeU",
    "https://youtu.be/zGEsqmNKSeE",
    "https://youtu.be/IBKmTbRmHI4",
    "https://youtu.be/bvyPuJI7rFU",
    "https://youtu.be/JeEUFfHoYVw",
    "https://youtu.be/v3GeWvqx-C4",
    "https://youtu.be/jP6tNR65wF4",
    "https://youtu.be/r_ieNWukEDI",
    "https://youtu.be/tZNCOYSbgiw",
    "https://youtu.be/b9t-ZxGDJBI",
    "https://youtu.be/v8AEivzb6Ng",
    "https://youtu.be/u36HnG0-bBY",
    "https://youtu.be/9zlsX7RGPnc",
    "https://youtu.be/nJwOhuIl5x4",
    "https://youtu.be/wv_62WiuUgQ",
    "https://youtu.be/_LRGcONgoxY",
    "https://youtu.be/iobG3_FQll0",
    "https://youtu.be/DvV7xWMIjQc",
    "https://youtu.be/IyrCML0cwMk",
    "https://youtu.be/2OYJPNEZhBY"
]

for link in youtube_links:
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
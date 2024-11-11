import os
import sys
import re
import logging
from yt_dlp import YoutubeDL

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/app/logs/download.log')
    ]
)

logger = logging.getLogger(__name__)

# For single-line progress updates
class SingleLineProgress:
    def __init__(self):
        self.last_length = 0

    def update(self, message):
        # Clear the previous line
        sys.stdout.write('\r' + ' ' * self.last_length + '\r')
        sys.stdout.write(message)
        sys.stdout.flush()
        self.last_length = len(message)

progress_display = SingleLineProgress()

def validate_youtube_url(url):
    """Validate YouTube URL or video ID"""
    if not url:
        return None

    youtube_id_pattern = r'(?:(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})|^([a-zA-Z0-9_-]{11})$)'

    match = re.search(youtube_id_pattern, url)
    if match:
        video_id = match.group(1) or match.group(2)
        if video_id:
            if len(url) == 11:
                return f"https://www.youtube.com/watch?v={url}"
            return url

    return None

def get_ydl_opts(format_type='video'):
    """Get yt-dlp options from environment variables or use defaults"""
    if format_type == 'audio':
        format_spec = 'bestaudio/best'
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        format_spec = os.getenv('FORMAT', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best')
        postprocessors = [{
            'key': 'FFmpegEmbedSubtitle',
            'already_have_subtitle': False,
        }, {
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        }]

    return {
        'format': format_spec,
        'outtmpl': '/app/data/%(channel)s/%(title)s/%(title)s.%(ext)s',
        'download_archive': os.getenv('DOWNLOAD_ARCHIVE'),
        'restrictfilenames': True,
        'no_warnings': False,
        'ignoreerrors': True,
        'verbose': True,
        'progress_hooks': [logging_hook],
        'ffmpeg_location': '/usr/bin/ffmpeg',
        'writethumbnail': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'postprocessors': postprocessors
    }

def download_video(url, format_type='video'):
    """Download video using yt-dlp with error handling and logging"""
    validated_url = validate_youtube_url(url)
    if not validated_url:
        logger.error(f"Invalid YouTube URL or video ID: {url}")
        logger.info("Please provide a valid YouTube URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
        logger.info("Or a valid video ID (e.g., dQw4w9WgXcQ)")
        return False

    ydl_opts = get_ydl_opts(format_type)

    try:
        with YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Starting download for: {validated_url}")
            ydl.download([validated_url])
            logger.info(f"Successfully downloaded: {validated_url}")
            return True
    except Exception as e:
        logger.error(f"Error downloading {validated_url}: {str(e)}")
        return False

def logging_hook(d):
    if d['status'] == 'downloading':
        _percent = d.get('_percent_str', '0%')
        _speed = d.get('_speed_str', 'N/A')
        _eta = d.get('_eta_str', 'N/A')
        progress_message = f"Downloading: {d['filename']} - {_percent} at {_speed} ETA: {_eta}"
        progress_display.update(progress_message)
    elif d['status'] == 'finished':
        progress_display.update(f"Download complete: {d['filename']}\n")
        logger.info(f"Download complete: {d['filename']}")

def main():
    url = os.getenv('VIDEO_URL')
    format_type = os.getenv('FORMAT_TYPE', 'video')  # 'video' or 'audio'

    if not url:
        logger.error("No VIDEO_URL provided")
        print("""
Usage: Please provide a VIDEO_URL in your .env file or when running the container:

docker-compose run -e VIDEO_URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ" -e FORMAT_TYPE="video" yt-dlp

Or update your .env file with:
VIDEO_URL=https://www.youtube.com/watch?v=dQw4w9WgXcQ
FORMAT_TYPE=video  # or 'audio' for MP3

You can also use:
- Short URL: https://youtu.be/dQw4w9WgXcQ
- Video ID: dQw4w9WgXcQ
        """)
        sys.exit(1)

    success = download_video(url, format_type)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

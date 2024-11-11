# kev1njodea/dockerfiles/yt-dlp

- https://github.com/yt-dlp/yt-dlp
- https://pypi.org/project/yt-dlp

## Overview

Dockerized version of `yt-dlp`, a feature-rich command-line audio/video downloader. Includes custom [yt-dlp.py](files/yt-dlp.py) script.

## Getting Started

### Build image

- `docker compose build`
or
- `docker compose build --no-cache`

## Customizing the Setup

### Volumes

The `docker-compose.yml` file maps the local `./data` directory to `/app/data` in the container.
You can adjust this volume mapping if you need to store files in a different location.

### Environment Variables

```bash
# .env
# Single video URL
VIDEO_URL=https://www.youtube.com/watch?v=xxxxxxxxxxx
FORMAT_TYPE=audio
```

`FORMAT_TYPE` parameter can be either `audio` or `video`.

When set to `audio`, it uses:

- Best audio quality format
- FFmpeg to convert to MP3 at 192kbps
- Maintains metadata

### Begin download

- `docker compose up`

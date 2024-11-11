# Base image
FROM python:3.13.0-slim-bookworm

# User Arguments
ARG USERNAME=ytdlp
ARG USER_UID=1002
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Set working directory
WORKDIR /app

# Install system dependencies and clean up in the same layer to reduce image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY --chown=$USER_UID:$USER_GID ./files/requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=$USER_UID:$USER_GID ./files/yt-dlp.py .

# Create and set permissions for download directory
RUN mkdir -p /app/data && chown -R $USER_UID:$USER_GID /app/data

# Switch to non-root user
USER $USER_UID

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Healthcheck to ensure the container is running properly
# HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
#     CMD python -c "import yt_dlp; print('healthy')" || exit 1

# Set default command to run yt-dlp
CMD ["python", "yt-dlp.py"]

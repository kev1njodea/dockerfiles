# Set the base image and version
FROM baseImage1:latest

# Update packages, install packages, and clean up
RUN apt-get update \
    && apt-get install -y \
        package1 \
        package2 \
    && rm -rf /var/lib/apt/lists/*

# # User Arguments
# ARG USERNAME=user
# ARG USER_UID=1001
# ARG USER_GID=$USER_UID
#
# # Create the user
# RUN groupadd --gid $USER_GID $USERNAME && \
#     useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
#
# # Copy data from host to container
# COPY --chown=$USER_UID:$USER_GID ./files/ /home/$USERNAME/
#
# # Switch to the new user
# USER $USERNAME

# Copy data from host to container
COPY files /path

# Set the containers working directory
WORKDIR /path

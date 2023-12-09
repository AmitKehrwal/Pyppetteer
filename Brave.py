import subprocess

# Install curl
subprocess.run(["apt", "install", "curl", "-y"])

# Download Brave keyring with curl
subprocess.run(["curl", "-fsSLo", "/usr/share/keyrings/brave-browser-archive-keyring.gpg", "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"])

# Add Brave repository to sources.list
subprocess.run(["echo", "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main", ">", "/etc/apt/sources.list.d/brave-browser-release.list"])

# Update apt
subprocess.run(["apt", "update"])

# Install Brave browser
subprocess.run(["apt", "install", "brave-browser"])

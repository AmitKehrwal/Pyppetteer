import subprocess

# Install wget
subprocess.run(["apt", "install", "wget", "-y"])

# Install webdriver_manager
subprocess.run(["pip", "install", "webdriver_manager"])

# Upgrade webdriver_manager
subprocess.run(["pip", "install", "--upgrade", "webdriver_manager"])

# Install pyppeteer
subprocess.run(["pip", "install", "pyppeteer"])

# Install pyppeteer_stealth
subprocess.run(["pip", "install", "pyppeteer_stealth"])

# Install getindianname
subprocess.run(["pip", "install", "getindianname"])

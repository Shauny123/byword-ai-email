import os
import subprocess

def is_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

def install_packages(packages):
    if is_colab():
        for pkg in packages:
            subprocess.run(["pip", "install", pkg])
    else:
        with open("requirements.txt", "w") as f:
            f.write("\n".join(packages))
        print("✅ requirements.txt written. Run: pip install -r requirements.txt")

packages = [
    "fastapi",
    "uvicorn[standard]",
    "pydantic",
    "sendgrid",
    "python-dotenv",
    "google-api-python-client",
    "google-auth-httplib2",
    "google-auth-oauthlib"
]

install_packages(packages)

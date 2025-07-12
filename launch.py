import subprocess
import webbrowser
import time
import os

# 🔥 Launch Flask app
subprocess.Popen(["python", "main.py"])

# ⏳ Give it a few seconds to start
time.sleep(2)

# 🌐 Open index.html in browser
webbrowser.open(f"file://{os.path.abspath('index.html')}")

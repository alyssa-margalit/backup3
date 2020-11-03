import subprocess
player = subprocess.Popen(["mplayer", "forest.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
player.stdin.write("q")
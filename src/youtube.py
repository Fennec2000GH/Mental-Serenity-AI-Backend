
import urllib.request
import re

search_keyword="mozart"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

for video_id in video_ids:
	print("https://www.youtube.com/watch?v=" + video_id)

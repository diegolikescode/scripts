import webbrowser

hour = 1
minute = 25
total_seconds = ((hour * 60) + minute) * 60
video_link = "https://www.youtube.com/watch?v=sCE-fQJAVQ4&t={}s&ab_channel=DappUniversity".format(total_seconds) 

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(video_link)

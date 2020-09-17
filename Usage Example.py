from youtubesearchpython import SearchVideos, SearchPlaylists

videos = SearchVideos("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)
videosResult = videos.result()
print(videosResult)

playlists = SearchPlaylists("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)
playlistsResult = playlists.result()
print(playlistsResult)

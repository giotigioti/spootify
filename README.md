# Spootify
## A guide on how to download spotify songs after the api change
* set this as an alias so you don't have to type it every time ` yt-dlp -x --audio-format mp3 --embed-metadata --embed-thumbnail -o "%(title)s.%(ext)s" `
* go to [exportify](https://exportify.net/) to export your csv file for your playlist
* go to [tunemymusic](https://www.tunemymusic.com/) to transfer a spotify playlist to youtube music
* run the alias you set earlier
* run the attached python script to convert the csv to m3u for ncmpcpp using the default of 1 for the title names so ncmpcpp can recognize them

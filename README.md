# Spootify
## A guide on how to download spotify songs after the api change
* set this as a alias so you dont have to type it everytime yt-dlp -x --audio-format mp3 --embed-metadata --embed-thumbnail -o "%(title)s.%(ext)s"
*  go to [exportify](https://exportify.net/) to export your csv file for your playlist
*  go to [tunemymusic](https://www.tunemymusic.com/) to transfer a spotify playlist to youtube music
*  run the alias you set earlier
*  run the attached python script to convert the csv to m3u for ncmpcpp
* use the default off 1 for the title names for ncmcpp

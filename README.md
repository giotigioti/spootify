# Spootify
## A guide on how to download spotify songs after the api change
set this alias to something so you dont have to type it everytime yt-dlp -x --audio-format mp3 --embed-metadata --embed-thumbnail -o "%(title)s.%(ext)s"
go to https://exportify.net/ to export your csv file for your playlist
go to https://www.tunemymusic.com/ to transfer a spotify playlist to youtube
run the alias you set earlier
run the attached pythin script to convert the csv to m3u for ncmpcpp

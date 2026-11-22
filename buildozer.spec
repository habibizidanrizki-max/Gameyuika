[app]
title = Game Yuika
package.name = gameyuika
package.domain = com.zidan.gameyuika
source.dir = .
source.include_exts = py,png,jpg,mp3,wav
version = 0.1
requirements = python3,pygame
orientation = landscape
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
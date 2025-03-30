import os

def download_video(link, filename, thumbnail):
    print(f"\nVideo Details:\nLink: {link}\nFilename: {filename}\nThumbnail: {thumbnail}\n")
    proceed = input("Do you want to proceed with this video? (y/n): ").strip().lower()
    
    command = f"ffmpeg -i '{link}' -vf 'scale=-1:360' -c:a copy '{filename}.mp4'"
    os.system(command)
    print(f"Downloaded: {filename}.mp4")


video_list = [
"/yl https://madxabhi-pw.onrender.com/89b5b411-8f2f-4319-a525-5a31507d76c4/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 01 : Divisibility Tests -t https://static.pw.live/5eb393ee95fab7468a79d189/71fd1a76-0a8d-4baf-ad4a-948ee66b8c37.png",
"/yl https://madxabhi-pw.onrender.com/35305295-d16c-4efc-b23b-c212ee1b869c/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 02 : Division algorithm -t https://static.pw.live/5eb393ee95fab7468a79d189/a6df1e86-18c6-438e-bcd4-f30ed1d95fcb.png",

"/yl https://madxabhi-pw.onrender.com/533a76b0-4677-4325-960a-7a12bde6810c/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 03 - Euclidean Algorithm  Rishi sir  7pm -t https://static.pw.live/5eb393ee95fab7468a79d189/32a796dc-aa97-480b-9cf1-72a1e45fcd24.png",
"/yl https://madxabhi-pw.onrender.com/1d84a533-ec18-4417-90eb-e43a62b4171b/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 04 - Fundamental Theorem of arithmetic. Rishi sir -t https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/f1898c3d-10b0-4477-b607-0f46edd90771.png",
"/yl https://madxabhi-pw.onrender.com/a3ba0a1d-f1e0-4653-bf79-b0c7b07001a2/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n GCD Rishi Sir -t https://static.pw.live/5eb393ee95fab7468a79d189/f8711b86-f9b2-4df4-8a0f-12a2d33c7c5b.png",
"/yl https://madxabhi-pw.onrender.com/bc2bd197-acf2-4b03-ab9d-6cee5a4bd525/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 06 : LCM (IOQM 2024) -t https://static.pw.live/5eb393ee95fab7468a79d189/04d6fe96-a070-4193-857a-7bb3c4035423.png",
"/yl https://madxabhi-pw.onrender.com/1fe8b4c7-7555-401a-8ebb-e661613e87fb/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 07 - prime numbers 25/11 -t https://static.pw.live/5eb393ee95fab7468a79d189/91d5f5ec-1d83-410f-a643-4a0d316f1956.png",
"/yl https://madxabhi-pw.onrender.com/53708928-9350-4c2d-81b2-358d28a5c6b7/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 08 : Composite Numbers -t https://static.pw.live/5eb393ee95fab7468a79d189/2e335f4a-3393-4931-aa47-80c920037903.png",
"/yl https://madxabhi-pw.onrender.com/8883c5a6-9569-4a71-aca8-181e3375725b/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 09 - Modulus Function 01/12 -t https://static.pw.live/5eb393ee95fab7468a79d189/4bfe0254-5bb0-4fe1-9db4-fa4c8d8f7f85.png",
"/yl https://madxabhi-pw.onrender.com/962b0e3e-af59-4a66-8130-c0d854984840/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 10 : GIF | FPF comp -t https://static.pw.live/5eb393ee95fab7468a79d189/c092ab2a-68ff-44f1-a58d-949e0db2cfce.png",
"/yl https://madxabhi-pw.onrender.com/7f99e282-701b-452d-b014-24019da579ac/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 11 - Congruence 05/12 -t https://static.pw.live/5eb393ee95fab7468a79d189/681c0789-83a7-4097-b59a-4d3c7021d6e2.png",
"/yl https://madxabhi-pw.onrender.com/48e4c062-8129-46ac-975e-ec28833dddc7/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Ioqm number theory 07/12/2023 -t https://static.pw.live/5eb393ee95fab7468a79d189/3357d81b-162c-42a7-85b5-3ef6860297fb.png",
"/yl https://madxabhi-pw.onrender.com/a9983e25-22ec-4de6-8e55-9b890f073706/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n IOQM number theory 13 08/12/23 -t https://static.pw.live/5eb393ee95fab7468a79d189/086a8644-b323-48be-b346-1f148dcdbd38.png",
"/yl https://madxabhi-pw.onrender.com/39a16ef0-83a6-49d0-beaf-bb61b5e5544c/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Ioqm 2024 12/2024 lec -t https://static.pw.live/5eb393ee95fab7468a79d189/3e7112e3-e50a-4d60-a0cc-e4ee5298473c.png",
"/yl https://madxabhi-pw.onrender.com/ebe59c8d-cf85-4a38-9077-a04ee3b0bd86/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 15 : Chinese Remainder Theorem -t https://static.pw.live/5eb393ee95fab7468a79d189/064c3129-fcfc-46b6-b010-a4ceb770df1c.png",
"/yl https://madxabhi-pw.onrender.com/8d6cf5fc-114e-4597-831e-f30dc71bb691/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 16 : Number Theoretic Functions -t https://static.pw.live/5eb393ee95fab7468a79d189/0af68b7d-4fdb-4417-baa6-df0eea9c4840.png",
"/yl https://madxabhi-pw.onrender.com/d1df7259-9628-4241-849e-23b5a825f65e/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory 17 : Base System -t https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/e836b46f-7cec-4064-8623-f080f8076e8d.png",
"/yl https://madxabhi-pw.onrender.com/b5b10943-4291-43b8-82b0-227bad6535bb/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n Number Theory lec 18 Diophantine Equation -t https://static.pw.live/5eb393ee95fab7468a79d189/3d6eb8c0-78c2-414a-a20c-5ae860d6c892.png",
"/yl https://madxabhi-pw.onrender.com/7665db74-11b7-4e88-9dc8-5de8105cd715/master.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM4NjI3NDkuODk0LCJkYXRhIjp7Il9pZCI6IjY1ZTE4OTA2ZDFlMTcxMjAwOWFhY2FkNCIsInVzZXJuYW1lIjoiOTc3Mjk0NTI0NiIsImZpcnN0TmFtZSI6IlNhdXJhYmgiLCJsYXN0TmFtZSI6Ikt1bWFyIFNoYXJtYSBLdW1hciBTaGFybWEiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhLnN0YXR1cy55dC5vZmZpY2lhbEBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3NDMyNTc5NDl9.-gPJ0TnFgE32MZhSFM9qf-0UbMsrcPuT5ghc3vss1yY -n number theory lec 19 practice session -t https://static.pw.live/5eb393ee95fab7468a79d189/da881f16-5ade-4e95-aa1b-f3d7c6b7d9d2.png"
]

for item in video_list:
    parts = item.split(" ")
    link = parts[1]
    filename = parts[3]
    thumbnail = parts[5]
    download_video(link, filename, thumbnail)

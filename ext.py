extension = input("What's the name of the file? ").lower().strip()

if extension.endswith('.jpg') or extension.endswith('.jpeg'):
    print("image/jpeg")
elif extension.endswith('.tif') or extension.endswith('.tiff'):
    print("image/tiff")
elif extension.endswith('.gif'):
    print("image/gif")
elif extension.endswith('.pdf'):
    print("application/pdf")
elif extension.endswith('.zip'):
    print("application/zip")
elif extension.endswith('.txt'):
    print("text/plain")
elif extension.endswith('.png'):
    print("image/png")
elif extension.endswith('.apng'):
    print("image/apng")
elif extension.endswith('.avif'):
    print("image/avif")
elif extension.endswith('.bmp'):
    print("image/bmp")
elif extension.endswith('.mp3'):
    print("audio/mpeg")
elif extension.endswith('.mp4'):
    print("video/mp4")
elif extension.endswith('.php'):
    print("application/x-httpd-php")
elif extension.endswith('.webp'):
    print("image/webp")
elif extension.endswith('.xml'):
    print("application/xml")
else:
    print("application/octet-stream")

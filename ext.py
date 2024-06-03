extension = input("What's the name of the file? ").lower().strip()
print(extension)

if '.jpg' in extension or extension.endswith('.jpeg'):
    print("image/jpg")
elif '.gif' in extension:
    print("image/gif")
elif '.pdf' in extension:
    print("application/pdf")
elif '.zip' in extension:
    print("application/zip")
elif '.txt' in extension:
    print("application/txt")
else:
    print("application/octet-stream")

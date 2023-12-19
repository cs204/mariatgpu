input = input("File name: ")

allowed_extensions = ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip")
mime_to_ext = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

file_ext: str = input.split(".")[-1]

if file_ext in allowed_extensions:
    print(mime_to_ext[file_ext])

filename = input("File name: ").strip().lower()
if filename .endswith(".gif"):
    print("image/gif")
elif filename .endswith(".jpg"):
    print("image/jpeg")
elif filename .endswith(".jpeg"):
    print("image/jpeg")
elif filename .endswith(".png"):
    print("image/png")
elif filename .endswith(".pdf"):
    print("document/pdf")
elif filename .endswith(".txt"):
    print("text/plain")
elif filename .endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
import os
import shutil



doc = (".odt", ".doc", ".docx", ".pdf") 


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")


video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")




def is_documents(file):
    return os.path.splitext(file)[1] in doc

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()



os.chdir("/home/franz/Escritorio/Electronexuz")  ## os no admite valores numericos

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "/home/franz/Escritorio/Electronexuz/audio")
    elif is_video(file):
        shutil.move(file, "/home/franz/Escritorio/Electronexuz/video")
    elif is_documents(file):
        shutil.move(file, "/home/franz/Escritorio/Electronexuz/documents")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "/home/franz/Escritorio/Electronexuz/screenshots")
        else:
            shutil.move(file, "/home/franz/Escritorio/Electronexuz/images")
    else:
        shutil.move(file, "/home/franz/Escritorio/Electronexuz/Ordenado")

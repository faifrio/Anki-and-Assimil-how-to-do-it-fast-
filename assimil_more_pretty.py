import sys
from os import listdir
from shutil import copyfile

path_in = str(sys.argv[1])
path_out = str(sys.argv[2])

lesson_folders = listdir(path_in)
lesson_folders = sorted(lesson_folders)
for folder in lesson_folders:
    if folder[0] == "L":
        path = path_in + folder + "/"
        files_folder = listdir(path)
        files_folder = sorted(files_folder)

        row_list = []
        for audio in files_folder:
            if audio[0] == "S" and "00" not in audio:
                copyfile(path + audio, path_out + folder[:4] + "-" + audio)
                print(path + audio, path_out + folder[:4] + "-" + audio)

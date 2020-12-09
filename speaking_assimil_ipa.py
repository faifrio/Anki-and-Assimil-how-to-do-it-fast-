import eyed3
import sys
from os import listdir
import csv
import epitran

epi = epitran.Epitran('eng-Latn')  # <--------

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
        lesson = folder[:4]
        for audio in files_folder:
            if audio[0] == "S" and "00" not in audio:
                audiofile = eyed3.load(path + audio)

                name_mp3 = "[sound:" + lesson + "-" + audio + "]"
                sentence = audiofile.tag.title[4:]
                info = lesson + "-" + audio[:-4]
                epi_text = epi.transliterate(sentence)

                row_list.append([sentence, name_mp3 + " " + info, epi_text])

        print(row_list)

        with open(path_out + lesson + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

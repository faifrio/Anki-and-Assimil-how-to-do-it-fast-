From this post: https://www.reddit.com/r/languagelearning/comments/k9rj73/anki_and_assimil_how_to_do_it_fast_tutorial/

# Anki and Assimil, how to-do it fast

Assimil + Anki is a great combination. The problem is that creating the cards one by one for each dialogue is very slow. I want to share a little tutorial to create all flashcards at once. The idea is to create CSV files to be imported from Anki. Three types of CSVs to practice: translate, speaking, listen. Here we go:

## Step 0: get the software that we need

1. Install Python ([tutorial](https://realpython.com/installing-python/#how-to-check-your-python-version-on-windows)). Python is a programming language.
2. Install PIP ([tutorial](https://www.w3schools.com/python/python_pip.asp)). PIP is a package manager for Python packages.
3. Install eyeD3 ([link](https://pypi.org/project/eyeD3/)). eyeD3 is a Python tool for working with audio files, specifically MP3 files containing ID3 metadata (i.e. song info).
4. Download Python scripts: [GitHub](https://github.com/faifrio/Anki-and-Assimil-how-to-do-it-fast-) or [Drive](https://drive.google.com/drive/u/1/folders/1JzR8-K-TCTEIQ_ey4j9KYeAszkNKPJ1S)

## Step 1: rename and add the audios to Anki

These are the files Assimil delivers. Those framed in yellow belong to the dialogues of the lesson.

[image](https://i.imgur.com/SAopzZ2.png)

Note:

>This works for English. I don't know if the codes that Assimil uses (L001 for the first lesson, S01 for the first audio) are the same in all languages. If it is not the same in your files, you have to change the following lines by opening each script (with any text editor):  
>  
>In `if folder [0] == "L":` change the **L** for the first letter of the lesson code (in my case **L**001)  
>  
>In `if audio [0] == "S" and "00"* not in audio:`  change the **S** to the letter of the audios of the sentences (in my case **S**01)

We run the first script ([how to run your python scripts](https://realpython.com/run-python-scripts/)) to change the name and location of these files. We open a terminal in the folder where we have downloaded it and write:

`python3 assimil_more_pretty.py path-to-your-assimil-mp3 path-to-new-folder`

For example:

`python3 assimil_more_pretty.py /home/mike/english/assimil-mp3/ /home/mike/english/pretty_assimil`

&#x200B;

The result is a new folder with the following content:

[image](https://i.imgur.com/NZiEjJk.png)

&#x200B;

So each file has a unique and easy name. This is good for two reasons:

1. We can save the files in the Anki media folder, and we can access them from the flashcards.
2. We are going to add a field to each flashcard created later to be able to consult the book if there is any doubt.

So that Anki can use the audios we have to put them in its `collection.media` folder. The directory depends on your operating system, [check yours here](https://superuser.com/a/1480369).

[image](https://i.imgur.com/m0e47gG.png)

## Step 2: generate the CSVs

## listening files

Flashcard idea:

* front: audio
* reverse: the sentence command

&#x200B;

command:

`python3 listening_assimil.py path-to-your-assimil-mp3 path-to-new-folder for example`

example:

`python3 listening_assimil.py /home/mike/english/assimil-mp3/ /home/mike/english/listening`

&#x200B;

The ouput will be multiples csv with the columns:

1. code for anki to play the audio
2. sentence
3. reference to the lesson

[image](https://i.imgur.com/5owQ45e.png)

## translate files

Flashcard idea:

* front: text in your native language
* reverse: your translation

command:

`python3 translate_assimil.py path-to-your-assimil-mp3 path-to-new-folder`

example:

`python3 translate_assimil.py /home/mike/english/assimil-mp3/ /home/mike/english/translate`

&#x200B;

This time the first column is empty to be able to write the translation into your native language.

[image](https://i.imgur.com/LoVnpnm.png)

## speaking files

Flashcard idea: read the text aloud and then compare yourself to the audio.

command:

`python3 speaking_assimil.py path-to-your-assimil-mp3 path-to-new-folder`

example:

`python3 speaking_assimil.py /home/mike/english/assimil-mp3/ /home/mike/english/speaking`

## Step 3: import and enjoy

To import a file to Anki (File→Import). I recommend doing the lesson of the day. Add the translation in the corresponding csv. Import the lesson csv and start with Anki.

# Extra: IPA (International Phonetic Alphabet).

If you want to add a column to each csv with the international phonetic transcription. Like this:

[image](https://i.imgur.com/NKy4siJ.png)

You have to [install epitran](https://pypi.org/project/epitran/) just like you did with eyeD3. Open the scripts (with any text editor) and modify line 7:

`epi = epitran.Epitran('eng-Latn')`

Changing `eng-Latin` by the code of your target language (which you can find in the section "Transliteration Language/Script Pairs" of [this page](https://pypi.org/project/epitran/)) ​ ​

&#x200B;

&#x200B;

P.S: thanks to u/Blancolanda for helping me bring this to reddit

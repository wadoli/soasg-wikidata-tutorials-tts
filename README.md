# soasg-wikidata-tutorials-tts

## What's in this repository?

This repository contains the text to speech material created at the [Tutorial Factory](https://hack.glam.opendata.ch/project/61) at the [#GLAMhack2021](http://make.opendata.ch/wiki/event:2021-04) for the Wikidata tutorials for the [Sum Of All Swiss GLAMs project](https://glam.opendata.ch/sum-of-all-swiss-glams/).

**Project Team (and authors of the text in the SSML-files):**
- Annina Clara Engel
- Alicia Fagerving
- Sarah Fuchs
- Valérie Hashimoto
- Oliver Waddell
- Nicolai Wenger 

The generated audio will be published as spoken commentary to the presentations on the website https://tutorials.schoolofdata.ch/.

## What's in it for me?

I put this up so you can easily create speech audio for your projects. Namely, feel free to grab any of the tutorials on https://tutorials.schoolofdata.ch/ in the language that suits you, translate the slides and the slide notes and generate the audio to go with it in one of the [languages Google's Cloud Text-to-Speech service supports](https://cloud.google.com/text-to-speech/docs/voices). Then upload it back to https://tutorials.schoolofdata.ch/ to have it published on the website and support GLAMs with using Wikidata!

Some notes on how to get the audio:
- For good results you should mark up the text you want spoken with [Speech Synthesis Markup Language (SSML)](http://www.w3.org/TR/speech-synthesis11/), have a look at the files in the [folder "ssml"](https://github.com/wadoli/soasg-wikidata-tutorials-tts/tree/master/ssml) to see some examples
- If you want to use Google Cloud with Python like we did, have a look at their [documentation](https://cloud.google.com/text-to-speech/docs), especially the [quickstart document on how to use the client libraries](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries) (don't forget to set the environment variable GOOGLE_APPLICATION_CREDENTIALS) and the [code sample to read SSML](https://cloud.google.com/text-to-speech/docs/samples/tts-synthesize-ssml-file#python) (you might want to consider using [Poetry](https://python-poetry.org/) to manage the required dependencies)
- If you want to do it the way we did, have a look at the file [filenames_tts_python_calls.ods](filenames_tts_python_calls.ods) that generates the filenames and the calls to create the audio and the file [synthesize_text.py](synthesize_text.py), in which you can simply append the calls to create the actual audio.

Good luck!, *Oliver*
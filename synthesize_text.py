from google.cloud import texttospeech

# the following code is copied from https://cloud.google.com/text-to-speech/docs/create-audio#ssml
# with minor modifications by Oliver Waddell for the Wikidata Tutorial Factory @ #GLAMhack2021
#
# Original copyright notice 
# from https://github.com/googleapis/python-texttospeech/blob/master/samples/snippets/synthesize_text.py :
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def synthesize_ssml(ssml, langcode, voicename, ssmlgender, output_filename):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code=langcode,
        name=voicename,
        ssml_gender=ssmlgender,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file',output_filename,'.')


def file_to_string(path):
    with open(path) as file:
        return str(file.read())

# sample calls to create the audio for one presentation
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide01.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide01.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide02.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide02.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide03.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide03.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide04.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide04.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide05.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide05.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide06.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide06.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide07.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide07.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide08.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide08.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide09.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide09.mp3")
synthesize_ssml(ssml=file_to_string("01_create_account_script_ssml_fr_slide10.xml"),langcode="fr-FR",voicename="fr-FR-Wavenet-E",ssmlgender=texttospeech.SsmlVoiceGender.FEMALE,output_filename="01_create_account_audio_fr_slide10.mp3")

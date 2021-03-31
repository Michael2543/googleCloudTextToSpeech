
"""Google Cloud Text-To-Speech API sample application .
Example usage:
python quickstart.py
"""

#This code uses the Text-to-speech API sample application
#It adds a way to name the outfile and uses code to avoid the max-char Limit from Google Cloud TTS.
#The programm also parses a txt File.
#Befor using you should have a look on your encoding
import os


#Point with this line on your auth file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Micha/OneDrive/Dokumente/Code/Google Cloud/TextSpeech.json"

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()
textInput = ""
OString = ""

#A counter variable. This variable helps to create a new file on prgrammstart and extend it during the runtime.
c = 0

#Creating a Filename:
print("Please enter a name for the output file.")
bucket = input() + ".mp3"

#Open the file and parse the input to a variable
with open ("input.txt", encoding='utf-8', mode = "r") as input:
    textInput = input.readlines()
    print(textInput)
    
    #
    for line in textInput:
      line = line.strip()
      OString = OString + " " + line 
      print(len(OString))
      if len(OString) > 4500:
          c += 1
          print(len(OString))
          # Set the text input to be synthesized
          synthesis_input = texttospeech.types.SynthesisInput(text= OString)

          # Build the voice request, select the language code("de-DE") and the ssml
          # voice gender ("male")
          voice = texttospeech.types.VoiceSelectionParams(
          language_code='de-DE',
          name='de-DE-Wavenet-E',
          ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

        # Select the type of audio file you want returned
          audio_config = texttospeech.types.AudioConfig(
          audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
          response = client.synthesize_speech(
          input_=synthesis_input, voice=voice, audio_config=audio_config
          )
        # The response's audio_content is binary.
          if c == 1:
              with open(bucket, 'wb') as out:
              # Write the response to the output file.
                  out.write(response.audio_content)
              print('Audio content written to file "output.mp3"')
          else:
              with open(bucket, 'ab') as out:
            # Write the response to the output file.
                  out.write(response.audio_content)
              print('Audio content written to file "output.mp3"')
          #emptys the string variable
          OString = ""
        
    c += 1
    print(len(OString))
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text= OString)

    # Build the voice request, select the language code("de-DE") and the ssml
    # voice gender ("male")
    voice = texttospeech.types.VoiceSelectionParams(
    language_code='de-DE',
    name='de-DE-Wavenet-E',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
    input_=synthesis_input, voice=voice, audio_config=audio_config
          )
        # The response's audio_content is binary.
    if c == 1:
        with open(bucket, 'wb') as out:
    # Write the response to the output file.
            out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    else:
        with open(bucket, 'ab') as out:
    # Write the response to the output file.
            out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

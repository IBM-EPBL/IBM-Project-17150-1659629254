from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('RnoqF739Lb5BbgnUDYehER97eEjqPVZ98QhpGelXNKbq')
text_to_speech = TextToSpeechV1( authenticator=authenticator
)
text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/f60eb2cf-126a-4812-baf3-1a3eb7324f54')
with open('hello_world.wav', 'wb') as audio_file: audio_file.write( text_to_speech.synthesize(
'its time to take dolo650',
 
voice='en-US_AllisonV3Voice', accept='audio/wav'
).get_result().content) 

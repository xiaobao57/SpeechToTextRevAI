import time
import IPython
import json

from rev_ai.speechrec import RevSpeechAPI

def await_transcript(client, id_):

   while client.view_job(id_)['status'] == 'in_progress':

       print('waiting...')

       time.sleep(5)

   return client.get_transcript(id_)

# Create client and print account info
client = RevSpeechAPI('01PR6ZhS9868AdeZdJ0wA3P9sze5g86ZNhSmEsoEIB6H9YJYkpkS-xEay8WLei_bfGnMAJxr-eI_rZGFTOVuOqEitPL0o')
print(client.get_account())

# Get user input and create file
file = input("Enter the name of the file (ex: interview.mp3): ")
result = client.submit_job_local_file('C:/Users/Bryan/OneDrive/Desktop/User-created_Documents/Tech/RevAI/' + file)
transcript = await_transcript(client, result['id'])

# Assign text file to an item dictionary
json_data = json.dumps(transcript)
item_dict = json.loads(json_data)


for i in range(len(item_dict['monologues'])):
	print("Speaker: " + transcript['monologues'][i]['speaker'])
	for j in range(len(item_dict['monologues'][i]['elements'])):
		print(transcript['monologues'][i]['elements'][j]['value'], end='')
	print()

# IPython.embed()
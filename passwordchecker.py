import hashlib
import requests



def get_hashed_password(password):
	hash=hashlib.sha1(password.encode(encoding='utf-8'))
	hash=hash.hexdigest().upper()
	return hash

def get_api_response(head_hash):

	url='https://api.pwnedpasswords.com/range/'+(head_hash)
	response=requests.get(url)
	#print (response.text)
	return response.text


if __name__ =='__main__':

	with open('test.txt', mode='r') as input_file:
		for line in input_file:
			hash=(get_hashed_password(str(line).split(';')[0]))
			tail=hash[5:]
			head=hash[:5]
			#print (head + ' '+tail)
			response = get_api_response(head)
			response = response.splitlines()
			#print (response)

			summary={}
			for counter in range(0, len(response)):
				key = response[counter].split(':')[0]
				value= response[counter].split(':')[1]
				summary.update({key: value})

			
			star_string= ''.join(['*' for char in line.split(';')[0]])
			if tail in summary.keys(): 
				print(f'{star_string} is hacked {summary[tail]} times!!')

			else:
				print(f'{star_string} is hacked 0 times!!')
				


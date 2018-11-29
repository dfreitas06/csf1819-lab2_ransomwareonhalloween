#Decrypt AES - CTR_MODE 128bit Key Size

import sys, struct
from Crypto.Cipher import AES
from Crypto.Util import Counter

key = '47683b9a9663c065353437b35c5d8519'

def decrypt_aes(filename):
	file = open(filename, 'rb')
	data = file.read()
	file.close()

	ctr_hex = data[0:16].encode('hex')
	counter = int(ctr_hex, 16)
	
	data_hex = data[16:].encode('hex')
	
	cipher = AES.new(key.decode('hex'), AES.MODE_CTR, counter=Counter.new(128, initial_value=counter))
	decoded_data = ''
	for i in range(0, len(data_hex), 32):
			data_block = data_hex[i:i+32].decode('hex')
			dec_block = cipher.decrypt(data_block)
			decoded_data += dec_block
			
	tmp = filename.split('.')
	new_filename = tmp[0] + '.' + tmp[1]
	new_file = open(new_filename, 'wb')
	new_file.write(decoded_data)
	new_file.close()

if __name__ == '__main__':
	decrypt_aes(sys.argv[1])
#!/usr/bin/python3

import uuid
import hashlib
import itertools
import sys


alf = 'abcdefghijklmnopqrstuvwxyz1234567890' 

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()

def guess(hash):
	for l in range(4): #change the range if you expect the dehashed value to be longer or shorter)
		for try_ in itertools.product(alf, repeat=l + 1):
			if hash_password(''.join(try_).strip()) == hash:
				print(''.join(try_))

for i in sys.stdin:
	guess(i.strip())

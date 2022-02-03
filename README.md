# bot-concours

Ce bot permet de spam les réponses dans un commentaire afin d'avoir plus de chances de gagner un concours sur Twitter.

Ce programme nécessite le module tweepy installable avec la commande ```pip3 install tweepy``` (ceci est impératif afin de lancer le programme)

Tout d'abord, il faudra vous créer un compte Twitter Developpers afin d'acquérir une clé API 

https://developer.twitter.com/en


Ensuite, il faudra créer votre projet sur le Dashbord. Puis copier les clés dans le fichier ```bot-concours.py``` et remplir les champs ci-dessous


```python
consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_SECRET'
access_token='ACCESS_TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET'
```

Finalement, lancez le programme dans l'invite de commande en tappant ```python3 bot-concours.py```
On va vous demander le message que vous voulez spammer, puis le nombre de fois que vous voulez l'envoyer (il est parfois impossible d'atteindre ce nombre à cause des restrictions de twitter qui limitent le nombre de réponses à un tweet en 1 heure) et finalement l'ID du tweet qui s'obtient en copiant les nombres situés à la fin de l'url du tweet (par exemple ```https://twitter.com/misernesstwitch/status/1481346695149535232```)


En espérant que vous gagnerez vos concours !

## Ambiente
Creazione di un container dove eseguire l'ambiente di sviluppo
 - Docker
      -   Per l'esecuzione in ambiente Mac (M1) necessario aggiungere il parametro `platform: linux/amd64`
      -  Aggiunta del parametro nella configurazione del database   
   
 - Definizione file Dockerfile   
 - Definizione file docker-compose.yaml  
 - Definizione file .env con variabili di ambiente da memorizzare

> *Nella cartella sono presenti i file associati per la creazione dei container indicato.*

  

**Librerie aggiuntive**

python-dotenv library per leggere file .env con configurazioni

Le librerie necessarie per l’esecuzione dell’ambiente sono presenti in un file dal nome ‘re  quirements.txt”


**Configurazione Database**

Si utilizza un database locale in formato sqlite, per l’attivazione del database su Mysql è presente un file .env con le variabili di ambiente da configurare con i parametri di accesso al DB

Presente anche nel file delle configurazioni di Django la sezione con la parametrizzazione per l’accesso con mysql.

**Docker shell**

    docker-compose build    
    docker-compose up
    docker compose docker exec -it illiad sh

  
  

## Database

Si utilizza come standard per la restituzione dei dati il formato JSON. I dati sono memorizzati localmente su un database SQLIite 
Sono presenti anche i due database utilizzati per la gestione dell'ambiente (db.sqlite3) e per i test di copetura (.coverage).
L’accesso alle API deve essere effettuato con credenziali abilitate, le credenziali sono memorizzate a livello di database e file sessione utente.

## **Feature API**

Si è scelto di utilizzare DjangoRestFramework data la presenza di documentazione e l’utilizzo di un framework riusabile per implementazioni successive

  

***Filtri per data, nome, description (GET)***
    
|url |descrizione  |  note|
|--|--|--|
|GET /orders  | lista ordini |paginazione con 100 elementi come da impostazioni |

***Parametri chiamata***


|parametri filtro |Esempio  | 
|--|--|--|
|?data (formato YYYY-MM-DD): **gte:** grande più di **lte:** piu piccolo d | es. ordini tra due date - `GET /orders?gte=2024-06-16&&lte=2024-06-17`: | i |
| nome  (formato stringa): **name** | es. filtro ordini contente nel nome ‘pro”: `GET /orders?name=pro` |
|descrizione (formato stringa): **des** | es. filtro ordini contente nel  nome ‘pro”: `GET /orders?desc=pro`

 ---------- 
**ORDER**
Utilizzando i parametri anche in cascata nel seguente ordine di precedenza data > nome > descrizione
| url | descrizione |
|--|--|
| GET /order/detail/<id:int>/ | dettaglio singolo ordine |
| PUSH /order/detail/<id:int>/ | modifica tutti dati ordine |
| PATCH /order/detail/<id:int>/ | modifica dati ordine parziali|
|  DELETE /order/detail/<id:int>/| elimina voce ordine |


-----------    
**PRODUCT**
 presente anche un api get per la lettura dei dati associati ai singoli prodotti
    
| url |  descrizione|
|--|--|
| GET /product | lista prodotti, indicazione della paginazione come da file di configurazione di Django|
| GET /product/id:int |dettaglio prodotto singolo per associazine dati ordini|
|  DELETE /order/detail/<id:int>/| elimina voce ordine |

 **https://www.django-rest-framework.org/api-guide/routers/#defaultrouter** 
 

## Sviluppo

-   modello dei dati    

Si presuppone che un ordine abbia N prodotti associati e che N prodotti possano essere in altrettanti ordini.

Al fine di avere nel database la consistenza dei dati e la possibilità di estrazioni dei dati che non effettuino join tra tabelle che potrebbero avere dimensioni elevate si utilizza per la memorizzazione dei prodotti negli ordini un Array Field con i riferimenti agli ID dei prodotti.  

Si presuppone che la lunghezza dei campi charfield non sia superiore a 255 caratteri



**MODEL: Order**

| Type | Obbligatorio | Nome|
|--|--|--|
| primary | Si |ID |
|char field (255)  | Si | name|
| text field | No | description|
| data | Si | date|
| product (Many to many relation) | No |products |


  | Type | Obbligatorio | Nome|
|--|--|--|
| primary | Si |ID |
| char field (255) | Si | name|
| float |Si  | price|

Potranno essere creati oggetti del tipo ‘Order’ con riferimenti a uno più oggetti del tipo ‘Product’.

Il campo ‘products’ del modello ‘Order’ può essere vuoto, nel caso di ordini senza riferimenti a oggetti del modello ‘Product’

Si è scelto di memorizzazione dei dati dei prodotti acquistati un ManyToMany related field, si presuppone che i dati dei prodotti (oggetti Product) possano essere creati, ma non eliminati in modo ricorsivo con chiamate delete da oggetti Order.

## Django - RESTFramework

Creazione progetto

 - django-admin startproject iliad
 - django-admin startapp EndpointAPi

Utilizzo DB locale sqlite : db.sqlite3



## Authenticazione

Gli utenti devono essere autenticati tramite utente e/o token. Per comodità la gestione delle autenticazioni sono abilitate dall’admin di Django .  

    http://localhost:8000/admin

  *Creazione utente admin*
 - u: operation
 - p: operation
  
Inserito '**rest_framework.authtoken**' per la possibilità della gestione dei token di autenticazione direttamente dal pannello di amministrazione di Django.

  

## Testing

Verifica della copertura dei test. La libreria **coverage** permette di verificare la copertura dei test effettuati sul codice con un livello di granularità alto.

    pip install coverage

    coverage run --source=EndpointAPI manage.py test
    coverage -m    

> https://coverage.readthedocs.io/en/7.5.3/
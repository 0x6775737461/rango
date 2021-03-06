## rango

---

Uma API REST feita com o framework Django REST.

---

### Requerimentos

**OBS: Todas as aplicações foram testadas apenas em GNU/Linux,
preferencialmente os _Debian Based_ (baseados em Debian).**

As ferramentas usadas neste "leia-me":

- bash (Bourne Again Shell).

- [curl](https://github.com/curl/curl).

- [jq](https://github.com/stedolan/jq).

- ... (algumas já são implícitas, como o python, django framework, etc.)

### Instalação

Crie seu ambiente de desenvolvimento isolado:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Baixando os pacotes:

```bash
(env) $ pip install -r requirements.txt
```

---

#### Atenção

Esta aplicação foi feita com o intuíto de solucionar um desafio técnico. Para que os requerimentos
em relação ao banco de dados seja atendido, há "fixtures" para inserir os dados no DB. Porém no
repositório haverá o arquivo(`db.sqlite3`) já preenchido para fins de análise.

O preenchimento foi feito com os seguintes comandos:

```bash
$ python3 manage.py loaddata regions.json
$ python3 manage.py loaddata fruits.json
```

Os passos á seguir serão válidos caso queira explorar como os variados métodos funcionam. Então o arquivo
de exemplo no repositório deve ser apagado.

### Como usar

Antes de seguir esse _hands-on_, apague (ou não) o banco de dados que o repositório contém.
Para iniciar a aplicação utilize o CLI do Django (esteja com o shell desenvolvimento ativado):

```bash
(env) $ test -e db.sqlite3 || python manage.py migrate && echo "Apague o arquivo antes de seguir!"
(env) $ python manage.py runserver
```

Temos duas tabelas (_Region_ e _Fruits_) no nosso banco de dados, ambas possuem os
4 métodos HTTP: GET, POST, PUT e DELETE.

#### POST

Com a aplicação em execução faça uma requisição POST com o `curl`.

```bash
$ curl -X POST -H 'content-type: application/json' -d '{"name":"Centro-Oeste"}' http://127.0.0.1:8000/region/
```

A nossa tabela _Region_ agora possui a região Centro-Oeste na coluna "names", vamos inserir alguma fruta
na tabela _Fruits_ utilizando também o método POST:

```bash
$ curl -X POST -H 'content-type: application/json' -d '{"name":"Cajá","origin":1}' http://127.0.0.1:8000/fruits/ | jq
```

#### GET

GET pode ser feito na API para pegar os dados na coluna "name" da tabela "Region".
No comando anterior inserimos a região "Centro-Oeste", com o ID retornado pela API faça uma requisição GET
passando esse ID como parâmetro:

```bash
$ curl -Ss -X GET http://127.0.0.1:8000/region/1/ | jq
```

Formato da resposta:

```json
{
  "id": 1,
  "name": "Centro-Oeste"
}
```

#### PUT

Este método irá servir como atualizador de dados já existentes em nosso banco de dados.
Repare que anteriormente inserimos a fruta "Cajá" e fizemos a relação dela com a região
Centro-Oeste, porém ela tem maior abundância no Nordeste, então vamos modificar a região através
do método PUT:

```bash
$ curl -X PUT -H 'content-type: application/json' -d '{"name":"Nordeste"}' http://127.0.0.1:8000/region/1/ | jq
```

#### DELETE

Para apagar os dados que atribuímos podemos usar o método DELETE.
Apagando as informações do "Nordeste" e a fruta "Cajá":

```bash
$ curl -X DELETE http://127.0.0.1:8000/region/1/
```

Não iremos precisar apagar os dados da tabela _Fruits_, ela é configurada com uma "chave estrangeira",
então ela é apagada assim que apagamos a região associada.

## todo:

- [ ] remover o db e o arquivo de migrations do gitignore.

- [ ] os métodos http estão repetindo em Region(\*) e Fruits(\*).

- [ ] script para inserir os dados das regiões e frutas, automaticamente.

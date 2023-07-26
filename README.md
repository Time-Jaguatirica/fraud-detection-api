# API Detecção de Fraudes


### Python3 environment
```bash
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```


### Como rodar localmente
- Criar um arquivo *.env* similar ao *.env.example*.

- Utilizando servidor local:
```bash
gunicorn app:server --bind 0.0.0.0:8000
```

- Utilizando docker compose:
```bash
docker compose up
```


### Referências
- [Real Python](https://realpython.com/python-dash/)
- [Health Check](https://howchoo.com/devops/how-to-add-a-health-check-to-your-docker-container)

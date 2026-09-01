# G2-2026-2
Grupo G2 - Metodos de Desenvolvimento de Software 2026/2

# Flask Application

Aplicação base desenvolvida com Flask.

## Requisitos

* Python 3.10 ou superior
* pip

## Configuração do ambiente

Clone o repositório e acesse o diretório do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_PROJETO>
```

Crie e ative um ambiente virtual:

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a aplicação

Com o ambiente virtual ativado, execute:

```bash
python run.py
```

A aplicação estará disponível no endereço informado pelo Flask no terminal, normalmente:

```text
http://127.0.0.1:5000
```

## Desenvolvimento

Antes de iniciar o desenvolvimento, certifique-se de que:

1. O ambiente virtual está ativado.
2. As dependências do `requirements.txt` estão instaladas.
3. A aplicação inicia corretamente com `python run.py`.

## Configurações sensíveis

Informações sensíveis, como credenciais, tokens e chaves de API, não devem ser versionadas no repositório. Essas configurações devem ser fornecidas por variáveis de ambiente ou outro mecanismo apropriado.


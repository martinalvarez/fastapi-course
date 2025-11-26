fastapi-basico/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies/
│   │   └── __init__.py
│   ├── web/
│   │   ├── __init__.py
│   │   └── routers/
│   │       ├── __init__.py
│   │       └── items.py
│   ├── models/            # Modelos Pydantic (request/response)
│   │   ├── __init__.py
│   │   └── item_model.py
│   ├── services/          # Lógica de negocio
│   │   ├── __init__.py
│   │   └── item_service.py
│   ├── data/              # “Repositorio” (memoria, mock, luego DB si querés)
│   │   ├── __init__.py
│   │   └── item_repository.py
│   └── utils/             # Acá podés meter generadores, iteradores, helpers
│       ├── __init__.py
│       └── python_concepts.py
│
├── tests/
│   ├── __init__.py
│   ├── test_items.py
│   └── conftest.py
│
├── requirements.txt
├── pyproject.toml          # (opcional si usás poetry/pdm)
└── README.md


✔️ Por qué esta estructura es buena
Web / Routers

app/web/routers mantiene los endpoints limpios.

Podés hacer routers chicos y agregar más (users, auth, etc).

Services

Aíslan la lógica de negocio → facilita testing y reuso.

Data

Repositorios simples, empezando en memoria (list, dict), luego podés crecer a SQLAlchemy si querés.

Dependencies

DI al estilo FastAPI: get_repository, get_service, etc.

Utils

Si querés jugar con todos los conceptos de Python (generators, itertools, decoradores), acá es buen lugar.

Tests

Fácil de usar con pytest + TestClient.












✅ Cómo crear, activar y desactivar un venv en Python
1) Crear entorno virtual

En la carpeta de tu proyecto:

python -m venv .venv


(.venv es un nombre estándar y recomendado.)

Linux / macOS
source .venv/bin/activate

3) Desactivar el entorno virtual

Funciona igual en todos los sistemas:

deactivate

Cómo instalar paquetes desde requirements.txt

Con el entorno virtual activado:
pip install -r requirements.txt



✅ 1. ¿Cómo hago para correr el sitio?

Asumiendo que ya tenés tu venv activado y un main.py con FastAPI, el comando es:

uvicorn app.main:app --reload


app.main → ruta al módulo

app → instancia de FastAPI dentro de ese módulo

--reload → recarga automática en desarrollo

Si pusiste el proyecto de otra forma, adaptamos el comando.
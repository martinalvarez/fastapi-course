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

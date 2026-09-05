name: CI - Centro Psicologico Mente Sana

on: [push, pull_request]

jobs:
  verificar:
    runs-on: ubuntu-latest
    steps:
      - name: Descargar el código fuente
        uses: actions/checkout@v4

      - name: Configurar entorno Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar pytest
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Ejecutar Pruebas Automatizadas
        run: |
          pytest

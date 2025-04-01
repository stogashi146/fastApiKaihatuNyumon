FROM python:3.11-buster

ENV PYTHONUNBUFFERD=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.tmol* poetry.lock* ./

# portryでライブラリをインストール(pyproject.tomlがすでにある場合）
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--reload"]
# ENTRYPOINT ["tail", "-f" , "/dev/null"]
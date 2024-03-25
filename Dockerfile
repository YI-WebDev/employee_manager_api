FROM python:3

# バイトコードの生成を無効化
ENV PYTHONDONTWRITEBYTECODE 1
# 標準出力のバッファリングを無効化
ENV PYTHONUNBUFFERED 1

# ディレクトリを/srcに設定
WORKDIR /src

# 依存パッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトファイルを/srcにコピー
COPY . /src/

# ポート8000を公開
EXPOSE 8000

# Djangoの開発サーバーを実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
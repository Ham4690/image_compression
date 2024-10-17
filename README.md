# Image Compression

このプロジェクトでは、`input`フォルダ内の JPEG 画像を圧縮し、`output`フォルダに同名で保存します。圧縮後の画像は指定サイズに近づけるように調整されます。

## フォルダ構成

```
image_compression_project/
├── compress_images.py  # メインスクリプト
├── input/              # 圧縮前の画像を保存するフォルダ
├── output/             # 圧縮後の画像を保存するフォルダ
├── README.md           # このファイル
```

## 必要なライブラリ

このプロジェクトでは、画像処理のために`Pillow`ライブラリを使用しています。以下の手順で必要なライブラリをインストールしてください。

```bash
python3 -m venv venv  # 仮想環境を作成
source venv/bin/activate  # 仮想環境を有効化
pip install Pillow  # 必要なライブラリをインストール
```

## 使い方

1. `input`フォルダに圧縮したい JPEG 画像を保存します。
2. 以下のコマンドを実行して、画像を圧縮します。

```bash
python compress_images.py
```

3. 圧縮後の画像は、`output`フォルダに同じファイル名で保存されます。

## 圧縮ロジック

- 画像の初期画質は 85 に設定されており、ファイルサイズが指定サイズ（デフォルトは 300KB）を超える場合、画質を段階的に下げながら圧縮します。
- 最低画質は 10 まで下げることができます。それでもファイルサイズが指定サイズに達しない場合は、これ以上の圧縮は行いません。

## カスタマイズ

- デフォルトでは最大サイズが 300KB に設定されています。`compress_images.py`内の`max_size_kb`を変更することで、任意のファイルサイズに調整可能です。

```python
compress_images_in_folder(input_folder, output_folder, max_size_kb=500)  # 500KBまで圧縮する場合
```

## 注意事項

- 現在は JPEG 画像のみが対象となっていますが、`Pillow`ライブラリを使って他の画像フォーマットにも拡張可能です。

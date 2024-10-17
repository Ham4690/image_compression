import os
from PIL import Image

def compress_image(input_path, output_path, quality=85, max_size_kb=300):
    """JPEG画像を圧縮して指定されたファイルサイズに近づける"""
    img = Image.open(input_path)
    
    # 初期設定で画像を圧縮保存
    img.save(output_path, "JPEG", quality=quality)
    
    # ファイルサイズを確認
    size_kb = os.path.getsize(output_path) / 1024
    
    # サイズが指定サイズを超える場合、画質を下げて圧縮
    while size_kb > max_size_kb and quality > 10:
        quality -= 5
        img.save(output_path, "JPEG", quality=quality)
        size_kb = os.path.getsize(output_path) / 1024
        print(f"Compressed size: {size_kb:.2f}KB with quality={quality}")
    
    print(f"Final size: {size_kb:.2f}KB")

def compress_images_in_folder(input_folder, output_folder, max_size_kb=300):
    """フォルダ内の画像を圧縮して別フォルダに保存"""
    # フォルダが存在しなければ作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # フォルダ内のファイルをループで処理
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path):
            print(f"Compressing {filename}...")
            compress_image(input_path, output_path, max_size_kb=max_size_kb)
        else:
            print(f"{filename} is not a valid file.")

if __name__ == "__main__":
    input_folder = "input"  # 圧縮前の画像フォルダ
    output_folder = "output"  # 圧縮後の画像を保存するフォルダ
    compress_images_in_folder(input_folder, output_folder)

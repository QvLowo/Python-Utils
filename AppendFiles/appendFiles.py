"""
合併多個下載的檔案內容，搬移至目標資料夾
"""

import os
import re
import shutil

target_path = "your_target_path"
source_path = "your_download_source_path"

source_file = "svc_log"
source_file_suffix = ".txt"


# 確保目標資料夾存在
os.makedirs(target_path, exist_ok=True)

# 指定預設執行路徑
os.chdir(source_path)

# 取得所有 .txt 檔案
text_files = [f for f in os.listdir(source_path) if f.startswith(
    source_file) and f.endswith(source_file_suffix)]
# 排序
text_files.sort(key=lambda f: (re.sub(r'\D', '', f), f))

first_file = os.path.join(source_path, source_file+source_file_suffix)
with open(first_file, "r", encoding="utf-8") as file:
    first_line = file.readline().strip()
    parts = first_line.split(',')
    sid = parts[1]

output_file = sid + ".txt"
print(f"身分證為: {output_file}")

# 合併檔案內容
with open(output_file, "w", encoding="utf-8") as outfile:
    for file in text_files:
        origin_file = os.path.join(source_path, file)  # 拼接路徑+檔案名稱
        with open(origin_file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n")
        os.remove(origin_file)  # 刪除合併前檔案

# 移動合併後的檔案到目標資料夾
shutil.move(output_file, os.path.join(target_path, output_file))
print(f"合併完成，檔案已移動到 {target_path}/{output_file}")

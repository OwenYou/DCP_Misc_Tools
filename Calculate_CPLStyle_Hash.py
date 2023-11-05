import base64
import hashlib
import time
import os
# from progress.bar import Bar
from math import ceil

# 输入数据
# Input Data Path
audio = r'E:\audio.mxf'
video = r"E:\video.mxf"

def calculate_dcp_style_hash(filepath, bar = None):
    file_size = os.path.getsize(filepath)
    with open(filepath, "rb") as file:
        # 创建一个SHA-1哈希对象
        # Create a SHA-1 object.
        sha1_hash = hashlib.sha1()
        # 逐块更新哈希对象以处理文件内容
        # Update the hash object per file chunk.
        chunk_size = 262144  
        # ↑每次读取的字节数, 现在是256KB, 这个数提高到这个值对处理速度提升很大
        # Bytes per chunk, 256KB is optimized for performance.
        total_work = ceil(file_size/chunk_size)  # Total chunk count
        print(total_work)
        # progress = 0
        if bar:  
            # 如果传入progress.bar的Bar对象, 就处理进度条信息
            # if a progress.bar Bar class is present, process info for it.
            bar.max = total_work
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                sha1_hash.update(data)
                bar.next()
            bar.finish()
        else:  
            # 不管progress.bar, 只计算哈希
            # no progress.bar, calculate hash only
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                sha1_hash.update(data)

    # 计算SHA-1哈希HEX值
    # calculate SHA-1 Hash Hex
    sha1_hex_digest = sha1_hash.hexdigest()
    # print("SHA-1哈希值:", sha1_hex_digest)
    binary_data = bytes.fromhex(sha1_hex_digest)
    # 使用base64进行编码
    # encode with base64
    base64_encoded = base64.b64encode(binary_data).decode('utf-8')
    # print(base64_encoded)
    return base64_encoded

if __name__ == '__main__':
    time1 = time.time()
    # bar = Bar('Hash Calculation Progress')
    print(calculate_dcp_style_hash(video))
    print(time.time()-time1)




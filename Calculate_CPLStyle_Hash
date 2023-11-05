import base64
import hashlib
import time
import os
# from progress.bar import Bar
from math import ceil

# 输入数据
audio = r'E:\audio.mxf'
video = r"E:\video.mxf"

def calculate_dcp_style_hash(filepath, bar = None):
    file_size = os.path.getsize(filepath)
    with open(filepath, "rb") as file:
        # 创建一个SHA-1哈希对象
        sha1_hash = hashlib.sha1()
        # 逐块更新哈希对象以处理文件内容
        chunk_size = 262144  # 每次读取的字节数, 现在是256KB, 这个数提高到这个值对处理速度提升很大
        total_work = ceil(file_size/chunk_size)  # 总chunk量
        print(total_work)
        # progress = 0
        if bar:  # 如果传入progress.bar的Bar对象, 就处理进度条信息
            bar.max = total_work
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                sha1_hash.update(data)
                bar.next()
            bar.finish()
        else:  # 不管progress.bar, 只计算哈希
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                sha1_hash.update(data)

    # 计算SHA-1哈希HEX值
    sha1_hex_digest = sha1_hash.hexdigest()
    # print("SHA-1哈希值:", sha1_hex_digest)
    binary_data = bytes.fromhex(sha1_hex_digest)
    # 使用base64进行编码
    base64_encoded = base64.b64encode(binary_data).decode('utf-8')
    # print(base64_encoded)
    return base64_encoded

if __name__ == '__main__':
    time1 = time.time()
    # bar = Bar('Hash Calculation Progress')
    print(calculate_dcp_style_hash(video))
    print(time.time()-time1)




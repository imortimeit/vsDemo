import requests
from contextlib import closing
import time
import os

def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print ('下载开始')
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())

if __name__ == '__main__':
    url = 'https://cdn.feet9.com/media/videos/mp4/17995.mp4?cdn_hash=f5d3ce01f0e5e9830fef0f5865d3f507&cdn_creation_time=1585993714&cdn_ttl=1800&cdn_cv_net=172.104.101.201'
    path = '玉足2.mp4'
    download_file(url, path)

# read all txt files under the directory and print all links start with 'http'
import datetime
import os
from mega import Mega

list = []
target_date = datetime.datetime(2025, 1, 8)


def read_txt_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        create_time = os.path.getmtime(file_path)
        create_date = datetime.datetime.fromtimestamp(create_time)
        print(create_date, filename)
        if create_date > target_date:
            if filename.endswith('.txt'):
                # create a folder under upper directory with the name same as txt
                folder_name = os.path.splitext(filename)[0].replace(' ', '_').split('_')[0]
                # folder_path = os.path.join(os.path.dirname(directory), folder_name)
                # os.makedirs(folder_path, exist_ok=True)
                with open(os.path.join(directory, filename), 'r') as f:
                    urls = []
                    for line in f:
                        if line.startswith('http'):
                            urls.append(str(line).split()[0])
                    index = 0
                    for url in urls:
                        if 'folder' in url:
                            urls.remove(urls[index + 1])
                        index += 1
                    dic = {folder_name: urls}
                    list.append(dic)
    return list

def download_links(list):
    mega = Mega()
    m = mega.login()
    for dic in list:
        for key in dic:
            folder_name = key
            folder_path = os.path.join(os.path.dirname(DIRECTORY), folder_name)
            os.makedirs(folder_path, exist_ok=True)
            urls = dic[key]
            for url in urls:
                m.download_url(url, folder_path)


DIRECTORY = "F:\\Video\\Latex\\veritabledxzx22\\Link"
MEGA_LINK = "https://mega.nz/file/K4IUibpQ#wwTE6IpBZAUI5UTS_gvf3SQEbYN5haBFqcSU9e06A7Q"

if __name__ == '__main__':
    os.environ['TEMP'] = r'E:\Temp'
    mega = Mega()
    m = mega.login()
    m.download_url(MEGA_LINK, DIRECTORY)

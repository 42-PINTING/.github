import os
import shutil
import yaml
from datetime import datetime

def list_scrums_in_directory(directory):
    content_list = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    source_path = os.path.join(directory, entry.name)
                    dest_path = os.path.join("/home", "scrums")
                    content_list.append(entry.name)
                    shutil.copy(source_path, dest_path)
                    print(f"{source_path} -> {dest_path}")
    except FileNotFoundError:
        print(f"The directory {directory} or {dest_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content_list

def update_mkdocs_config(yaml, directory, section, date_format='%Y.%m.%d'):
    try:
        # YAML 파일 읽기
        with open("mkdocs.yml", 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        files = list_files_in_directory(directory)

        # 디렉토리 내 파일 목록 가져오기
        files = list_files_in_directory(directory)

        # 파일 목록을 기반으로 날짜 부분 업데이트
        file_entries = {}
        for file in files:
            file_name = os.path.splitext(file)[0]
            try:
                date = datetime.strptime(file_name, '%Y.%m.%d')
                file_entries[file_name] = os.path.join(directory, file)
            except ValueError:
                print(f"File name '{file_name}' does not match date format '{date_format}'")

        # 기존 섹션 업데이트
        if section in config['nav']:
            config['nav'][section] = [{file_name: file_path} for file_name, file_path in sorted(file_entries.items())]

        # YAML 파일 다시 쓰기
        with open(yaml_file, 'w', encoding='utf-8') as file:
            yaml.safe_dump(config, file, allow_unicode=True, sort_keys=False)

        print(f"YAML file '{yaml_file}' updated successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# directory_path = '/home/scrum-archive'
# contents_list = list_scrums_in_directory(directory_path)
update_mkdocs_config("mkdocs.yml", "scrums", "Scrum")

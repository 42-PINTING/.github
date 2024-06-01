import os
import shutil
import yaml
from collections import OrderedDict

def archive_to_docs(archive_directory_path, dest_directory_path):
    content_list = []
    try:
        with os.scandir(archive_directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    source_file_path = os.path.join(archive_directory_path, entry.name)
                    dest_file_path = os.path.join(dest_directory_path, entry.name)
                    content_list.append(entry.name)
                    print(f"{source_file_path} -> {dest_file_path}")
                    shutil.copy(source_file_path, dest_file_path)
    except FileNotFoundError:
        if (os.path.exists(archive_directory_path)):
            print(f"The directory {archive_directory_path} does not exist")
        else: 
            print(f"The directory {dest_file_path} does not exist") 
    except PermissionError:
        print(f"Permission denied to access the directory {archive_directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content_list

def list_content_in_directory(directory):
    content_list = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    content_list.append(entry.name)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content_list

def find_section(nav, section_name):
    for item in nav:
        if isinstance(item, dict) and section_name in item:
            return item
    return None

def update_mkdocs_config(yaml_file, docs_directory_path, config_directory_path, section):
    # try:
        # YAML 파일 읽기
        with open(yaml_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        # 디렉토리 내 파일 목록 가져오기
        files = list_content_in_directory(docs_directory_path)

        # 파일 목록을 기반으로 날짜 부분 업데이트
        file_entries = {}
        for file in files:
            file_name = os.path.splitext(file)[0]
            file_entries[file_name] = os.path.join(config_directory_path, file)

        section_item = find_section(config['nav'], section)
        if section_item is not None:
            reversed_file_entries = OrderedDict(reversed(list(sorted(file_entries.items()))))
            print(reversed_file_entries)
            section_item[section] = [{file_name: file_path} for file_name, file_path in reversed_file_entries.items()]
        else:
            print("there is no nav section")
        # YAML 파일 다시 쓰기
        with open(yaml_file, 'w', encoding='utf-8') as file:
            yaml.safe_dump(config, file, allow_unicode=True, sort_keys=False)

        print(f"YAML file '{yaml}' updated successfully.")
    # except FileNotFoundError as e:
    #     print(f"File not found: {e}")
    # except PermissionError:
    #     print(f"Permission denied: {e}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

archive_path = '/home/Pinting-Docs/scrum-archive'
docs_path = '/home/Pinting-Docs/docs/scrums'
config_path = 'scrums'
mkdocs_scrum_section = 'Scrum'

archive_to_docs(archive_path, docs_path)
update_mkdocs_config("mkdocs.yml", docs_path, config_path, mkdocs_scrum_section)
# Оригинальный репозиторий
https://github.com/Nanne/pytorch-NetVlad

Данный репозиторий имеет множество доработок для адаптации к текущему конкурсу Я-Профессионал (МФТИ, 2021)

# Установка

Перейти в папку docker репозитория netvlad_pytorch:
```bash
cd docker
```
Запустить скрипт, выполняющий сборку докер образа:
```bash
bash build.sh
```

# Загрузка модели
Загрузить и извлечь архив модели по ссылке https://drive.google.com/open?id=17luTjZFCX639guSVy00OUtzfTQo4AMF2 в папку
/data/\<USER\>
где \<USER\> -- логин пользователя для входа в сервер, предоставленный по конкурсу.


# Запуск докер контейнера

```bash
./docker/start_and_into.sh

export PYTHONPATH="${PYTHONPATH}:${PWD}"
```

# Запуск скрипта подготовки метаданных для NetVLAD
```bash
python prepare_metadata_for_netvlad.py
```
Данный скрипт принимает два аргумента (см через команду `python prepare_metadata_for_netvlad.py -h`), значения аргументов этого скрипта уже готовы для датасета конкурса Я-профессионал.
В результате выполнения скрипта появится файл `metadata.json` в папке /home/\<USER\>/netvlad_pytorch (аргумент по умолчанию)

# Запуск NetVLAD (получение векторов изображений)
```bash
bash run_NetVLAD.sh
```
В результате выполнения вышеприведенного скрипта появится файл NetVLAD_query_top_40.txt в папке /home/\<USER\>/netvlad_pytorch.
Данный файл содержит в каждой строчке пару (query_image database_image), где query_image - изображение запроса (из тестовой выборки), database_image - изображение из базы данных с известной позой.

# Получение поз изображений запроса (изображений из тестовой выборки)
```bash
python get_poses_from_db.py
```
Данный скрипт выдает для каждого тестового изображения позу, равную позе изображения из database, которая имеет ближайшее расстояние (расстояние между векторами изображений запроса и базы данныъх).

# pytorch-NetVlad

Implementation of [NetVlad](https://arxiv.org/abs/1511.07247) in PyTorch, including code for training the model on the Pittsburgh dataset.

### Reproducing the paper

Below are the result as compared to the results in third row in the right column of Table 1:

|   |R@1|R@5|R@10|
|---|---|---|---|
| [NetVlad paper](https://arxiv.org/abs/1511.07247)  | 84.1  | 94.6  | 95.5  |
| pytorch-NetVlad(alexnet)  | 68.6  | 84.6  | 89.3  |
| pytorch-NetVlad(vgg16)  | 85.2  | 94.8  | 97.0  |

# Сборка докер образа

```bash
cd netvlad_pytorch
bash build.sh
```

## Запуск докер контейнера

```bash
./docker/start_and_into.sh

export PYTHONPATH="${PYTHONPATH}:${PWD}"
```

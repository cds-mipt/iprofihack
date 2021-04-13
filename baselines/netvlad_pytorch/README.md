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
Загрузить модель по ссылке https://drive.google.com/open?id=17luTjZFCX639guSVy00OUtzfTQo4AMF2 в папку
/data/\<USER\>
где \<USER\> -- логин пользователя для входа в сервер, предоставленный по конкурсу.


# Запуск докер контейнера

```bash
./docker/start_and_into.sh

export PYTHONPATH="${PYTHONPATH}:${PWD}"
```


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

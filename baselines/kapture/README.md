# Kapture

- Статья kapture https://arxiv.org/pdf/2007.13867.pdf
- Pipeline kapture-localization
https://github.com/naver/kapture-localization/blob/main/doc/tutorial.adoc
- Image retrival (AP-Gem) https://github.com/naver/deep-image-retrieval
- Local feature exctractor (R2D2)  https://github.com/naver/r2d2

Метод состоит из нескольких этапов. Сперва предобученная нейронная сеть AP-Gem извлекает из изображений глобальные признаки, по которым далее ищутся похожие изображения (Image retrieval). Этот этап уже позволяет получить базовое решение и сделать submit. 
Далее вторая нейронная сеть (R2D2) - извлекает ключевые точки, которые позволяют восстоновить позу камеры, учитывая геометрию исходящих лучей из одной и той же точки на разных изображениях.  
(Как один из способов решения задачи, предлагается участникам)

## Запуск



```sh
# переходим в корень папки базового решения
cd baselines/kapture
# переходим в директорию со скриптами для работы с docker
cd docker

# собираем образ
bash build.sh

# запускаем контейнер
bash run.sh

# запустится Jupyter notebok, зажимаем Ctrl и переходим по ссылке
# Откроется тетрадка с решением 
# Запуская все ячейки, получаем на выходе файл submission.txt






```


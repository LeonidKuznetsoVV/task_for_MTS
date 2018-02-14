# task_for_MTS_big_data

## 1 В данном репозитории находится набор файлов для реализации процесса загрузки файлов.
#### Процесс запускается bash-скриптон который производит очистку целевой директории от предыдущих загрузок и запускает два процесса Map-Reduce. (соответственно c Mapper-ами prefilter.py и mapper.py ).

#### Для реализации разделения файлов по папкам используется подмена библиотеки CustomOutputFormat
#### Способ взят отсюда:
#### https://stackoverflow.com/questions/18541503/multiple-output-files-for-hadoop-streaming-with-python-mapper

#### Комплируем класс: javac -cp /usr/hdp/2.6.3.0-235/hadoop-mapreduce/ -d ./CustomMultipleOutputFormat.java и добавляем его в class path

#### 

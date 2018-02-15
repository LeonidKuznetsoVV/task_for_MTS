
## Задание №1

#### На Teradata SQL:
##### SELECT id,"Value","Date" 
##### FROM Table
##### QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY "Date" DESC,"Value" DESC)=1

## Задание № 2

##### В папке Task 2 находится набор файлов для реализации процесса загрузки файлов.
##### Процесс запускается bash-скриптом main.sh который производит очистку целевой директории от предыдущих загрузок и запускает два процесса Map-Reduce. (соответственно c Mapper-ами prefilter.py и mapper.py ).

#### Про дополнительные библиотеки:
##### Поскольку задание требует разделять файлы по дирректориям внутри Map-Reduce, то для реализации используется подмена jar-файла CustomOutputFormat с помощью опции -libjars .Способ взят отсюда:
##### https://stackoverflow.com/questions/18541503/multiple-output-files-for-hadoop-streaming-with-python-mapper
##### Комплируем класс командой: javac -cp /usr/hdp/2.6.3.0-235/hadoop-mapreduce/ -d ./CustomMultipleOutputFormat.java и добавляем его в class path. После чего запускаем main.sh (предварительно сделав перенос файлов в нужную папку на виртуальной машине через ssh).

##### PS. Насколько мне удалось найти, такую же функцию разделения по папкам можно выполнить через Python библиотеки (напр. MRjob).


## Задание № 3

##### В папке Task 3 лежит код, который я использовал для решения задачи № 2.
##### Код исполняет пункты 1-5 задания.

#### Общие комментарии:
##### -Приведение таблицы к первой нормальной форме происходит на этапе загрузки. При это предполагается, что все поля таблицы кроме display_url уже приведены к 1НФ. Если это не так, то стоит производить загрузку в несколько таблиц. В данном коде строка сначала выгружается в словарь, потом из словаря трансформируется в денормализованную таблицу, которая загружается в базу данных, а далее в базе данных происходит ее нормализация через декомпозицию на две таблицы и присваивание индексов.

##### -Извлечение данных происходит через обход nested structure по каждой строке. Это сделано, для того, чтобы извлекать нужные поля по их имени из любой сколь угодно вложенной структуры данных. Если структура данных заранее известна, то стоит использовать цепные индексы - напр. line['user']['name'] и т.п.

##### -В коде происходит выгрузка всего файла с твитами в DataFrame (то есть в оперативную память). Так сделано, для того чтобы избежать проблем с "залочиванием" таблицы в sqlite3. Но в конечной версии это лучше сделать через загрузку каждой строки в sql.

##### -Если самых счастливых стран несколько, то берется любая.

#### По вопросу 6:
##### Для ежедневной оценки параметров следует обновлять таблицу через добавление строк. Для того, чтобы сделать пересчет максимально эффективным можно проиндексировать таблицу по полю sentiment. Т.к. для индексирования используется структура данных B-дерево, то поиск максимального индекса будет происходить эффективно за счет упорядоченности листов дерева.

#### По шагам ETL, видимо как-то так:
##### Регулярная выгрузка из FTP сервиса осуществляется через Linux cron + shell скрипт.
##### 1. Shell-скрипт регулярно проверяет наличие новых файлов на FTP и если такие присутствуют,  то начинает процесс построчного извлечения.
##### 2. При построчном извлечении проверяется структура данных и их корректность, исправляются опечатки,   отбираются необходимые поля, словари со вложенными списками разделяются на несколько строк и т.д. При этом программа сохраняет номер последней извлеченной строки для возобновления процесса в случае падения. 
##### Инструменты:python, pentaho. Процесс трансформации происходит одновременно с процессом извлечения строк. 
##### 3. Очищенные данные загружаются на промежуточный сервер. Если эффективнее загружать данные по n строк за шаг, то данные записываются в файлы по n строк в каждом. Как только файл отгружен на сервер запускается процесс загрузки в базу данных.(Teradata BTEQ  или TPT). Либо файлы выгружаются на конечный FTP-сервер и удаляются с промежуточного.

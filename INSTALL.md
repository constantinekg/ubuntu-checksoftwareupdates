# Процесс установки на сервер #

Для начала установить:

```bash
sudo apt install update-motd update-notifier-common git curl
cd /opt
sudo git clone https://github.com/constantinekg/ubuntu-checksoftwareupdates
sudo chmod +x /opt/ubuntu-checksoftwareupdates/influxv1/checksoftwareupdates.py /opt/ubuntu-checksoftwareupdates/influxv2/checksoftwareupdates.py
```

## Для influxdb v 2

```
sudo -H pip3 install influxdb-client
```

Далее необходимо поправить значения в теле скриптов (url'ы - куда будут слаться значения метрик; если используется influx версии 2 и выше, то наименование организации и api ключ). 

В целом на этом шаге сбор метрик готов, но если надо красивый дэшборд в графане и алерты, то соответственно создать дэшборд в графане и прикрутить там же алерты...

Если совсем секьюрно надо, то прикрутить ssl на инфлаксе или поставить nginx и запроксировать через него запросы на influx, при этом натянув ssl на nginx...

# Berker Okan site

## Kullanım:

SSH ile gir
`source .venv/bin/activate`
`cd berkerokan.com.tr/source`
`python3 manage.py runserver 0.0.0.0:80`
bu kadar.

0.0.0.0 ip adresi public oluyo

screen diye bişi var ayrı thread/process açıyor arkaplanda çalışıyor böylece ssh bağlantısını sürekli aktif tutmak zorunda değiliz serverin çalışması için .
`screen -r django_server` -> django_server diye screen açtım ona girmek için

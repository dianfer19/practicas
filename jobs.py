from apscheduler.schedulers.blocking import BlockingScheduler

def holamundo():
    print('Hola Mundo')

scheduler = BlockingScheduler()
#scheduler.add_job(holamundo, 'cron', day_of_week='mon-fri', hour=22, minute=36)
# scheduler.add_job(envio_mail, 'cron', hour=22)
# Ejecuta la funcion todos los días a las 10 am
# scheduler.add_job(mostrar, 'cron', hour=10)
# Ejecuta la funcion especificando un día de la semana y una hora determinada
# scheduler.add_job(mostrar, 'cron', day_of_week='wed', hour=8)
# Ejecuta la funcion especificando varios días de la semana y una hora minuto determinada
# scheduler.add_job(mostrar, 'cron', day_of_week='mon,wed,fri', hour=13, minute=30)
# Ejecuto el primer dia del mes
# scheduler.add_job(mostrar, 'cron', day=1, hour=0)
# trigger por intervalos
# scheduler.add_job(mostrar, 'interval', hours=2)
scheduler.add_job(holamundo, 'interval', seconds=10)
#scheduler.add_job(leer_bandeja, 'interval', minutes=1)

scheduler.print_jobs()
scheduler.start()

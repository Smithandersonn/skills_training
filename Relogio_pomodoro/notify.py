from winotify import Notification


notificacao = Notification(app_id="Alerta Timer", title="Notificação Relogio",
msg="Boas Noticias...Hora de descansar um Pouquinho!",duration="short")

notificacao.show()
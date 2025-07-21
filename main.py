import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def buscar_trajes():
    # Ejemplos simulados (luego lo mejoramos con scraping real)
    trajes = [
        {"nombre": "O'Neill Hyperfreak 4/3", "precio": 175, "url": "https://cleanlinesurf.com"},
        {"nombre": "Rip Curl Flashbomb 4/3", "precio": 180, "url": "https://realwatersports.com"},
    ]
    return trajes

def armar_resumen(trajes):
    resumen = "Trajes 4/3 mm hasta $180 USD:\n\n"
    for t in trajes:
        resumen += f"{t['nombre']} - ${t['precio']} - {t['url']}\n"
    return resumen

def enviar_mail(resumen, destinatario, remitente, password):
    msg = MIMEText(resumen)
    msg['Subject'] = "Resumen diario trajes de surf"
    msg['From'] = remitente
    msg['To'] = destinatario

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(remitente, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    trajes = buscar_trajes()
    resumen = armar_resumen(trajes)

    import os
    REMITENTE = os.getenv("EMAIL_SENDER")
    PASSWORD = os.getenv("EMAIL_PASSWORD")
    DESTINATARIO = os.getenv("EMAIL_RECEIVER")

    enviar_mail(resumen, DESTINATARIO, REMITENTE, PASSWORD)

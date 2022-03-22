
from flask import Flask
from datetime import datetime
from flask import jsonify
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# Funcion para el envio de correo


def send_mail(time, result):
    msg = MIMEText("prueba realizada a la hora " + time +
                   " dando como resultado: " + result)
    msg['Subject'] = 'PruebaProteccionFibonacci'
    recipients = ['juan.gomezh@proteccion.com.co',
                  'correalondon@gmail.com']
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv('email'), os.getenv('password'))
    server.sendmail(os.getenv('email'),
                    ['soupbizkit@gmail.com', 'waltersantacruzg@gmail.com'], msg.as_string())

# Retorna secuencia de fibonacci basado en os minutos de una hora dada.


@app.route('/', methods=['GET'])
def fibonacci():
    date_now = datetime.now()  # hora actual
    minutes = date_now.strftime("%M")  # se extraen los minutos
    seconds = date_now.second  # se extraen los segundos
    print(minutes)

    # Se obtienen los dos dígitos de los minutos
    fibo_sequence = [int(a) for a in str(minutes)]
    first_seed = fibo_sequence[0]
    second_seed = fibo_sequence[1]

    # cálculo de secuencia fibonacci
    for i in range(seconds):
        sum = first_seed + second_seed
        first_seed = second_seed
        second_seed = sum
        fibo_sequence.append(sum)

    date_time = date_now.strftime("%H:%M:%S")
    send_mail(date_time, str(fibo_sequence))
    print("hora: ", date_now)
    return jsonify(fibo_sequence), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

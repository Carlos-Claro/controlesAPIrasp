#################################
# Sistema de API para controle 
# de Temperatura e humidade
#################################
# Flask API,
# RaspberryPI, 
# Arduino,
# Nodered,
# MongoDB
# Apache
#################################
@author Carlos Claro 
@email carlosclaro79@gmail.com
# 

run app/resty.py

Armazenar dados coletados em arduino e raspberry pi gpio
em banco de dados MongoDB.
Servir dados via api para graficos armazenados em tabela 
unica e marcada por periodo, 
Servir dados de situação no momento, via arduino.

#

controle de iluminação, 
- rele in1 = jogo de lampadas 1
- rele in2 = Lampada individual
- rele in3 = ventilação ambiente
- rele in4 = aquecimento

Entradas de dados
- iterações com o ambiente - tipo de acao - chave - valor
- grafico de ação por tipo

Controle de temperatura, via arduino, ligado via serial
ao raspberry solicita dados do arduino da biblioteca:
https://github.com/Carlos-Claro/arduino.git monitor
 
- DHT11-1 = temperatura interna
- DHT11-2 = temperatura externa
- Sensor de iluminação interno
- Sensor de iluminação externo
- Sensor de chuva
- Higrometro H1
- Higrometro H2

#todo 
@todo
Controle de irrigação 
controle de evolução de plantas




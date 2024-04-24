import board
import digitalio
import time

# Konfiguration der Relais-Pins
relais_pins = [board.GP0, board.GP1, board.GP2]  # Hier die Pins für die Relais eintragen

# Konfiguration der Taster-Pins
taster_pins = [board.GP3, board.GP4, board.GP5]  # Hier die Pins für die Taster eintragen

# Initialisierung der Relais
relais = [digitalio.DigitalInOut(pin) for pin in relais_pins]
for r in relais:
    r.direction = digitalio.Direction.OUTPUT

# Initialisierung der Taster
taster = [digitalio.DigitalInOut(pin) for pin in taster_pins]
for t in taster:
    t.direction = digitalio.Direction.INPUT
    t.pull = digitalio.Pull.UP

# Schleife zur Tasterüberwachung
while True:
    for i, t in enumerate(taster):
        if not t.value:  # Wenn der Taster gedrückt wird
            relais[i].value = not relais[i].value  # Relais umschalten
            while not t.value:  # Warten bis der Taster losgelassen wird
                time.sleep(0.01)
    time.sleep(0.01)  # Kurze Pause für die CPU

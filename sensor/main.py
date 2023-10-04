import json 
import onewire
import ds18x20
import time
import machine



pico_id = machine.unique_id()
with open('confiq.json','r') as config_file:
    config_data = json.load(config_file)

pin = config_data.get("pin")
interval = config_data.get("interval")
ds_pin = machine.Pin(pin)
ds_sensor = ds18x20.DS18X20(onewire.Onewire(ds_pin))

roms = ds_sensor.scan() 
while True:
    ds_sensor.convert_temp()
    time.sleep_ms(interval)

    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print(f"{pico_id.hex()} {rom.hex ()} {temp:.2f}") 
   

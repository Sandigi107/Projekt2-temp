# Projekt2-temp 


---

# Temperaturavläsning med Raspberry Pi Pico och DS18B20-sensor

# Översikt

Detta projekt syftar till att skapa ett program som använder en Raspberry Pi Pico för att läsa av temperatursensorer (DS18B20) och visa mätresultaten i terminalen. Programmet kan hantera flera sensorer och ger utskrifter i formatet: <unit id> <sensor id> <mätvärde>. Med hjälp av en config.json-fil så kan vi se vilken pin vi ska använda samt vilket intervall vi ska ha mellan varje utskrift. 

# Installation

1. Ladda ner MicroPython till din Raspberry Pi Pico:

   - Anslut Pico till datorn.
   - Tryck på BOOTSEL-knappen på Pico och anslut den till datorn. Den visas som en USB-enhet.
   - Ladda ner MicroPython-firmware och överför den till Pico.

2. Kör koden med Thonny:

   - Öppna koden i din favorit-IDE. ex VSCode
   - Anslut Pico till datorn via USB.
   - Använd Thonny eller liknande program för att köra koden på Pico.

# Användning

- Koden läser av temperatursensorer och visar resultaten i terminalen i formatet: <unit id>  <mätvärde> <sensor id> 

- <unit id> är en unik identifierare för din Pico.
- <mätvärde> är den avlästa temperaturen.
- <sensor id> är en unik identifierare för varje ansluten temperatursensor.

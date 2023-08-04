import time
import board
import adafruit_bme680
import csv
import json
header = '[{"channel": "Population", "color": "Blue", "dataset": ['
footer='}]'

def convert_csv_to_json(csv_file, json_file):
    data = []  # Initialize an empty list to store the data from the CSV

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        next(reader)
        for row in reader:
            timestamp = row['Timestamp']
            temperature = row['Temperature']

            data.append({'x': timestamp, 'y': temperature})

    # Print the converted data


    # Write the JSON data with the header only
    with open(json_file, 'w') as file:
        file.write(header)
        for i, item in enumerate(data):
            file.write(json.dumps(item))
            if i != len(data) - 1:
                file.write(',')
        file.write(']}]')


csv_file = '/home/pi/Documents/bmedata.csv'
json_file = '/home/pi/Documents/filez.json'





i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25


# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
temperature_offset = -5
file_path = '/home/pi/Documents/bmedata.csv'
def write_header(file_path,headers):
        with open(file_path,'a',newline='') as csvfile:
           
            write=csv.writer(csvfile)
            write.writerow(headers)


def write_to_csv(file_path, data):
        with open(file_path,'a',newline='') as csvfile:
           
            writer = csv.writer(csvfile)
            writer.writerow(data)

global user_time
user_time = 5
start_time = time.time()

    # Run the loop for user specification
while time.time() - start_time <= user_time:
    time.sleep(1)
    print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    print("Trying to do csv")

  # check if the header is written
   

    # Write CSV header
   
   

    # Set the start time

        # Get the current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # Update your variables here
    temp_f = ((bme680.temperature + temperature_offset) * (9/5))+32
    gas = bme680.gas
    humidity = bme680.relative_humidity
    pressure = bme680.pressure
    altitude = bme680.altitude


        # Create a list with the data to write to CSV
    data = [timestamp, temp_f, gas, humidity, pressure, altitude]


    write_to_csv('/home/pi/Documents/bmedata.csv', data)


        # Write the data to the CSV file
   
       

    print("Saved to csv")
       
       

        # Call the function to convert CSV to JSON
       
       
       



convert_csv_to_json('/home/pi/Documents/bmedata.csv', '/home/pi/Documents/filez.json')

from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.aggregated_data import AggregatedData
import config


# Основну логіку, а саме file_datasource.py потрібно реалізувати
# самостійно. Перед читанням даних відкрити файли, при читанні
# зчитувати відповідний набір даних з файлів та повертати його.
class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
    ) -> None:
        self.acc_path = accelerometer_filename
        self.gps_path = gps_filename
        self.iter = 1
        self.acc_data = None
        self.gps_data = None
        print("INITIATION")
        print(self.acc_path)
        print(self.gps_path)

    def read(self) -> AggregatedData:
        """Метод повертає дані отримані з датчиків"""
        print("READING...")
        x, y, z = self.acc_data[self.iter]
        lon, lat = self.gps_data[self.iter]
        print(f"Cycle: {self.iter}")
        print("Accelerometer data:", self.acc_data[self.iter])
        print("GPS data:", self.gps_data[self.iter])
        self.iter += 1
        print("READING CYCLE COMPLETED\n")
        return AggregatedData(
            Accelerometer(x, y, z),
            Gps(lon, lat),
            datetime.now(),
            config.USER_ID,
        )

    def startReading(self):
        """Метод повинен викликатись перед початком читання даних"""
        print("OPENING FILES...")
        with open(self.acc_path, "r") as accel_file, open(
            self.gps_path, "r"
        ) as gps_file:
            self.acc_data = list(reader(accel_file))
            self.gps_data = list(reader(gps_file))
        print("OPENING FILES COMPLETED\n")

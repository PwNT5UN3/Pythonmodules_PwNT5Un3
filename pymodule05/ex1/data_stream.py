from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    '''An abstract datastream base class'''
    def __init__(self, stream_id: str) -> None:
        '''creates a datastream processor'''
        self.stream_id = stream_id
        self.stats: Dict[str, Union[str, int, float]] = {}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        '''processes a batch of data packets'''
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''
        filters data by excluding all entries
        that dont start with the given criteria optional
        '''
        result: List[Any] = []
        for item in data_batch:
            try:
                if str(item)[0:len(str(criteria))] == criteria or \
                   criteria is None:
                    result.append(str(item))
                else:
                    continue
            except Exception:
                continue
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''returns statistics built over the data processor lifetime'''
        return self.stats


class SensorStream(DataStream):
    '''A Datastream specialised on environmntal sensor data'''
    def __init__(self, stream_id: str) -> None:
        '''creates a sensor stream'''
        super().__init__(stream_id)
        self.stats['avg_temp'] = 0
        self.stats['avg_hum'] = 0
        self.stats['avg_pres'] = 0
        self.stats['total_temp'] = 0
        self.stats['total_hum'] = 0
        self.stats['total_pres'] = 0
        self.stats['temp_packets'] = 0
        self.stats['hum_packets'] = 0
        self.stats['pres_packets'] = 0
        self.stats['packets'] = 0
        self.stats['alerts'] = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        '''filters and processes environmental sensor data'''
        valid = []
        valid += super().filter_data(data_batch, 'temp:')
        valid += super().filter_data(data_batch, 'humidity:')
        valid += super().filter_data(data_batch, 'pressure:')
        for datapoint in valid:
            try:
                if datapoint[0:5] == 'temp:':
                    if float(datapoint[5:]) > float(self.stats['avg_hum']):
                        self.stats['alerts'] = int(self.stats['alerts']) + 1
                    self.stats['total_temp'] = int(self.stats['total_temp']) +\
                        int(datapoint[5:])
                    self.stats['temp_packets'] = \
                        int(self.stats['temp_packets']) + 1
                    self.stats['avg_temp'] = int(self.stats['total_temp']) / \
                        int(self.stats['temp_packets'])
                    self.stats['packets'] = int(self.stats['packets']) + 1
                elif datapoint[0:9] == 'humidity:':
                    self.stats['total_hum'] = int(self.stats['total_hum']) +\
                        int(datapoint[9:])
                    self.stats['hum_packets'] = \
                        int(self.stats['hum_packets']) + 1
                    self.stats['avg_hum'] = int(self.stats['total_hum']) / \
                        int(self.stats['hum_packets'])
                    self.stats['packets'] = int(self.stats['packets']) + 1
                elif datapoint[0:9] == 'pressure:':
                    self.stats['total_pres'] = int(self.stats['total_pres']) +\
                        int(datapoint[9:])
                    self.stats['pres_packets'] = \
                        int(self.stats['pres_packets']) + 1
                    self.stats['avg_pres'] = int(self.stats['total_pres']) / \
                        int(self.stats['pres_packets'])
                    self.stats['packets'] = int(self.stats['packets']) + 1
                else:
                    raise TypeError('unrecognised data')
            except Exception:
                continue
        return ('Sensor analysis: Packets processed: ' +
                f"{self.stats['packets']}, avg temp: " +
                f"{self.stats['avg_temp']}°C")

    def get_stats(self) -> Dict[str, str | int | float]:
        '''returns sensor data stats'''
        return super().get_stats()


class TransactionStream(DataStream):
    '''A datastrem specialised for order data'''
    def __init__(self, stream_id: str) -> None:
        '''creates the datastream'''
        super().__init__(stream_id)
        self.stats['net_flow'] = 0
        self.stats['large_orders'] = 0
        self.stats['orders'] = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''filters the order data'''
        valid: List[str] = []
        valid_buys = super().filter_data(data_batch, 'buy:')
        valid_sells = super().filter_data(data_batch, 'sell:')
        if criteria is not None:
            valid += super().filter_data(data_batch, criteria)
        for item in valid_buys:
            try:
                if int(item[4:]) > 0:
                    valid.append(item)
            except Exception:
                continue
        for item in valid_sells:
            try:
                if int(item[5:]) > 0:
                    valid.append(item)
            except Exception:
                continue
        return valid

    def process_batch(self, data_batch: List[Any]) -> str:
        '''processes a batch of orders'''
        valid = self.filter_data(data_batch)
        for order in valid:
            try:
                if order[0:4] == 'buy:':
                    if int(order[4:]) > 200:
                        self.stats['large_orders'] = \
                            int(self.stats['large_orders']) + 1
                    self.stats['net_flow'] = int(self.stats['net_flow']) +\
                        int(order[4:])
                    self.stats['orders'] = int(self.stats['orders']) + 1
                elif order[0:5] == 'sell:':
                    if int(order[5:]) > 200:
                        self.stats['large_orders'] = \
                            int(self.stats['large_orders']) + 1
                    self.stats['net_flow'] = int(self.stats['net_flow']) -\
                        int(order[5:])
                    self.stats['orders'] = int(self.stats['orders']) + 1
                else:
                    raise TypeError('unrecognised data')
            except Exception:
                continue
        if int(self.stats['net_flow']) < 0:
            return ('Sensor analysis: Orders processed: ' +
                    f"{self.stats['orders']}, net asset flow: " +
                    f"{self.stats['net_flow']}")
        else:
            return ('Sensor analysis: Orders processed: ' +
                    f"{self.stats['orders']}, net asset flow: +" +
                    f"{self.stats['net_flow']}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''returns financial stats'''
        return self.stats


class EventStream(DataStream):
    '''A Datastream processing log events'''
    def __init__(self, stream_id: str) -> None:
        '''creates the datastream'''
        super().__init__(stream_id)
        self.stats['events'] = 0
        self.stats['alerts'] = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        '''filters log data'''
        valid = []
        types = ['login', 'error', 'logout', criteria]
        for datapoint in data_batch:
            if datapoint in types:
                valid.append(datapoint)
        return valid

    def process_batch(self, data_batch: List[Any]) -> str:
        '''processes the different logs'''
        valid = self.filter_data(data_batch)
        for log in valid:
            if log == 'login':
                self.stats['events'] = int(self.stats['events']) + 1
            elif log == 'logout':
                self.stats['events'] = int(self.stats['events']) + 1
            elif log == 'error':
                self.stats['events'] = int(self.stats['alerts']) + 1
                self.stats['events'] = int(self.stats['events']) + 1
            else:
                continue
        return ('Sensor analysis: Events processed: ' +
                f"{self.stats['events']}, errors logged: +" +
                f"{self.stats['alerts']}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''returns event stats'''
        return self.stats


class StreamProcessor:
    '''A processor for stream data'''
    def __init__(self) -> None:
        '''creates the Processor'''
        self.sensor = SensorStream('ENV_PROC')
        self.broker = TransactionStream('FIN_PROC')
        self.log = EventStream("LOG_PROC")
        self.stats = {'sensor': 0, 'broker': 0, 'log': 0}

    def process_stream_all(self, data_batch: List[Any]) -> List[str]:
        '''processes the batch for all streams'''
        results = []
        results.append(self.sensor.process_batch(data_batch))
        results.append(self.broker.process_batch(data_batch))
        results.append(self.log.process_batch(data_batch))
        return results

    def process_stream_sprecific(self, data_batch: List[Any],
                                 stream: DataStream) -> str:
        '''processes the stream for one specific stream'''
        if isinstance(stream, SensorStream):
            self.stats['sensor'] += len(stream.filter_data(data_batch))
        elif isinstance(stream, TransactionStream):
            self.stats['broker'] += len(stream.filter_data(data_batch))
        elif isinstance(stream, EventStream):
            self.stats['log'] += len(stream.filter_data(data_batch))
        return stream.process_batch(data_batch)

    def print_proc_stats(self) -> None:
        '''prints processsor stats'''
        print(f" - Sensor data: {self.stats['sensor']} readings processed")
        print(f" - Transaction data: {self.stats['sensor']} orders processed")
        print(f" - Event data: {self.stats['sensor']} events processed")


def test_polymorphic_system() -> None:
    '''tests the streams'''
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor = SensorStream('SENSOR_001')
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    batch: List[Any] = ['temp:22.5', 'humidity:65', 'pressure:1013']
    print(sensor.process_batch(batch), end='\n\n')
    print("Initializing Transaction Stream...")
    broker = SensorStream('TRANS_001')
    print(f"Stream ID: {broker.stream_id}, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    batch = ['buy:100', 'sell:150', 'buy:75']
    print(broker.process_batch(batch), end='\n\n')
    print("Initializing Event Stream...")
    log = EventStream('EVENT_001')
    print(f"Stream ID: {log.stream_id}, Type: System Events")
    print("Processing event batch: [login, error, logout]")
    batch = ['login', 'error', 'logout']
    print(log.process_batch(batch), end='\n\n')


def test_stream_processing() -> None:
    '''tests the stream processor'''
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    processor = StreamProcessor()
    processor.process_stream_all(['temp:23', 'pressure:45', 'login', 'buy:40',
                                  'logout', 'error', 'sell:50',
                                  'sell:100', 'buy:1'])
    processor.print_proc_stats()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


def test_suite() -> None:
    '''runs all tests'''
    test_polymorphic_system()
    test_stream_processing()


if __name__ == "__main__":
    test_suite()

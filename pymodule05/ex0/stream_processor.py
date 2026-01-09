from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    '''Basic abstract base class'''
    @abstractmethod
    def process(self, data: Any) -> str:
        '''processes a datapoint'''
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        '''validates a datapoint'''
        pass

    def format_output(self, result: str) -> str:
        '''returns a formatted ouput string resulting from process()'''
        return f'Output: {result}'


class LogProcessor(DataProcessor):
    '''Processor for log entries'''
    def process(self, data: Any) -> str:
        '''processes a given log entry'''
        print(f'Processing data: {data}')
        if not self.validate(data):
            print('Validation: [WARNING] Log data could not be verified!')
            return super().format_output(f'Data ({data}) is not compatible')
        print('Validation: Log data verified')
        if str(data)[0:5] == 'ERROR':
            error = str(data)[7:]
            return super().format_output(f'[ALERT]: Error detected: {error}')
        elif str(data)[0:4] == 'INFO':
            info = str(data)[6:]
            return super().format_output(f'[INFO]: Log: {info}')
        else:
            log = str(data)
            return super().format_output(f'[LOG]: {log}')

    def validate(self, data: Any) -> bool:
        '''validates that the entry is a valid log entry'''
        log_types = ['ERROR', 'INFO:']
        try:
            log = str(data)
            if log[0:5] in log_types:
                return True
            raise ValueError(f'{log} is not a valid log type!')
        except Exception:
            return False


class TextProcessor(DataProcessor):
    '''processor for text inputs'''
    def process(self, data: Any) -> str:
        '''processes a text input'''
        print(f'Processing data: {data}')
        if not self.validate(data):
            print('Validation: [WARNING] Text data could not be verified!')
            return super().format_output(f'Data ({data}) is not compatible')
        print('Validation: Text data verified')
        text = str(data)
        return super().format_output('Processed test: ' +
                                     f'{len(text)} characters' +
                                     f', {len(text.split())} words')

    def validate(self, data: Any) -> bool:
        '''validates a text input'''
        try:
            str(data)
            return True
        except Exception:
            return False


class NumericProcessor(DataProcessor):
    '''processor for numeric inputs'''
    def process(self, data: Any) -> str:
        '''processes a numeric input'''
        data = self.flatten_data(data)
        print(f'Processing data: {data}')
        if not self.validate(data):
            print('Validation: [WARNING] Numeric data could not be verified!')
            return super().format_output(f'Data ({data}) is not compatible')
        print('Validation: Numeric data verified')
        return super().format_output(f'Processed {len(data)} numeric values,' +
                                     f' sum={sum(data)}, ' +
                                     f'avg={sum(data) / len(data)}')

    def validate(self, data: Any) -> bool:
        '''validates a numeric input'''
        try:
            for datapoint in data:
                int(datapoint)
            return True
        except TypeError:
            try:
                int(data)
                return True
            except Exception:
                return False
        except Exception:
            return False

    def flatten_data(self, data: Any) -> List[int]:
        '''flattens a list of numeric inputs for data compatability'''
        datapoints: List[List[int]] = []
        datapoints_flat: List[int] = []
        datapoints.append(data)
        try:
            datapoints_flat = [item for items in datapoints for item in items]
        except TypeError:
            datapoints_flat.append(data)
        return datapoints_flat


def interface(data: Any) -> str:
    '''a common interface and tree system for data streams'''
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    if numeric_processor.validate(data):
        return numeric_processor.process(data)
    elif log_processor.validate(data):
        return log_processor.process(data)
    elif text_processor.validate(data):
        return text_processor.process(data)
    else:
        return ('Unsupported Data!')


def data_stream_tester() -> None:
    '''a tester for the processors'''
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n')
    numeric_processor = NumericProcessor()
    print('Initialising Numeric Processor...')
    print(numeric_processor.process([1, 2, 3, 4, 5]), end='\n\n')
    text_processor = TextProcessor()
    print('Initialising Text Processor...')
    print(text_processor.process('Hello!'), end='\n\n')
    log_processor = LogProcessor()
    print('Initialising Log Processor...')
    print(log_processor.process('INFO: sdigfdsh'), end='\n\n')


def interface_tester() -> None:
    '''a tester for the interface system'''
    print('=== Polymorphic Processing Demo ===')
    print('Processing multiple datatypes through the same interface...')
    print(interface([1, 2, 3]))
    print(interface('Hello World!'))
    print(interface('ERROR: Testalert'))


def full_tester() -> None:
    '''a test suite wrapper'''
    data_stream_tester()
    interface_tester()
    print('\nFoundation systems online. Nexus ready for advanced streams')


if __name__ == '__main__':
    full_tester()

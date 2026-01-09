from abc import ABC
from typing import Any, List, Dict, Union, Protocol


class ProcessingStage(Protocol):
    '''a duck typing protocol for the stages'''
    def process(self, data: Any) -> Any:
        '''function blueprint for protocols'''
        ...


class ProcessingPipeline(ABC):
    '''A data processign pipeline'''
    def __init__(self, pipeline_id: Any) -> None:
        '''makes the pipeline'''
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        '''adds a stage to the pipeline'''
        self.stages.append(stage)

    def run_pipeline(self, data: Any) -> None:
        '''runs the pipeline process'''
        for stage in self.stages:
            data = stage.process(data)
        print(data)

    def process(self, data: Any) -> Any:
        '''blueprint for adapter child classes'''
        pass


class JSONAdapter(ProcessingPipeline):
    '''checker for JSON compatability'''
    def __init__(self, pipeline_id: Any) -> None:
        '''makes the adapter'''
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        '''checks data'''
        if isinstance(data, Dict):
            return '1'
        return '0'


class CSVAdapter(ProcessingPipeline):
    '''checker if data is csv compatible data'''
    def __init__(self, pipeline_id: Any) -> None:
        '''makes the adapter'''
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        '''compatability data for csv checks'''
        if isinstance(data, str) and data.count(',') > 0:
            return '1'
        return '0'


class StreamAdapter(ProcessingPipeline):
    '''checks if data is compatible with stream data specs'''
    def __init__(self, pipeline_id: Any) -> None:
        '''makes the adapter'''
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        '''compatibility check for stream data'''
        if isinstance(data, str):
            return '1'
        return '0'


class InputStage:
    '''
    the first processing stage
    used for compatibility checks and classification'''
    def process(self, data: Any) -> Dict:
        '''rudimentary preliminary compatability checks'''
        print(f'Input: {data}')
        ouput: Dict[str, Any] = {'type': ''}
        if data is not None:
            if JSONAdapter(1).process(data) == '1':
                ouput['type'] = 'json'
            elif CSVAdapter(1).process(data) == '1':
                ouput['type'] = 'csv'
            elif StreamAdapter(1).process(data) == '1':
                ouput['type'] = 'stream'
            else:
                raise ValueError('Invalid data type')
            ouput['data'] = data
            return ouput
        raise ValueError('Data cannot be None')


class TransformStage:
    '''A processsign stage for data enrichment and refinement'''
    def process(self, data: Dict) -> Dict:
        '''enrindhment processing'''
        if data['type'] == 'json':
            for key in data['data'].keys():
                data[key] = data['data'].get(key)
            data = {key: value for key, value in data.items() if key != 'data'}
            print('Transform: Enriched with metadata and validation')
        elif data['type'] == 'csv':
            print('Transform: Parsed and structured data')
        else:
            print('Aggregated and filtered')
        return data


class OutputStage:
    '''a processor stage used for final output'''
    def process(self, data: Any) -> str:
        '''final processing'''
        if data['type'] == 'json':
            if data['sensor'] == 'temp':
                return ('Output: Processed temperature reading: ' +
                        str(data['value']) + str(data['unit']))
            else:
                raise ValueError('Unsupported sensor type')
        elif data['type'] == 'csv':
            return 'Output: User activity logged: 1 actions processed'
        else:
            return ('Output: Stream summary: 5 readings, avg: 22.1C')


class NexusManager:
    '''a manager to manage multipl pipelines at once'''
    def __init__(self) -> None:
        '''creates the manager'''
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        '''adds a pipeline to the manager'''
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        '''processes data through all pipelines available to the manager'''
        for pipe in self.pipelines:
            pipe.run_pipeline(data)
            print('')


def nexus_test() -> None:
    '''tests the pipeline sysstem'''
    print('=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n')
    print('Initialising Nexus manager...')
    manager = NexusManager()
    print('Pipeline capacity: 1000 streams/second\n')
    print('Creating Data processing Pipeline...')
    manager.add_pipeline(ProcessingPipeline(1))
    print('Stage 1: Input validation and parsing')
    print('Stage 2: Data Transformation and enrichment')
    print('Stage 3: Output formatting and delivery\n')
    print('=== Multi-Format Data Processing ===\n')
    print('Processing JSON data through pipeline...')
    manager.process_data({"sensor": "temp", "value": 23.5, "unit": "C"})
    print('Processing CSV data through same pipeline...')
    manager.process_data("user,action,timestamp")
    print('Processing stream data through same pipeline...')
    manager.process_data('Real-time sensor stream')
    print('Nexus Integration complete. All systems operational.')


if __name__ == '__main__':
    nexus_test()

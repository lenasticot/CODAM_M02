from abc import ABC, abstractmethod
from typing import Any, Tuple, List
import typing


class DataProcessor(ABC):
    def __init__(self):
        self.items = []
        self.pos: int = -1
    @abstractmethod
    def validate(self, data: Any) -> bool:
        print(f"trying to validate input '{data}': ", end="")
    @abstractmethod
    def ingest(self, data: Any) -> None: 
        pass
    def output(self) -> tuple[int, str]:
        item = self.items[0]
        self.items.pop(0)
        self.pos += 1
        return (self.pos, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any):
        if isinstance(data, int):
            return True
        elif isinstance(data, float):
            return True
        elif isinstance(data, list):
            for i in data:
                if isinstance(i, int):
                    continue
                elif isinstance(i, float):
                    continue
                else:
                    return False
            return True
        return False
    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            print(f"Test invalid ingestion of string '{data}' without prior validation:")
            raise ValueError("Got exception: Improper numeric data")
        if isinstance(data, list):
            for d in data:
                self.items.append(str(d))
        else:
            self.items.append(str(data))

        print(f"Processing data: {self.items}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any):
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, str):
                    continue
                else:
                    return False
            return True
        else:
            return False
    def ingest(self, data: str | list) -> None:
        if not self.validate(data):
            print(f"Test invalid ingestion of data '{data}' without prior validation:")
            raise ValueError("Got exception: Improper string data")
        if isinstance(data, list):
            for d in data:
                self.items.append(d)
        else:
            self.items.append(data)
        print(f"Processing data: {self.items}")


class LogProcessor(DataProcessor):
    def validate(self, data: Any):
        if isinstance(data, dict):
            return True
        elif isinstance(data, list):
            for i in data:
                if isinstance(i, dict):
                    continue
                else:
                    return False
            return True
        else:
            return False
    def ingest(self, data:  dict | list):
        if not self.validate(data):
            print(f"Test invalid ingestion of data '{data}' without prior validation:")
            raise ValueError("Got exception: Improper dict data")
        if isinstance(data, list):
            for d in data:
                for key, value in d.items():
                    self.items.append(str(f"{key}: {value}"))
        else:
            for key, value in data.items():
                self.items.append(str(f"{key}: {value}"))

        print(f"Processing data: {self.items}")
  
class DataStream():
    # Will receive a stream of data containing different types
    # and then will route each element to the appropriate data processor
    # using polymorphic behavior
    def __init__(self):
        self.processors = []
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        print(f"Processor {type(proc).__name__} has been added correctly")
    def process_stream(self, stream: list[typing.Any]) ->None:

        for data in stream:   
            flag = 0
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    print(f"{data} has been correctly handled by {type(proc).__name__}")
                    flag = 1
                    break
            if flag == 0:
                print(f"{data} cannot be handled by your currrent processors")
    def print_processors_stats(self) -> None:
        # method in order to print stream statistics
        pass

def main():
    print("=== Code Nexus - Data Stream ===")
    # need to initialize the data processor that will be used after in the process stream
    test1 = DataStream()
    test = ["Bonjour", 8, [42, "fool"], [48, 15, 16, 23, 42], ["on", "a", "pas", "eleve", "les", "cochons", "ensemble"]]
    print("Registering Processors...")
    test1.register_processor(NumericProcessor())
    test1.register_processor(LogProcessor())
    test1.process_stream(test)
    
    
main()


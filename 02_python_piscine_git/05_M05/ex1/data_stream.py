from abc import ABC, abstractmethod
from typing import Any, List
import typing


class DataProcessor(ABC):
    def __init__(self):
        self.items: List = []
        self.pos: int = -1
        self.total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        print(f"trying to validate input '{data}': ", end="")

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        if not self.items:
            return
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
            print(
                  f"Test invalid ingestion of string '{data}' "
                  "without prior validation:"
                 )
            raise ValueError("Got exception: Improper numeric data")
        if isinstance(data, list):
            for d in data:
                self.items.append(str(d))
                self.total += 1
        else:
            self.items.append(str(data))
            self.total += 1

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
            print(
                  f"Test invalid ingestion of data '{data}'"
                  " without prior validation:"
                 )
            raise ValueError("Got exception: Improper string data")
        if isinstance(data, list):
            for d in data:
                self.items.append(d)
                self.total += 1
        else:
            self.items.append(data)
            self.total += 1
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
            print(
                  f"Test invalid ingestion of data '{data}'"
                  " without prior validation:"
                 )
            raise ValueError("Got exception: Improper dict data")
        if isinstance(data, list):
            for d in data:
                for key, value in d.items():
                    self.items.append(str(f"{key}: {value}"))
                    self.total += 1
        else:
            for key, value in data.items():
                self.items.append(str(f"{key}: {value}"))
                self.total += 1
        print(f"Processing data: {self.items}")


class DataStream():
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        print(f"Processor {type(proc).__name__} has been added correctly")

    def process_stream(self, stream: list[typing.Any]) -> None:
        if not stream:
            print("Error: cannot process an empty list")
            return
        if not self.processors:
            print(
                  "No processor found. Impossible to process the data"
                 )
            return
        for data in stream:
            flag = 0
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    print(
                          f"{data} has been correctly "
                          f"handled by {type(proc).__name__}"
                         )
                    flag = 1
                    break
            if flag == 0:
                print(
                      f"'{data}' cannot be handled by "
                      "your currrent processors"
                     )

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self.processors:
            print("No processor found, no data\n")
        for proc in self.processors:
            print(
                  f"{type(proc).__name__} : total "
                  f"{proc.total} processed, remaining "
                  f"{len(proc.items)} on processor"
                 )


def main():
    print("=== Code Nexus - Data Stream ===")
    print("Initialize data stream...")
    print()
    test1 = DataStream()
    test1.print_processors_stats()
    test = [
            "Bonjour", 8, [42, "fool"],
            [48, 15, 16, 23, 42],
            ["on", "a", "pas", "eleve", "les", "cochons", "ensemble"]
           ]
    print(f"Send first batch of data on stream: {test}")
    print()
    test1.process_stream(test)
    print()

    print("Registering Processors...")
    test1.register_processor(NumericProcessor())
    test1.register_processor(LogProcessor())
    print()
    test1.process_stream(test)
    print()
    print("Sending empty batch of data on stream")
    test2 = []
    test1.process_stream(test2)
    test1.print_processors_stats()
    test3 = [
             42, {'machin': 'truc'}, "oui",
             ["oui", "oui", "oui"],
             [
                {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
             ]
            ]
    print(f"Send second batch of data on stream: {test3}")
    print()
    test1.process_stream(test3)
    test1.print_processors_stats()
    print()

    for processor in test1.processors:
        x = 5
        print(f"Extracting {x} values from {type(processor).__name__}...")
        for y in range(0, x):
            a, b = processor.output()
            print(f"Text Value {a}: {b}")
    print()
    test1.print_processors_stats()


main()

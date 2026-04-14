from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.items = []
        self.pos: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.items:
            raise IndexError("No items left to extract")
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
                  f"Test invalid ingestion of string '{data}'"
                  " without prior validation:"
                 )
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
            print(
                  f"Test invalid ingestion of data '{data}'"
                  " without prior validation:"
                 )
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
            print(
                  f"Test invalid ingestion of data '{data}'"
                  " without prior validation:"
                 )
            raise ValueError("Got exception: Improper dict data")
        if isinstance(data, list):
            for d in data:
                for key, value in d.items():
                    self.items.append(str(f"{key}: {value}"))
        else:
            for key, value in data.items():
                self.items.append(str(f"{key}: {value}"))

        print(f"Processing data: {self.items}")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR ===\n")
    print("Testing Numeric Processor ...")
    test_1 = NumericProcessor()
    test = [4, 8, [42, "fool"], [48, 15, 16, 23, 42], "oui"]
    for items in test:
        print(f"Trying to validate input '{items}': ", end="")
        print(test_1.validate(items))
    print()
    for items in test:
        try:
            test_1.ingest(items)
        except ValueError as e:
            print(e)
    print()
    x = 3
    print(f"Extracting {x} values...")
    for y in range(0, x):
        try:
            a, b = test_1.output()
            print(f"Numeric value {a}: {b}")
        except IndexError as e:
            print(e)
    print()

    test_2 = TextProcessor()
    test2 = [
            "Bonjour", 8, [42, "fool"],
            [48, 15, 16, 23, 42],
            ["on", "a", "pas", "eleve", "les", "cochons", "ensemble"]
           ]

    print("Testing Text Processor ...")
    for items in test2:
        print(f"Trying to validate input '{items}': ", end="")
        print(test_2.validate(items))
    print()
    for items in test2:
        try:
            test_2.ingest(items)
        except ValueError as e:
            print(e)
    print()

    x = 3
    print(f"Extracting {x} values...")
    for y in range(0, x):
        try:
            a, b = test_2.output()
            print(f"Text Value {a}: {b}")
        except IndexError as e:
            print(e)

    print()

    test_3 = LogProcessor()
    test3 = [
             42, {'machin': 'truc'}, "oui",
             ["oui", "oui", "oui"],
             [
                {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
             ]
            ]
    print("Testing Log Processor ...")
    for items in test3:
        print(f"Trying to validate input '{items}': ", end="")
        print(test_3.validate(items))
    print()
    for items in test3:
        try:
            test_3.ingest(items)
        except ValueError as e:
            print(e)
    x = 3
    print()
    print(f"Extracting {x} values...")
    for y in range(0, x):
        try:
            a, b = test_3.output()
            print(f"Log value {a}: {b}")
        except IndexError as e:
            print(e)
    print()


main()

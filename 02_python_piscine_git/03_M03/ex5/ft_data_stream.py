import random
import time


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    nb = 2
    while True:
        count = 0
        for a in range(1, nb + 1):
            if nb % a == 0:
                count += 1
        if count == 2:
            yield nb
        nb += 1


def generator_demo():
    print("=== Generator demonstration ===")
    gen = fibonacci()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(gen), end=" ")
    p = prime()
    print("\nPrime number (first 5)", end=" ")
    for _ in range(5):
        print(next(p), end=" ")


def game_data(count):
    players = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', "Patrick"]
    levels = [4, 8, 12, 15, 16, 23, 42]
    event_types = ['login', 'logout', 'killed monster',
                   'died stupidly', 'leveled_up',
                   'item_found: potion', 'found love']

    for i in range(count):
        yield {
            "player": random.choice(players),
            "level": random.choice(levels),
            "type": random.choice(event_types),
            "event_num": i + 1
        }


def main():
    event = 1000
    print("=== Game Data Stream Processor ===\n")
    high_level = 0
    love = 0
    death = 0
    start = time.time()
    print(f"Processing {event} game events...")
    for events in game_data(event):
        if events['event_num'] <= 3:
            print(f"Event {events['event_num']}: "
                  f"Player {events['player']} (level {events['level']}) "
                  f"{events['type']}")
        if events['level'] >= 10:
            high_level += 1
        if events['type'] == "died stupidly":
            death += 1
        if events['type'] == "found love":
            love += 1

    if event > 3:
        print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {events["event_num"]}")
    print(f"High-level players (10+): {high_level}")
    print(f"{love} found love in a hopeless place")
    print(f"{death} died in mysterious circumstances...")
    print("")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time {time.time() - start:.3f}")
    print("")
    generator_demo()


main()

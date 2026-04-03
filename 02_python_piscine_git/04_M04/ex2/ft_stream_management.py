import sys


def inputs():
    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    return arch_id, status


def streams(i, s):
    sys.stdout.write(f"[STANDARD] Archive status from {i}: {s}\n")
    sys.stdout.flush()
    sys.stderr.write(
        "[ALERT] System diagnostic: "
        "Communication channels verified\n"
        )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.flush()


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    i, s = inputs()
    streams(i, s)
    print()
    sys.stdout.write("Three-channel communication test successful")


main()

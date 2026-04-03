def reading():
    with open("../new_discovery.txt", "r") as f:
        content = f.read()
    print(content)


def create_file():
    print("Initializing new storage unit: new_discovery.txt")
    try:
        with open("../new_discovery.txt", "x", encoding="utf-8") as f:
            print("Storage unit created successfully...\n")
            f.write(
                "Inscribing preservation data...\n"
                "[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee\n"
                )
    except FileExistsError:
        print("Error creating the file: it already exist\n")
        return
    reading()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{f.name}' ready for long-term preservation")


def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_file()


main()

def reading_file():
    print("Accessing Storage Vault: ancien_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    print("Connexion established...\n"
          "\nRECOVERED DATA:")
    content = file.read()
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")
    file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    reading_file()


main()
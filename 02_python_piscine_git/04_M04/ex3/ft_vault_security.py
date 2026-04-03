# to change
def updating_operation(file):
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(
                "\n[CLASSIFIED] New security protocols archived\n"
                "Vault automatically sealed upon completion"
                )
    except FileNotFoundError:
        print("Error File not found\n")
        return


def reading_operation(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Error File not found\n")
        return


def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:")
    reading_operation("../classified_data.txt")
    print("\nSECURE PRESERVATION:")
    updating_operation("../security_protocols.txt")
    reading_operation("../security_protocols.txt")
    print("\nAll vault operations completed with maximum security")


main()

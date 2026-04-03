# to add corrupted archives

def crisis_alert(doc):
    if doc == "standard_archive":
        print(f"ROUTINE ACCESS: Attempting access to {doc}")
    else:
        print(f"CRISIS ALERT: Attempting access to {doc}")
    try:
        with open(doc, "r", encoding="utf -8") as f:
            content = f.read()
            print(f"SUCESS: Archives recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: An error occured: {type(e).__name__}")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_alert("../lost_archive.txt")
    print()
    crisis_alert("../classified_vault.txt")
    print()
    crisis_alert("../standard_archive.txt")


main()

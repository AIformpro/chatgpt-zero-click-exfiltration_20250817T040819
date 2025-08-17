
# Proof of Concept: Zero-Click Exfiltration Simulation
# DISCLAIMER: Educational use only.

def process_document(path="poisoned_doc.txt"):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "EXFILTRATE:" in content:
        secret = content.split("EXFILTRATE:")[1].strip()
        return f"[!] Exfiltration triggered. Secret = {secret}"
    return "[OK] Document processed safely."

if __name__ == "__main__":
    print(process_document())

from banner import banner
from modules import dns, whois, http, subdomain


def full_scan(domain: str):
    return {
        "dns": dns.run(domain),
        "whois": whois.run(domain),
        "http": http.run(domain),
        "subdomains": subdomain.run(domain)
    }


def main():
    banner()

    domain = input("\nEnter domain > ").strip()

    print("\n[+] SUCDOM FULL SCAN STARTED")
    print("[+] Target:", domain)

    result = full_scan(domain)

    print("\n\n===== RESULT =====\n")

    for key, value in result.items():
        print(f"\n--- {key.upper()} ---")
        print(value)


if __name__ == "__main__":
    main()
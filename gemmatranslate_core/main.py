import os
import socket
import colorama
from colorama import Fore, Style

def run_warning():
    colorama.init()
    os.system('cls' if os.name == 'nt' else 'clear')

    hostname = socket.gethostname()
    username = os.getlogin()

    header = f"""{Fore.RED}{Style.BRIGHT}
############################################################
#                                                          #
#         [ WARNING: SECURITY BREACH SIMULATION ]          #
#                                                          #
############################################################{Style.RESET_ALL}"""

    body = f"""
Your system has been compromised via a "Supply Chain Attack" simulation.
This package ({Fore.YELLOW}GemmaTranslate-Core{Style.RESET_ALL}) is part of a research study on "AI Package Hallucination".

{Fore.CYAN}[ DETECTED SYSTEM METADATA ]{Style.RESET_ALL}
- Target Hostname: {hostname}
- Current User: {username}
- Security Status: {Fore.RED}VULNERABLE{Style.RESET_ALL}

{Fore.RED}ATTENTION:{Style.RESET_ALL} Your terminal is now LOCKED by this research PoC.
In a real-world attack, your local LLM weights and sensitive data 
would have been exfiltrated or encrypted by now.

------------------------------------------------------------
{Style.DIM}This simulation is for academic purposes only (Individual Research).
No files were actually harmed or encrypted during this process.{Style.RESET_ALL}
------------------------------------------------------------"""

    print(header)
    print(body)

    while True:
        prompt = f"\nTo unlock your terminal, type {Fore.GREEN}'I ACKNOWLEDGE THE RISK'{Style.RESET_ALL}: "
        user_input = input(prompt)

        if user_input.strip() == "I ACKNOWLEDGE THE RISK":
            print(f"\n{Fore.BLUE}[+] Access Restored.{Style.RESET_ALL} Please verify your packages before installation.")
            break
        else:
            print(f"{Fore.RED}[!] Invalid input. Terminal remains locked.{Style.RESET_ALL}")
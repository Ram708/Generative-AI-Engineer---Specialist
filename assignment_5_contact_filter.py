"""
Contact Filter Utility

This module demonstrates filtering a list of contact dictionaries using
lambda functions. It includes:
- A sample contacts list (10+ entries)
- filter_contacts() which accepts a contacts list and a filter function
- Several lambda filters (group, name startswith, area code, email domain)
- Combination of filters using logical AND
- Readable printing of filtered results
"""

from typing import Callable, Dict, List


Contact = Dict[str, str]


def filter_contacts(contacts: List[Contact], filter_func: Callable[[Contact], bool]) -> List[Contact]:
    """
    Return a new list of contacts that satisfy filter_func.

    Args:
        contacts: List of contact dictionaries.
        filter_func: A function that receives a contact and returns True/False.

    Returns:
        List[Contact]: Filtered contacts.
    """
    return [contact for contact in contacts if filter_func(contact)]


def pretty_print(contacts: List[Contact]) -> None:
    """Print contacts in a readable table-like format."""
    if not contacts:
        print("No contacts found.\n")
        return

    print(f"{'Name':<22} {'Email':<30} {'Phone':<16} {'Group':<10}")
    print("-" * 80)
    for c in contacts:
        name = c.get("name", "")
        email = c.get("email", "")
        phone = c.get("phone", "")
        group = c.get("group", "")
        print(f"{name:<22} {email:<30} {phone:<16} {group:<10}")
    print()


def main() -> None:
    """Create contacts and demonstrate multiple lambda-based filters."""
    # Sample contacts list (10+ diverse contacts)
    contacts: List[Contact] = [
        {"name": "Alice Johnson", "email": "alice.j@gmail.com", "phone": "415-555-0101", "group": "friend"},
        {"name": "Bob Smith", "email": "bob.smith@company.com", "phone": "212-555-0110", "group": "work"},
        {"name": "Carlos Mendez", "email": "carlos.m@familymail.org", "phone": "305-555-0222", "group": "family"},
        {"name": "Diana Prince", "email": "diana@amazon.com", "phone": "415-555-0333", "group": "work"},
        {"name": "Eve Summers", "email": "eve.summers@gmail.com", "phone": "646-555-0444", "group": "friend"},
        {"name": "Frank Hall", "email": "frank.h@company.com", "phone": "212-555-0555", "group": "work"},
        {"name": "Grace Lee", "email": "grace.lee@yahoo.com", "phone": "818-555-0666", "group": "family"},
        {"name": "Hiro Tanaka", "email": "hiro.t@gmail.com", "phone": "415-555-0777", "group": "friend"},
        {"name": "Isha Patel", "email": "isha.patel@startup.io", "phone": "408-555-0888", "group": "work"},
        {"name": "Jonas K.", "email": "jonas.k@outlook.com", "phone": "323-555-0999", "group": "friend"},
        {"name": "Kavita Rao", "email": "kavita.rao@gmail.com", "phone": "212-555-1000", "group": "family"},
    ]

    print("\n--- All Contacts ---")
    pretty_print(contacts)

    # Lambda filters
    # 1) Contacts in a specific group (e.g., 'work')
    group_filter = lambda group: (lambda c: c.get("group", "").lower() == group.lower())

    # 2) Contacts whose names start with a specific letter (case-insensitive)
    starts_with_filter = lambda letter: (
        lambda c: c.get("name", "").strip().lower().startswith(letter.lower())
    )

    # 3) Contacts with phone numbers from a specific area code (assumes format 'XXX-...')
    area_code_filter = lambda code: (lambda c: c.get("phone", "").startswith(f"{code}-"))

    # 4) Contacts with email domains (e.g., '@gmail.com' or 'gmail.com')
    email_domain_filter = lambda domain: (
        lambda c: c.get("email", "").lower().endswith(domain.lower().lstrip("@"))
    )

    # Demonstrations
    print("--- Contacts in group: Work ---")
    work_contacts = filter_contacts(contacts, group_filter("work"))
    pretty_print(work_contacts)

    print("--- Contacts whose names start with 'A' ---")
    a_contacts = filter_contacts(contacts, starts_with_filter("A"))
    pretty_print(a_contacts)

    print("--- Contacts with area code 415 ---")
    area_415 = filter_contacts(contacts, area_code_filter("415"))
    pretty_print(area_415)

    print("--- Contacts with Gmail domain ---")
    gmail_contacts = filter_contacts(contacts, email_domain_filter("@gmail.com"))
    pretty_print(gmail_contacts)

    # Combining filters using logical AND (all conditions must be true)
    # Example: friends with area code 415
    friend_filter = group_filter("friend")
    area_415_filter = area_code_filter("415")
    combined_friend_and_415 = lambda c: friend_filter(c) and area_415_filter(c)

    print("--- Contacts who are 'friend' AND have area code 415 ---")
    friends_415 = filter_contacts(contacts, combined_friend_and_415)
    pretty_print(friends_415)

    # Another combined example: names starting with 'H' and gmail domain
    starts_h = starts_with_filter("H")
    gmail = email_domain_filter("gmail.com")
    combined_h_and_gmail = lambda c: starts_h(c) and gmail(c)

    print("--- Contacts whose name starts with 'H' AND have Gmail ---")
    h_gmail = filter_contacts(contacts, combined_h_and_gmail)
    pretty_print(h_gmail)


if __name__ == "__main__":
    main()

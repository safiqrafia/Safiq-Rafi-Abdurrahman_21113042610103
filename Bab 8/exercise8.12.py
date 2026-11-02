def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('daging sapi', 'keju slice', 'selada', 'sosis')
make_sandwich('telur mata sapi', 'tomat', 'saus sambal')
make_sandwich('susu kental manis', 'meses')
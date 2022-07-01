prices = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

print(f"""Price of ASUS: {prices.get("ASUS")}""")

inp = input("Input a brand (must be capitalized): ")
print(f"""Price of {inp}: {prices.get(inp)}""") 
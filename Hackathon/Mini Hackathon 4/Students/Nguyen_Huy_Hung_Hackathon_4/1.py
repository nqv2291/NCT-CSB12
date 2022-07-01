laptops = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

print(f"""Available MACBOOKs: {laptops.get("MACBOOK")}""")

inp = input("Input a brand (must be capitalized): ")
print(f"""Available {inp}s: {laptops.get(inp)}""") 
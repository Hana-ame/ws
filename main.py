import handlers

print()
print("===")
print()


print(handlers.get("1") is None)
print(handlers.get("echo") is None)
print(handlers.get("echo")(" is None?"))
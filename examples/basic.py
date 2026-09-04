from pytoolkit import coalesce, ensure_list

print(coalesce(None, "ready"))
print(ensure_list("python"))
print(ensure_list([1, 2, 3]))

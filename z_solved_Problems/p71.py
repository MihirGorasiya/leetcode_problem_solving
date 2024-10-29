path = "/home//foo/"
path = "/home/user/Documents/../Pictures"
# path = "/.../a/../b/c/../d/./"
# path = "/../.../a/../b/c/../d/./"

dirs = []
splittedPath = path.split("/")

for path in splittedPath:
    if path == "..":
        if len(dirs) > 0:
            print(f"Poped: {dirs.pop()}")
    elif path == ".":
        continue
    elif path != "":
        dirs.append(path)

res = "/"+"/".join(dirs)

print(res)

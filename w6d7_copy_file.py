# Copy Content of One File to Another

# Approach#1
# with open("my-file.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         with open("my-clean-file.txt", 'a') as t:
#             t.write(line)

#Approach#2
with open("my-clean-file.txt", 'a+') as w:
    w.seek(0)
    if w.read():
        w.write("\n")

with open("my-file.txt", 'r') as f, open("my-clean-file.txt", 'a') as t:
    t.writelines(f.readlines())
    
with open("my-clean-file.txt", 'r') as handle:
    new_result = handle.readlines()
    print(new_result)   
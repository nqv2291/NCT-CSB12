link_1 = r"https://teams.microsoft.com/l/team/19%3axA8LfZCuuhFNt7eo0N7Zc2wgzrfxxI9tndiq5pxoweU1%40thread.tacv2/conversations?groupId=f2e81fee-acb0-491c-9137-a0f4e0d0ca40&tenantId=06f1b89f-07e8-464f-b408-ec1b45703f31"
link_2 = r"https://teams.microsoft.com/l/team/19%3akPhBsBt0uhdpb0-WGHq57oQbCLC3tlbN8OVHRGPT2Rk1%40thread.tacv2/conversations?groupId=11581fd9-58c4-4d56-b066-6b032f5d6af0&tenantId=06f1b89f-07e8-464f-b408-ec1b45703f31"

len = len(link_1)
comp = []
for i in range(len):
    if link_1[i] == link_2[i]:
        comp.append("_")
    elif comp[-1] == "_":        
        comp.pop()
        comp.append(link_1[i-1])
    else:
        comp.append("!")
print("".join(comp))
print(link_1)
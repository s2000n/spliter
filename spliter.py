def split_text(text, num_parts):
    part_length = len(text) // num_parts
    parts = [text[i:i + part_length] for i in range(0, len(text), part_length)]

    if len(parts) > num_parts:
        parts[-2] += parts[-1]
        parts.pop()

    for i, part in enumerate(parts, start=1):
        print(f"\n\npart{i}: {part}")

    return parts

text = input("Enter the text to split: ")
num_parts = int(input("Enter the number of parts: "))

result = split_text(text, num_parts)

input()
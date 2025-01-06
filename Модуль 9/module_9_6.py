def all_variants(text: str)->str:
    for i in range(1, len(text) + 1):
        fin = len(text) - i + 1
        for j in range(fin):
            string = text[j:j + i]
            yield string


if __name__ == "__main__":
    a = all_variants
    for i in a("abc"):
        print(i)

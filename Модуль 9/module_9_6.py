def all_variants(text):
	for i in range(1, len(text)+1):
		fin=len(text)-i+1
		for j in range(fin):
			string = text[j:j+i]
			yield string

if __name__ == "__main__":
 for i in all_variants("abc"):
	 print(i)
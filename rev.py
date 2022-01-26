def reverseString(str):
	#Write your code here.
    sp=str.split()
    new=sp[::-1]
    ans=" ".join(new)
    return ans

print(reverseString("I am doing good here"))
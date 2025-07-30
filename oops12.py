'''code to create a class of vowel_mask where vowels in the text must be mnased with consonents,
create a getitem and setitem for accessing the vowels in the text ":
input: 'education'
output: ' d*c*t**n'''

class vowelmask:
    def __init__(self, text):
        self.text=text
    def __getitem__(self, index):
        return self.text[index]
    def __setitem__(self, index, value):
        self.text[index]=value
    def mask_vowels(self):
        for i, ch in enumerate(self.text):
            if ch.lower() in 'aeiou':
                self[i]='*'
    def get_string(self):
       return ' '.join(self.text)
vm=vowelmask("education")
print('original:', ' '.join(vm.text))
vm.mask_vowels()
print("Masked:", vm.get_string())
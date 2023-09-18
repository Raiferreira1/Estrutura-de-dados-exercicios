from Stack import Stack

Pilha = Stack()

Pilha.push(1)
Pilha.push(2)
Pilha.push(3)
Pilha.push(4)

# print(Pilha)

#Crie um programa que verifique se os delimitadores de uma expressão matemática estão corretamente dispostos.
def isMathExpressionValid(self, expression):
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = Stack()

        for char in expression:
            if char in brackets.values():
                stack.push(char)
            elif char in brackets.keys():
                if stack.is_empty() or stack.pop() != brackets[char]:
                    return False
            else:
                continue

        return stack.is_empty()






#Crie um programa que verifique se um código HTML tem as tags balanceadas.

def isHtmlValid(html):
    stack = Stack()
    begin = end = 0
    valid_tags = {'body', 'h1', 'center', 'p', 'ol', 'li'}
    

    if not html.startswith('<'):
        return False
    
    while True:
        begin = html.find('<', end)
        end = html.find('>', begin + 1)
        
        if begin == -1 or end == -1:
             break
        
        tag = html[begin:end + 1]

        if tag[1] != '/':
            if tag[1:-1] not in valid_tags:
                return False
            
            stack.push(tag)

        else:
            if stack.is_empty() or stack.pop() != tag.replace('/',''):
                return False

    return stack.is_empty() 




# Mostre como uma pilha pode ser usada para determinar se a string é um palíndromo.
def isPalindrome(string):
    string = string.lower()  
    stack = Stack()

   
    for char in string:
        if char.isalnum():
            stack.push(char)


    for char in string:
        if char.isalnum() and char != stack.pop():
            return False

    return True



""" RGB to hex colors """

# def rgb(r, g, b):
#     # your code here :)
    
#     r = max(0, min(r, 255))
#     g = max(0, min(g, 255))
#     b = max(0, min(b, 255))    
    
    
#     r1 = int(r/16)
#     r2 = r%16
#     g1 = int(g/16)
#     g2 = g%16
#     b1 = int(b/16)
#     b2 = b%16

#     hex_value = [r1, r2, g1, g2, b1, b2]

    
    

#     conv = {
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }

#     def convert(value):
#         if value < 10:
#             return str(value)
#         else:
#             return conv[value]
        
#     hex_value = convert(r1) + convert(r2) + convert(g1) + convert(g2) + convert(b1) + convert(b2)

#     return hex_value

# print(rgb(-20, 0, 0))

""" Pig latin converter """

# def pig_it(text):
#     #your code here
#     sentence = text.split()

#     def alpha_check(word):
#         if word.isalpha():
#             return word[1:] + word[0] + 'ay'
#         else:
#             return word
        
#     pigified = [alpha_check(i) for i in sentence]

#     new_sent = " ".join(pigified)

#     return new_sent
    

# text='screw you guys im going home !'
# print(pig_it(text))
bus=['ibp',"bongloor","mangalpalli","yamjal","bn reddy"]

stop='magalpalli'
skip='bongloor'

for x in bus:
    if x=='mangalpalli':
        print(f'{x} has reached the stop')
    elif x==skip:
        print(f'{x} is skipped')
   
    print(f"{x} has crossed ")
      
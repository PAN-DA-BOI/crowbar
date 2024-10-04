attack_numb = input("What attack number is this? ")
attack_name = input("name of attack? ")

with open('output.txt', 'a') as f:
    f.write(f'def attack_page_{attack_numb}():\n')
    f.write('    page(root, \'blue\', \'green\')\n')
    f.write(f'    label = tk.Label(root, text=\'{attack_name}\', bg=\'blue\', fg=\'white\')\n')
    f.write('    label.pack(fill=\'x\')\n')
    f.write(f'    attack_button(root, \'START ATTACK\', \'green\', \'./rawattackscripts/attack_{attack_numb}_script.sh\')\n')
    f.write('    button(root, \'Back to Attacks\', \'black\', attacks_page)\n\n')

import tkinter as tk
import subprocess
import socket


colors = ['black', 'green', 'blue', 'white']

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
  
def page(root, bg_color, btn_color):
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg=bg_color)

def button(root, name, color, command):
    btn = tk.Button(root, text=name, bg=color, command=command, height=2, width=320)
    btn.pack()
    
def attack_button(root, name, color, command):
    var1 = tk.StringVar()
    entry1 = tk.Entry(root, textvariable=var1)
    entry1.pack()
    var2 = tk.StringVar()
    entry2 = tk.Entry(root, textvariable=var1)
    entry2.pack()
    def run_command():
        subprocess.call([command, var1.get(), var2.get()])
    btn = tk.Button(root, text=name, bg=color, command=run_command, height=2, width=320)
    btn.pack()

#attacks
def attack_page_1():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='nmap webpage',font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='input = ip', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_1_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_2():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='searchsploit',font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='input = ip, port', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_2_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
def attack_page_3():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Port scanning', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_3_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_4():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Vulnerability scanning', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_4_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_5():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Web application scanning', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_5_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_6():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Password cracking', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_6_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_7():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='SQL injection', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_7_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_8():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Directory brute forcing', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_8_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_9():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Wireless network scanning', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_9_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_10():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Password policy testing', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_10_script.sh')
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
    

def quit_page():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Are you sure you want to quit?', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    button(root, 'Confirm Quit', 'red', root.destroy)
    button(root, 'Return to Main Menu', colors[2], main_menu)
    
def attacks_page():
    page(root, colors[0], colors[1])
    button(root, 'NMAP webpage', colors[1], attack_page_1)
    button(root, 'Searchsploit', colors[1], attack_page_2)
    button(root, 'Port scanning', colors[1], attack_page_3)
    button(root, 'Vulnerability scanning', colors[1], attack_page_4)
    button(root, 'Web application scanning', colors[1], attack_page_5)
    button(root, 'Password cracking', colors[1], attack_page_6)
    button(root, 'SQL injection', colors[1], attack_page_7)
    button(root, 'Directory brute forcing', colors[1], attack_page_8)
    button(root, 'Wireless network scanning', colors[1], attack_page_9)
    button(root, 'Password policy testing', colors[1], attack_page_10)
    button(root, 'Back to Main Menu', colors[2], main_menu)


def about_page():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='this tool was made by Brody Evans\n to pentest servers, routers, \ncomputers, and more',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='CONTACT\n\nemail : brodyevans82Gmail.com\nphone : +1-385-235-1339\ngithub: PAN-DA-BOI\n\nSoftware Version 1.8.12', bg=colors[0], fg=colors[3], justify='left')
    label.pack(fill='x')
    button(root, 'Back to Main Menu', colors[2], main_menu)
    

def disguises_page():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Disguises', font=('Arial', 25), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    button(root, 'Dark Mode', 'gray', lambda: change_colors(['black', 'gray', 'blue', 'white']))
    button(root, 'hacker', 'green', lambda: change_colors(['black', 'green', 'blue', 'white']))
    button(root, 'Light Mode', 'white', lambda: change_colors(['white', 'gray', 'blue', 'black']))
    button(root, 'ocean', '#6B9AC4', lambda: change_colors(['#4059AD', '#6B9AC4', '#97D8C4', '#EFF2F1']))
    button(root, 'twilight', '#2E294E', lambda: change_colors(['#011638', '#2E294E', '#9055A2', '#EDF7F6']))
    button(root, 'woods', '#60992D', lambda: change_colors(['#5B3000', '#60992D', '#8CAE68', '#FCEFEF']))
    button(root, 'ice', '#ABA9C3', lambda: change_colors(['#FCF7F8', '#ABA9C3', '#CED3DC', '#222725']))
    button(root, 'terran', '#F2DD6E', lambda: change_colors(['#000000', '#F2DD6E', '#FFE641', '#7A7A7A']))
    button(root, 'murc', '#7A7E6F', lambda: change_colors(['#92694C', '#7A7E6F', '#736C68', '#D3C3C4']))
    button(root, 'Back to Main Menu', colors[2], main_menu)

def change_colors(new_colors):
    global colors
    colors = new_colors
    main_menu()


def help_and_credits_page():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Help', font=('Arial', 25), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='CONTACT\n\nemail : brodyevans82Gmail.com\ngithub: PAN-DA-BOI\n\nSoftware Version 1.8.12',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='credits', font=('Arial', 25), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='made sibgle handedly by Brody Evans\n(it took a lil while tbh)', bg=colors[0], fg=colors[3], justify='left')
    label.pack(fill='x')
    button(root, 'Back to Main Menu', colors[2], main_menu)


def donate_page():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='make change', font=('Arial', 25), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    paragraph1 = tk.Label(root, text='I dont need your money. Im fine, but I believe that everyone has the power to make a positive impact in the world.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    paragraph1.pack(fill='x')
    paragraph2 = tk.Label(root, text='There are so many people in need of help, from those struggling with poverty and homelessness to those affected by natural disasters and conflicts. By donating your time, resources, or skills to a local charity or organization, you can make a real difference in the lives of those around you.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    paragraph2.pack(fill='x')
    paragraph3 = tk.Label(root, text='I encourage you to consider volunteering your time, making a financial donation to a charity of your choice, or taking other actions to support those in need. Whether it\'s cleaning up a local park, tutoring a child, or providing food and shelter to those in need, every act of kindness counts and can make a significant difference in the world.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    paragraph3.pack(fill='x')
    button(root, 'Back to Main Menu', colors[2], main_menu)

def main_menu():
    page(root, colors[0], colors[1])
    root.title('Easy Hack')
    button(root, 'About', colors[1], about_page)
    button(root, 'Attacks', colors[1], attacks_page)
    button(root, 'Disguises', colors[1], disguises_page)
    button(root, 'help/credits', colors[1], help_and_credits_page)
    button(root, 'Donate', colors[1], donate_page)
    button(root, 'Quit', 'red', quit_page)


root = tk.Tk()
#root.attributes('-fullscreen', True)
#root.config(cursor='none')
root.geometry('320x480')
main_menu()
root.mainloop()
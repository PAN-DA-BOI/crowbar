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
    button(root, 'about this Attack', colors[1], about_attack_1_script)
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
    button(root, 'about this Attack', colors[1], about_attack_2_script)
    button(root, 'Back to Attacks', colors[2], attacks_page)
    ip = socket.gethostbyname(socket.gethostname())
    ip_label = tk.Label(root, text=f'IP: {ip}', bg=colors[0], fg=colors[3])
    ip_label.pack(fill='x')
def attack_page_3():
    page(root, colors[0], colors[1])
    titleLabel = tk.Label(root, text='Port scanning', font=('Arial', 25), bg=colors[0], fg=colors[3])
    titleLabel.pack(fill='x')
    label = tk.Label(root, text='Input = IP', bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    attack_button(root, 'START ATTACK', colors[1], './rawattackscripts/attack_3_script.sh')
    button(root, 'about this Attack', colors[1], about_attack_3_script)
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
    button(root, 'about this Attack', colors[1], about_attack_4_script)
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
    button(root, 'about this Attack', colors[1], about_attack_5_script)
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
    button(root, 'about this Attack', colors[1], about_attack_6_script)
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
    button(root, 'about this Attack', colors[1], about_attack_7_script)
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
    button(root, 'about this Attack', colors[1], about_attack_8_script)
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
    button(root, 'about this Attack', colors[1], about_attack_9_script)
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
    button(root, 'about this Attack', colors[1], about_attack_10_script)
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
    
def about_attack_1_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Network Scan',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The network scan script uses the nmap tool to perform a comprehensive scan of a target IP address. The script uses the -T5 option to increase the speed of the scan, the -A option to perform an aggressive scan, and the -v option to increase the verbosity of the output. The results of the scan are saved to an XML file, which is then converted to HTML format using the xsltproc tool. The HTML output is saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The network scan can help to identify open ports, services, and vulnerabilities on the target system, which can be used to plan further attacks or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_1)

def about_attack_2_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Service and Version Id',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The service and version identification script uses the nmap tool to identify the service and version running on a target IP address and port number. The script then uses the searchsploit tool to search for potential exploits for the identified service and version. The results of the search are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The service and version identification can help to identify potential vulnerabilities and attack vectors on the target system, which can be used to plan further attacks or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_2)

def about_attack_3_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Port Scanning',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The port scanning script uses the nmap tool to perform a port scan of a target IP address. The script uses the -p- option to scan all 65535 ports, the -T4 option to increase the speed of the scan, and the -v option to increase the verbosity of the output. The results of the scan are saved to an XML file, which is then converted to HTML format using the xsltproc tool. The HTML output is saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The port scanning can help to identify open ports and services on the target system, which can be used to plan further attacks or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_3)

def about_attack_4_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Vulnerability Scanning',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The vulnerability scanning script uses the nmap tool to perform a vulnerability scan of a target IP address. The script uses the -sV option to perform a version scan, the -sC option to perform a script scan, the -T4 option to increase the speed of the scan, and the -v option to increase the verbosity of the output. The results of the scan are saved to an XML file, which is then converted to HTML format using the xsltproc tool. The HTML output is saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The vulnerability scanning can help to identify known vulnerabilities and weaknesses on the target system, which can be used to plan further attacks or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_4)

def about_attack_5_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Web App Scanning',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The web application scanning script uses the wget tool to download a target web application and the nikto tool to perform a vulnerability scan of the application. The script uses the -r option to recursively download all linked resources, the -p option to download all resources in their original location, and the -k option to convert all links to their absolute form. The results of the scan are saved to an HTML file, which can be viewed in a web browser by the operator. The web application scanning can help to identify known vulnerabilities and weaknesses on the target application, which can be used to plan further attacks or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_5)
    
def about_attack_6_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Password Cracking',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The password cracking script uses the hashcat tool to crack a target password hash. The script uses the -m 0 option to specify the hash type (MD5), the -a 3 option to perform a brute force attack, and the /usr/share/wordlists/rockyou.txt wordlist to perform the attack. The results of the attack are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The password cracking can help to identify weak or insecure passwords on the target system, which can be used to gain unauthorized access or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_6)

def about_attack_7_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='SQL Injection',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The SQL injection testing script uses the sqlmap tool to test a target URL for SQL injection vulnerabilities. The script uses the --batch option to run the tool in batch mode and the --random-agent option to use a random user agent to avoid detection. The results of the test are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The SQL injection testing can help to identify potential vulnerabilities on the target system, which can be used to gain unauthorized access or to modify data.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_7)
    
def about_attack_8_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Directory Brute Forcing',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The directory brute forcing script uses the dirb tool to perform a brute force attack on a target URL. The script uses the /usr/share/wordlists/dirb/common.txt wordlist to perform the attack. The results of the attack are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The directory brute forcing can help to identify hidden or restricted directories on the target system, which can be used to gain unauthorized access or to modify data.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_8)

def about_attack_9_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Wireless Scan',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The wireless network scanning script uses the iwlist tool to scan for wireless networks in the area. The script filters the output to display only the ESSID and address of each network. The results of the scan are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The wireless network scanning can help to identify potential targets for further attacks or to identify areas for improvement in the target networks security.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_9)
    
def about_attack_10_script():
    page(root, colors[0], colors[1])
    label = tk.Label(root, text='Password Policy',font=('Arial', 14), bg=colors[0], fg=colors[3])
    label.pack(fill='x')
    label = tk.Label(root, text='The password policy testing script uses the ncrack tool to test the password policy of a target system. The script uses the -U option to specify the username, the -P option to specify the password list (/usr/share/wordlists/rockyou.txt), and the target URL. The results of the test are displayed in HTML format and saved to the /var/www/html/index.html file, which can be viewed in a web browser by the operator. The password policy testing can help to identify weak or insecure password policies on the target system, which can be used to gain unauthorized access or to identify areas for improvement.', bg=colors[0], fg=colors[3], wraplength=300, justify='left')
    label.pack(fill='x')
    button(root, 'back to attack', colors[1], attack_page_10)

    
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
    button(root, 'loud', '#69F970', lambda: change_colors(['#009DDC', '#69F970', '#F00699', '#54428E']))
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
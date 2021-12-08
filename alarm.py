from tkinter import * 
from tkinter import ttk
import datetime
from tkinter import messagebox
import time
import winsound

def alarm(alarm_time):
    current_time = datetime.datetime.now()
    date = current_time.strftime('%d/%m/%Y')
    # print("The set date is:", date)
    # print("Your alarm time is : " , alarm_time)

    while True:
        time.sleep(1)

        current_time = datetime.datetime.now()
        now = current_time.strftime('%H:%M:%S')
        # print(alarm_time, now)
        if now == alarm_time:
            # print("Time to wake up ")
            winsound.PlaySound("alarmtone.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Alarm","Time to wake up")
            break

def add_alarm_function():
    h = hour.get()
    m = min.get()
    s = sec.get()
    if int(h)<10:
        s_h = '0'+str(h)
    else:
        s_h = str(h)

    if int(m)<10:
        s_m = '0'+str(m)
    else:
        s_m = str(m)

    if int(s)<10:
        s_s = '0'+str(s)
    else:
        s_s = str(s)
    alarm_time = f'{s_h}:{s_m}:{s_s}'
    messagebox.showinfo("Info",f"Your alarm has been added at time {alarm_time}")

    alarm(alarm_time)

clock = Tk()
clock.title('Alarm clock')
clock.geometry("900x500")
clock.config(background='#0D1C25')

heading = Label(clock , text="ALARM CLOCK", font =("Montserrat bold",24),bg='#0D1C25',fg='white')
heading.place(relx = 0.36, rely = 0.05)

set_alarm_frame = Frame(clock,bg="#FF6F69")
set_alarm_frame.place(relx=0.08,rely=0.3,width=400,height=200)

set_alarm_heading = Label(set_alarm_frame, text= "Select Alarm", font =("times new roman",24),background='#0D1C2F',fg="white")
set_alarm_heading.place(relx=0.3,rely=0.2)

hour_value = IntVar()
hour_label = Label(set_alarm_frame, text = "Hour : " , font =("Times New Roman",12),bg='#FF6F69',fg='white')
hour_label.grid(row =0 , column =0,padx=(18,0),pady=22)
hour = ttk.Combobox(set_alarm_frame, textvariable=hour_value, state='readonly',justify='center', width=7)
hour['values'] = ['Select',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
hour.grid(row =0 , column = 1,pady ="80px")
hour.current(0)

min_value = IntVar()
min_label = Label(set_alarm_frame, text = "Min : " , font =("Times New Roman",12),bg='#FF6F69',fg='white')
min_label.grid(row =0 , column =2 ,padx=(18,0),pady=22)
min = ttk.Combobox(set_alarm_frame, textvariable=min_value, state='readonly',justify='center', width=7)
min['values'] = ['Select',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
min.grid(row =0 , column = 3,pady ="80px")
min.current(0)


sec_value = IntVar()
sec_label = Label(set_alarm_frame, text = "Sec : " , font =("Times New Roman",12),bg='#FF6F69',fg='white')
sec_label.grid(row =0 , column =4,padx=(18,0),pady=22)
sec = ttk.Combobox(set_alarm_frame, textvariable=sec_value, state='readonly',justify='center', width=7)
sec['values'] = ['Select',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
sec.grid(row =0 , column = 5,pady ="80px")
sec.current(0)


submit = Button(set_alarm_frame, text= "Add Alarm",font=('Times New Roman',12),command =add_alarm_function,bg='#0D1C25',fg='white')
submit.place(relx=0.4,rely=0.8)



current_time_frame  = Frame(clock,bg='#FF6F69')
current_time_frame.place(relx=0.58,rely = 0.3,width= 300, height=200)

current_time_heading = Label(current_time_frame, text= "Current Time", font =("Times New Roman",24),background='#0D1C25',fg='white')
current_time_heading.place(relx=0.22,rely=0.2)

time_going_on = datetime.datetime.now()
curr_time = time_going_on.strftime('%H:%M:%S')

def show_time():
    time_going_on = datetime.datetime.now()
    curr_time = time_going_on.strftime('%H:%M:%S')

    time_label.config(text=curr_time,fg='white')
    time_label.after(100, show_time)

time_label = Label(current_time_frame,text= curr_time, font =("Times New Roman",24),bg='#0D1C25')
time_label.place(relx=0.3,rely=0.5)
show_time()


clock.mainloop()
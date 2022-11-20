from transcribe import get_cmd
import datetime


# It is going to be a loop
# Inside get cmd 
# 


# while True:
# cmd = get_cmd()
# print(cmd)
# if "journal" in cmd.lower():
  # print("record journal")

title = get_cmd("What is the title?")
print(title)
filename = title.strip().replace(" ","_").replace(".","").replace(",","_")
now = datetime.datetime.now()

date_time = now.strftime("%Y %B %d, %H:%M:%S")

with open(f"./logs/{filename}.txt","w") as f:
  log_entry_long_form  = get_cmd("Enter the thought")

  f.write(date_time)
  print("Title:",title)
  f.write("\n")
  f.write(f"{title.strip().capitalize()}")
  f.write("\n")
  f.write(log_entry_long_form.strip())

  print(f"...  Done! Check ./logs/{filename}.txt")

  # print(log_entry_long_form)
from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys #Used for closing the running program
print "Press:\n\tr: Run GoPiGo Program\n\ts: Stop GoPiGo\n\tx: Exit Program"

while True:
        print "Enter the Command:",
        a=raw_input()	# Fetch the input from the terminal
        if a=='r':
               enable_encoders()
               enc_tgt(1,1,95)
               fwd()
               time.sleep(10)
               left()
               time.sleep(.5)
               enc_tgt(1,1,1026)
               fwd()
               time.sleep(50)
               right()
               time.sleep(.5)
               enc_tgt(1,1,405)
               fwd()
               time.sleep(50)
               
               
               
               
                
        elif a=='s':
                stop()	# Turn left
        elif a=='x':
                print "Exiting"		# Exit
                sys.exit()
        else:
                print "Wrong Command, Please Enter Again"
        time.sleep(.1)

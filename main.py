import random

'''
stone=-1
paper=1
scizor=0

'''

computer_choice= random.choice([-1,1,0])
You=input("Enter your choice : ")
You_dict={"s":-1,"p":1,"c":0}
reverse_dict={-1:"Stone",1:"Paper",0:"cizor"}

Your_choice=(You_dict[You])

print(f" You Choose {reverse_dict[Your_choice]}\n Computer Choose {reverse_dict[computer_choice]}")


if(computer_choice==Your_choice):
    print("It's an Draw ")

else:

    if(computer_choice==-1 and Your_choice==1):
        print("You win!")
    elif(computer_choice==-1 and Your_choice==0):
        print("You Lose!")
    elif(computer_choice==1 and Your_choice==0):
        print("You win!")
    elif(computer_choice==1 and Your_choice==-1):
        print("You Lose!")
    elif(computer_choice==0 and Your_choice==-1):
        print("You win!")
    elif(computer_choice==0 and Your_choice==1):
        print("You Lose!")
    else:
        print("Something went wrong !")    
         
    












def cave():
    print(r'''
            _________________
             ____/#################\____
         ___/################,##########\___
       _/################/##/ \##\##########\_
      /#################/\##| |##/\###########\
     /##################\ \#| |#/ /############\
    |##DWB###############\ \| |/ /#########JRB##|
    |####################{{{\ /}}}##############|
    |###################{{<.> <.>}}#############|
    |#####################{ | | }###############|
    |#####################{ | | }####_#######__#|
    |#####################/_| |_\##_( )###__(  )_
    |####################{(_)_(_)}(  ` )_( '__ ` )
    |#####################{VV_VV}##(__( `)_(  )-` )
    |#####################\^^))^/######(   )_')  )
    |######################--((-########( ' _)__)
    |########################))##########(__)###|
    |########################(##################|
    |###########################################|
    |###########################################|
    |###########################################|
    |###########################################|
\ | /########| |################################| \ | /
_\|/|#######/   \####################\|/########|__\|/___
            \   /
             \ /
              V
    ''')
def sea():
    print(r'''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         .               `         /
                          .    ,../...       .
          .                .  /       `\  /  .
     \    .        o         < '  )     =<
     /\  .                    \ \      /  \   .  __
   >=)'>                       `'\'"'"'         /o \/
     \/ .    /         o              /,        \__/\    .:/
     /   .  /--\ /         /         <')=<     .      ,,///;,   ,;/
           ::::::::;;\\\
             \            \_/            .            ''\\\\\'' ';\
    (                      \              .   __
     )                                       <'_><          (
    (          (                ,/..          `              )
     )     (    )             <')   `=<                )    (
    (       )  (               ``\```                 (      )
_____)_____(____)______________________________________)____(_______jgs_
    ''')



print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# code is strt from here
import random

print("**********WELCOME TO THE TREASURE HUNT*********")
print("Your mission to find the Treasure.")
choose1 = input("You are at the crossover,choose \"left\" or \"right\".").lower()

# choose first:
def num():
    ans = random.randint(0,1)
    return ans
t1 = num()
if t1==0:
    t1 = "left"
else:
    t1 ="right"




if choose1 == t1:

    # choose second:
    t2 = num()
    if t2 == 0:
        t2 = "wait"
    else:
        t2 = "swing"
    sea()
    choose2=input("You are at the bank of a river .choose to \"swing\" or \"wait\".").lower()
    if choose2 == t2:

        #choose third:
        t3 = random.randint(0,2)
        if t3 == 0:
            t3 = "cave black"
        elif t3 == 1:
            t3 ="cave blue"
        else:
            t3 = "cave red"

        cave()
        choose3 = input("You are at the island.choose to go in \"cave red\" or\"cave blue\"or \"Cave black\".").lower()
        if choose3 == t3:
            print("^_^ , Congratulation,You found the treasure")
        else:
            print("You die by the hand of great sage. Game over")
    else:
        print("you drown in the lake.Game over")
else:
    print("You fall into a hole.Game Over")
Board = [" " for x in range(10)]
dic_WinGroup = {1:(1,2,3),2:(4,5,6),3:(7,8,9),4:(1,4,7),5:(2,5,8),6:(3,6,9),7:(1,5,9),8:(3,5,7)}
dic_NoInGroup = {1: [1, 4, 7], 2: [1, 5], 3: [1, 6, 8], 4: [2, 4], 5: [2, 5, 7, 8], 6: [2, 6], 7: [3, 4, 8], 8: [3, 5], 9: [3, 6, 7]}


def print_Board(bo):
    print("   |   |")
    print(" " + bo[1] + " | " + bo[2]  + " | "  + bo[3])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + bo[4] + " | " + bo[5]  + " | "  + bo[6])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + bo[7] + " | " + bo[8]  + " | "  + bo[9])
    print("   |   |")


def check_Empty(bo, pos):
    if bo[pos] == " ":
        return True
    else:
        return False


def is_Full_Board(bo):
    if bo.count(" ") < 1:
        print("Tie Game!!")
        return False
    return True


def is_Winning(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def possible_Moves(bo):
     return [x for x, letter in enumerate(bo) if letter == " " and x != 0]


def func_aiMove(bo, let, po, NoInterset):
    aiMove = []
    for i in po:
        bC = bo[:]
        bC[i] = let
        Setlis = 0
        li1 = dic_NoInGroup[i] #list of sets contained possibleMove number
        for j in li1: #roop the list of sets
            li2 = dic_WinGroup[j]
            print(f"{let} = {i}i : {j}j : {li2}", end="") #remove row
            while ((bC[li2[0]] == let or bC[li2[0]] == " ") and (bC[li2[1]] == let or bC[li2[1]] == " ") and (bC[li2[2]] == let or bC[li2[2]] == " ")):
                if (bC[li2[0]].count(let) + bC[li2[1]].count(let) + bC[li2[2]].count(let)) >= 2:
                    Setlis += 1
                break
            print(Setlis) #remove row
        if Setlis >= NoInterset:
            aiMove.append(i)
            print(f"{Setlis} : {aiMove}") #remove row
    if len(aiMove) > 0:
        return aiMove
    return ""


def com_turn(bo):
    possibleMoves = possible_Moves(bo)
    move = 0

    for let in ["o", "x"]:
        for i in possibleMoves:
            boardCopy = bo[:]
            boardCopy[i] = let
            if is_Winning(boardCopy, let):
                move = i
                return move, bo
    
    for let in ["o", "x"]:
        if let == "o":
            for z in [2,1]:
                i = func_aiMove(bo, let, possibleMoves, z)
                if i != "":
                    if z == 1:
                        afteri = []
                        for j in i:
                            bC = bo[:]
                            bC[j] = "o"
                            k = func_aiMove(bC, "x", possible_Moves(bC), 2)
                            if len(k) > 0 and k != "":
                                afteri.append(j)
                        print(i) #remove row
                        i = list(set(i).symmetric_difference(set(afteri)))
                        print(i) #remove row
                    if len(i) > 0:
                        move = selectRandom(i)
                        return move, bo
        else:
            i = func_aiMove(bo, let, possibleMoves, 2)
            if i != "":
                afteri = []
                for j in i:
                    bC = bo[:]
                    bC[j] = "o"
                    k = func_aiMove(bC, "x", possible_Moves(bC), 2)
                    if len(k) > 0 and k != "":
                        afteri.append(j)
                print(i) #remove row
                i = list(set(i).symmetric_difference(set(afteri)))
                print(i) #remove row
                if len(i) > 0:
                    move = selectRandom(i)
                    return move, bo
    
    allOpen = []
    for i in possibleMoves:
        if i in range(10):
            allOpen.append(i)
    if len(allOpen) > 0:
        move = selectRandom(allOpen)
        return move, bo
    return move, bo
    

def selectRandom(li):
    from random import randrange
    ln = len(li)
    r = randrange(0,ln)
    return li[r]

def player_turn(bo):
    move = 0
    a = input("Please place \"x\" in the board, (1-9):")
    if a == "r":
        play_Again()
    try:
        move = int(a)
        if move > 0 and move < 10:
            if check_Empty(bo, move):
                return move, bo
            else:
                print_Board(bo)
                print("The slot is unavailable!")
                return player_turn(bo)
        else:
            print_Board(bo)
            print("Please key in correct number!")
            return player_turn(bo)
    except ValueError:
        print_Board(bo)
        print("Please key in correct number!:")
        return player_turn(bo)

def play_Again():
    a = input("Do you want replay? (Y/N):")
    a = a.upper()
    if a == "Y" or a == "YES" or a == "N" or a == "NO":
        if a == "Y" or a == "YES":
            bo = list(Board)
            return main(bo)
        else:
            return
    else:
        print("Please enter correctly!")
        play_Again()

def main(bo):
    turn = []
    print_Board(bo)
    while is_Full_Board(bo):
        turn = list(player_turn(bo))
        bo = turn[1]
        bo[turn[0]] = "x"
        print_Board(bo)
        print("Player has placed \"x\"..")
        if is_Winning(bo, "x"):
            print("Well Done!! You are the winner!!")
            break
        
        turn = list(com_turn(bo))
        bo = turn[1]
        bo[turn[0]] = "o"
        print_Board(bo)
        if turn[0] != 0:
            print("Com has placed \"o\"..")
        if is_Winning(bo, "o"):
            print("Player \"o\" is the winner!!")
            break
    play_Again()    
    
bo = list(Board)
main(bo)

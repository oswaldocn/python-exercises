__author__ = 'Oswaldo'

def main():
    cont = 'yes'
    while cont == 'yes':
        player1 = player_choice('Player1')
        player2 = player_choice('Player2')
        check_results(player1, player2)
        cont = check_exit()

def player_choice(player):
    choice = ''
    while choice not in ('rock', 'paper', 'scissors'):
        choice = input('%s escolha "rock", "paper" ou "scissors": ' % player).lower()
        if choice == 'rock':
            num = 1
        elif choice == 'paper':
            num = 2
        elif choice == 'scissors':
            num = 3
        if choice not in ('rock', 'paper', 'scissors'):
            print('Digite um valor válido')
    return num

def check_results(player1, player2):
    difference = player1 - player2
    if difference == 0:
        print('EMPATE!')
    elif difference%3 == 1:
        print('O VENCEDOR É O PLAYER 1!')
    elif difference%3 == 2:
        print('O VENCEDOR É O PLAYER 2!')

def check_exit():
    check = ''
    while check not in ('yes', 'no'):
        check = input('Deseja jogar novamente? (yes ou no): ').lower()
        if check not in ('yes', 'no'):
            print('Digite um valor válido (yes ou no)')
    return(check)

main()
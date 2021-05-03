import menu
import banner
import florio_island
import belusylva_island
import maricopia_island
import voluca_island
import durice_island
import aurus_island


def go_back():
    menu.back_menu()

    answer = input('\n > ').lower()

    if answer == 'y':
        start()

    elif answer == 'n':
        exit()

    else:
        menu.invalid()

        go_back()


def start():
    banner.print_banner()

    menu.main_menu()

    answer = input('\n > ').lower()

    if answer == 'q':
        exit()

    elif answer == '1':
        florio_island.florio()

        go_back()

    elif answer == "2":
        belusylva_island.belusylva()

        go_back()

    elif answer == "3":
        maricopia_island.maricopia()

        go_back()

    elif answer == "4":
        voluca_island.voluca()

        go_back()

    elif answer == "5":
        durice_island.durice()

        go_back()

    elif answer == "6":
        aurus_island.aurus()

        go_back()

    else:
        menu.invalid()

        go_back()


start()

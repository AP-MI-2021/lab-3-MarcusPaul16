from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def is_square(n: int):
    '''
    Determina daca un numar este patrat perfect
    :param n: nr intreg
    :return: bool, daca e patrat perfect, returneaza true, altfel, returneaza false
    '''
    if sqrt(n) == int(sqrt(n)):
        return True
    else:
        return False


def bits_number(n: int):
    """
    returneaza numarul de biti de 1, in reprezentarea binara a lui n
    :param n: nr intreg
    :return: returneaza nr de biti de 1
    """
    count = 0
    while n != 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    return count


def get_longest_all_primes(lst: list[int]):
    inceput = 0
    final_inceput = 0
    maxim = 0
    counter = 0
    for i in range(len(lst)):
        if prime(lst[i]) is True:
            counter += 1
        else:
            if counter > maxim:
                maxim = counter
                final_inceput = inceput
            inceput = i + 1
            counter = 0
    if counter > maxim:
        maxim = counter
        final_inceput = inceput
    return lst[final_inceput: final_inceput + maxim]


def get_longest_all_perfect_squares(lst: list[int]):
    """
    Determina cea mai launga secventa de numere situate consecutiv in lista, care sunt patrate perfecte
    :param lst: lista cu numere elemente numere intregi
    :return: o lista, care contine cea mai lunga secventa de numere, aflate pe pozitii consecutive in lista initiala,  care sunt patrate perfecte
    """
    inceput = 0
    final = 0
    count = 0
    maxim = 0
    inceput_maxim = 0
    final_maxim = 0
    ok = 0
    for i in range(len(lst)):
        if is_square(lst[i]) is True:
            count += 1
            final = i
            ok = 1
        else:
            if count > maxim:
                maxim = count
                inceput_maxim = inceput
                final_maxim = final
            count = 0
            inceput = i + 1
    if count > maxim:
        inceput_maxim = inceput
        final_maxim = final
    if ok > 0:
        lst_final = lst[inceput_maxim:final_maxim + 1]
        return lst_final


def get_longest_same_bit_counts(lst: list[int]):
    """
    Cauta cea mai launga secventa de numere, aflate pe indici consecutivi in lista initiala, care au acelasi  numar de bitsi de 1
    :param lst: lista cu elementele, de tip intre
    :return: o lista, care contine cea mai lunga secventa de nr cu acelasi numar de bitsi de 1
    """
    if lst == []:
        return None
    first_number = bits_number(lst[0])
    numar_elemente = 1
    inceput = 0
    inceput_maxim = 0
    maxim_nr_elemente = -1
    for i in range(1, len(lst)):
        second_number = bits_number(lst[i])
        if first_number == second_number:
            numar_elemente += 1
        else:
            if numar_elemente > maxim_nr_elemente:
                maxim_nr_elemente = numar_elemente
                inceput_maxim = inceput
            inceput = i
            numar_elemente = 1
        first_number = second_number
    if numar_elemente > maxim_nr_elemente:
        maxim_nr_elemente = numar_elemente
        inceput_maxim = inceput
    return lst[inceput_maxim:inceput_maxim + maxim_nr_elemente]




def test_prime():
    assert prime(3) is True
    assert prime(4) is False
    assert prime(1) is False
    assert prime(27) is False


def test_bits_number():
    assert bits_number(2) == 1
    assert bits_number(3) == 2
    assert bits_number(0) == 0
    assert bits_number(23) == 4


def test_is_square():
    assert is_square(9) is True
    assert is_square(5) is False
    assert is_square(81) is True


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([0, 1, 2, 2, 3, 3, 3, 3]) == [3, 3, 3, 3]
    assert get_longest_same_bit_counts([0, 0, 0]) == [0, 0, 0]
    assert get_longest_same_bit_counts([2, 3, 3, 3, 5]) == [3, 3, 3, 5]
    assert get_longest_same_bit_counts([2, 3, 4, 5, 7]) == [2]


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([20, 35, 36, 81, 4]) == [36, 81, 4]
    assert get_longest_all_perfect_squares([1, 1, 0]) == [1, 1, 0]
    assert get_longest_all_perfect_squares([5]) is None
    assert get_longest_all_perfect_squares([4]) == [4]


def test_get_longest_all_primes():
    assert get_longest_all_primes([2, 2, 2, 4]) == [2, 2, 2]
    assert get_longest_all_primes([1, 1, 1]) == []
    assert get_longest_all_primes([2, 3, 4, 6, 8, 9, 11, 11, 11, 11]) == [11, 11, 11, 11]


def test_all():
    test_is_square()
    test_bits_number()
    test_get_longest_same_bit_counts()
    test_get_longest_all_perfect_squares()
    test_prime()
    test_get_longest_all_primes()



option = """
        Daca doresti sa introduci date in lista ta, scrie '1'.
        Daca doresti sa golesti lista ta, scrie '2'.
        Daca doresti sa afisezi lista, scrie '3'.
        Daca doresti sa afli cea mai lunga secventa de numere patrate perfecte, scrie '4'.
        Daca doresti sa afli cea mai lunga secventa de numere cu acelasi numar de bitsi de 1, scrie '5'.
        Daca doresti sa afli cea mai lunga secventa de numere prime, scrie '6'.
        Daca doresti sa opresti programul, scrie '7' sau apasa ctrl + c .
        Raspunsul tau:
        """

def main():
    lista = []
    while True:
        test_all()
        alegere = int(input(option))
        if alegere == 1:
            lista_string = input("Scrie aici lista ta de numere, despartite de un spatiu: ")
            lista = [int(numar) for numar in lista_string.split()]
        elif alegere == 2:
            lista.clear()
        elif alegere == 3:
            print(lista)
        elif alegere == 4:
            print(f"Cea mai lunga secventa de numere care sunt patrate perfecte, este {get_longest_all_perfect_squares(lista)}")
        elif alegere == 5:
            print(f"Cea mai lunga secventa de numere cu acelasi nr. de bitsi de 1 este: {get_longest_same_bit_counts(lista)}")
        elif alegere == 6:
            print(f"Cea mai lunga secventa de numere pare este: {get_longest_all_primes(lista)}")
        elif alegere == 7:
            print("Programul s-a oprit!")
            break
        else:
            print("Comanda inexistenta")


if __name__ == main():
    main()

"""
Ce code permet de lire le contenu d'un fichier
"""
#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l=[]
    with open(filename,'r',encoding='utf8') as f:
        for i in f:
            m=i
            liste = [int(x) for x in m.split(";")]
            l.append(liste)
    return l

def get_list_k(data, k):
    """
    Permet de renvoyer la liste d'indice k dans data
    """
    if len(data)>k:
        i=data[k]
        return i
    return None

def get_first(l):
    """
    Permet de renvoyer la premiere valeur de la liste l
    """
    if len(l)>=1:
        return l[0]
    return None

def get_last(l):
    """
    Permet de renvoyer la derniere valeur de la liste l
    """
    if len(l)>=1:
        return l[-1]
    return None

def get_max(l):
    """
    Permet de renvoyer la valeur maximun de la liste l
    """
    if len(l)>=1:
        return max(l)
    return None

def get_min(l):
    """
    Permet de renvoyer la valeur minimum de la liste l
    """
    if len(l)>=1:
        return min(l)
    return None

def get_sum(l):
    """
    Permet de renvoyer la somme de la liste l
    """
    if len(l)>=1:
        return sum(l)
    return None


#### Fonction principale


def main():
    """
    main
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

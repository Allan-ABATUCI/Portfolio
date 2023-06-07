
def dico_reseau(tamis):
    """
     A partir d'un tableau tamis modélisant les interactions entre personnes d'un réseau,
     retourne un dictionnaire dont les clés sont les prénoms des membres du réseau et les valeurs le tableau de leurs amis.
     entrées
    tamis: tableau des interactions ou tamis[2*i] est amis avec tamis[2*i+1] ex:['amis1','amis2']
    sortie
    dico: dictionnaire modélisant les interactions ex:{'user':['amis1','amis2'],'amis2':['user']}
    """
    dico={}
    for i in range(len(tamis) // 2):
        if tamis[2*i] not in dico.keys():
            dico[tamis[2*i]]=tamis[2*i+1]
        if tamis[2*i+1] not in dico.keys():
            dico[tamis[2*i+1]]=tamis[2*i]
        if tamis[2 * i+1] not in dico[tamis[2 * i]]:
            dico[tamis[2 * i]] += " " + tamis[2 * i + 1]
        if tamis[2 * i] not in dico[tamis[2 * i + 1]]:
            dico[tamis[2 * i + 1]] += " " + tamis[2 * i]
    #transforme objets en list
    for i in range(len(tamis)):
        if type(dico[tamis[i]])!=list:
            t=dico[tamis[i]]
            dico[tamis[i]]=t.split()
    return dico

def network(tab):
    """
    retourne un dictionnaire de reseau d'amis.
    paramêtres:
    tab = tableau modélisant les interactions d'un réseau tel que tab[2*i] est amis avec tab[2*i+1]
    variables:
    dico = dictionnaire du reseau d'amis; dict
    exemple : network(["Alice","Nassim","Michael","Zack"]) = {"Alice":["Nassim"],"Nassim":["Alice"],"Michael":["Zack"],"Zack":["Michael"]}
    """
    i = 0
    dico = {}
    if tab == []:
        return dico
    while 2 * i < len(tab):
        if tab[2 * i] not in dico:
            dico[tab[2 * i]] = []
        dico[tab[2 * i]] += [tab[2 * i + 1]]

        if tab[2 * i + 1] not in dico:
            dico[tab[2 * i + 1]] = []
            dico[tab[2 * i + 1]] += [tab[2 * i]]
        i += 1
    return dico

def get_people(reseau):
    """
     retourne la liste des personnes du réseau dans un tableau.
     paramêtres:
     reseau= dictionnaire de liste d'amis; dict
    """
    if reseau == {}:
        return reseau
    i = 0
    tab = []
    key = list(reseau)
    while i < len(reseau):

        if key[i] not in tab:
            tab.append(key[i])
        i += 1
    return tab




def are_friends(reseau, pers1, pers2):
    """
     retourne True si les deux personnes sont amies, et False sinon.
     paramêtres:
     reseau= dictionnaire de liste d'amis; dict
     pers1,pers2 = personne visée par la recherche; str
    """
    if pers1=="" or reseau=={} or pers2=="":
        return False
    if pers1 in reseau[pers2] and pers2 in reseau[pers1]:
            return True
    return False


def all_his_friends(reseau, pers, groupe):
    """
     retourne True si la personne est amie avec toutes les personnes du groupe, et False sinon.
     paramêtres:
     reseau= dictionnaire de liste d'amis; dict
     pers = personne visée par la recherche; str
     groupe = liste de personne; list
     variables:
     none

    """
    if groupe==[] or reseau=={} or pers=="":
        return False
    i = 0

    while i < len(groupe):
        if groupe[i] not in reseau[pers]:
            return False

        i += 1

    return True




def is_a_community(reseau, groupe):
    """
    retourne True si le groupe est une communauté, et False sinon.
    paramêtres:
    reseau= dictionnaire de liste d'amis; dict
    groupe = liste de personne; list
    variables:
    key = clés du dictionnaire; list
    """
    if groupe==[] or reseau=={}:
        return []
    i = 0
    a = 0
    key = list(reseau)

    while i < len(reseau):

        if key[i] in groupe:
            while a < len(groupe):
                if (groupe[a] != key[i]) and groupe[a] not in reseau[key[i]]:
                    return False

                a += 1

        i += 1
    return True

def find_community(reseau,groupe):
    """
     prenant en paramètre un réseau et un groupe de personnes et retournant une communauté.
     L'ordre du groupe est important car les comparaisons sont basés sur la première personne
     paramêtres:
     reseau = dictionnaire de liste d'amis; dict
     groupe = liste de personne; list
     variables:
     commu=tableau de la communauté créée; list
     reseau= dictionnaire de liste d'amis; dict
     groupe= liste ou l'on veut trouvé une communauté; list
     amis= compteur d'amis dans la nouvelle communauté; int
     exemple:
     find_community({"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]} , ["Alice", "Bob", "Charlie", "Dominique"])
     =["Alice", "Bob", "Dominique"]
    """
    if reseau=={} or groupe==[]:
        return []
    commu=[]
    commu.append(groupe[0])
    for personne in groupe:
        amis=0
        for i in commu:
            if personne in reseau[i] and personne not in commu:
                amis+=1
        if amis==len(commu):
            commu.append(personne)

    return commu





def order_by_decreasing_popularity(reseau, groupe):
    """
    trie l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourner la communauté trouvée.
    paramêtres:
    reseau = dictionnaire de liste d'amis; dict
    groupe = liste de personne; list
    """
    if groupe==[] or reseau=={}:
        return []
    k=len(groupe)
    stck = 0
    for personne in range(k):
        for i in range(k-personne-1,0,-1):
            if len(reseau[groupe[i]]) > len(reseau[groupe[i - 1]]):
                stck = groupe[i]
                groupe[i] = groupe[i - 1]
                groupe[i - 1] = stck
    return groupe




def find_community_by_decreasing_popularity(reseau):
    """
    La fonction doit trier l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourner la communauté trouvée
    variables:
     groupe = tableau de personne unique dans le réseau;
     reseau = dictionnaire de liste d'amis; dict
     stck = variable intermédiaire ; str
     commu = tableau de la communauté créée; list

    exemple : find_community_by_decreasing_popularity({"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]})
    =['Bob', 'Alice', 'Dominique']
    """
    if reseau=={}:
        return []
    groupe=list(reseau)
    k = len(groupe)
    stck = []
    for personne in range(k):
        for i in range(k-personne-1,0,-1):
            if len(reseau[groupe[i]]) > len(reseau[groupe[i - 1]]):
                stck = groupe[i]
                groupe[i] = groupe[i - 1]
                groupe[i - 1] = stck
    commu = []
    commu.append(groupe[0])
    for personne in groupe:
        amis = 0
        for i in commu:
            if personne in reseau[i] and personne not in commu:
                amis += 1
        if amis == len(commu):
            commu.append(personne)

    return commu


def find_community_from_person(person,reseau):
    """
    la fonction trie les amis de person par ordre de popularité décroissante et pour chacune de ces personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté.
    paramêtres:
    groupe = tableau de personne unique dans le réseau; list
    reseau = dictionnaire de liste d'amis; dict
    variables:
    stck = variable intermédiaire ; str
    commu = tableau de communauté; list

    """
    if person=="" or reseau=={}:
        return []
    groupe=reseau[person]
    k = len(groupe)
    stck = ""
    for personne in range(k):
        for i in range(k-personne-1,0,-1):
            if len(reseau[groupe[i]]) > len(reseau[groupe[i - 1]]):
                stck = groupe[i]
                groupe[i] = groupe[i - 1]
                groupe[i - 1] = stck
    commu = []
    commu.append(person)
    for personne in groupe:
        amis = 0
        for i in commu:
            if personne in reseau[i] and personne not in commu:
                amis += 1
        if amis == len(commu):
            commu.append(personne)
    return commu


def find_max_community(reseau):
    """
     retourne la plus grande communauté trouvée dans un réseau d'amis
     paramêmtres:
     reseau = dictionnaire de liste d'amis; dict
     variables:
     stck = variable intermédiaire ; str
    commu = tableau de communauté; list
    """
    if reseau=={}:
        return []
    groupe=list(reseau)
    k = len(groupe)
    stck = ""
    for personne in range(k):
        for i in range(k - personne - 1, 0, -1):
            if len(reseau[groupe[i]]) > len(reseau[groupe[i - 1]]):
                stck = groupe[i]
                groupe[i] = groupe[i - 1]
                groupe[i - 1] = stck
    commu = []
    commu.append(groupe[0])
    for personne in groupe:
        amis = 0
        for i in commu:
            if personne in reseau[i] and personne not in commu:
                amis += 1
        if amis == len(commu):
            commu.append(personne)
    return commu

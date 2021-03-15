import re

# valeur minimale pour la taille du nom de l'adresse email (nom@domaine.fr)
nameMinSize = 5

# fonction permettant de supprimer les mots de passes iphone
def delete_iphone_password(listEmail):
    for email in listEmail:
        pswd = email.split(':')[1] # on récupère le mot de passe
        if(pswd.count("-")==2):
            listEmail.remove(email)
    return(listEmail)

# fonction permettant de vérifier le regex email
def check_regex(listEmail):
    regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    for email in listEmail:
        if(not(re.search(regex,email.split(':')[0]))):
            listEmail.remove(email)
    return(listEmail)

# fonction permettant de supprimer les combos dont la taille du nom est < à une certaine valeur
def deleteShortName(listEmail):
    for email in listEmail:
        name = email.split(':')[0].split('@')[0]
        if(len(name)<=nameMinSize):
            listEmail.remove(email)
    return(listEmail)

# fonction permettant de supprimer les domaines inconnus
# la liste des domaines connus: know_domain
def delete_unknow_domain(listEmail):
    for email in listEmail: # pour chacune des emails dans la liste
        domain = email.split(':')[0].split('@')[1].split('.')[0] # on récupère le domaine
        if domain not in know_domain: # si le domaine n'est pas connu
            listEmail.remove(email) # on supprime l'email de la liste
    return(listEmail) # on retourne la liste avec le éléments supprimés

# fonction permettant de trier le fichier en fonction des domaines connus
# la liste des domaines connus: know_domain
def sort_by_domain(listEmail,know_domain):
    sort_list = [] # on initialise une liste
    for domain_name in know_domain: # pour chacun des domaines connus
        for email in listEmail: # puis pour chacune des emails dans la liste
            domain = email.split(':')[0].split('@')[1].split('.')[0] # on récupère le domaine
            if domain_name == domain: # si le domaine est connu est correspond à celui en cours
                sort_list.append(email.replace("\n","")) # on l'ajoute à la liste
    return(sort_list)

# fonction permettant de supprimer les doublons
def delete_doublon(listEmail):
    new_list = [] # on initialise une liste
    for email in listEmail: # pour chacune des emails dans la liste
        if email not in new_list: # si l'email n'est pas dans la nouvelle liste
            new_list.append(email) # alors on l'ajoute
    return(new_list) # on retourne la nouvelle liste ne contenant plus que les emails uniques

# fonction permettant d'écrire dans un fichier tous les éléments de la liste listEmail
def write_new_list(listEmail):
    list_to_add = "" # création d'une chaine de caractère
    for email in listEmail: # pour chacune des emails dans la liste
        list_to_add += email # on ajoute à la chaine de caractère l'adresse email
    fileListEmail = open("newList.txt", "w") # on ouvre la nouvelle liste
    fileListEmail.write(list_to_add) # on écrit dans la nouvelle liste

# fonction permettant de créer des fichiers contenant les emails correspondant à leur domaine
def make_different_files_for_domain(listEmail, know_domain):
    for email in listEmail: # pour chacune des emails dans la liste
        domain = email.split(':')[0].split('@')[1].split('.')[0] # on récupère le domaine
        if domain in know_domain: # si le domaine est connu
            domainFile = open("domain/"+domain+".txt", "a") # on ouvre le fichier en mode ajout
            domainFile.write(email + "\n") # on écrit dedans

# fonction permettant de mettre en minuscule l'adresse email
def lowEmails(listEmail):
    i=0
    for combo in listEmail:
        email = combo.split(":")[0].lower()
        pswd = combo.split(":")[1]
        listEmail[i] = email + ":" + pswd
        i+=1
    return(listEmail)

# fonction permettant de lister tous les domaines présents
def listDomains(listEmail):
    domains = []
    for combo in listEmail:
        domain = combo.split('@')[1].split('.')[0]
        if domain not in domains:
            domains.append(domain)
    [print(domain) for domain in domains]

fileListEmail = open("lastList.txt", "r") # on ouvre le fichier contenant les emails
listEmail = fileListEmail.readlines() # on lit chacune des lignes

# liste des domaines connus
know_domain = ['gmail','free','outlook','hotmail','icloud','neuf','orange','yahoo','laposte','sfr','live','gmx','msn']

print('Charging ' + str(len(listEmail)) + ' Emails...')

# formater les emails
listEmail = lowEmails(listEmail)
# afficher les différents domaines
# listDomains(listEmail)

# fonctions du programme, à mettre en commentaire si vous ne voulez pas l'executer
listEmail = delete_unknow_domain(listEmail) # supprimer les domaines inconnus
listEmail = sort_by_domain(listEmail, know_domain) # trier en fonction des domaines
listEmail = delete_doublon(listEmail) # supprimer les doublons
listEmail = delete_iphone_password(delete_iphone_password(listEmail)) # supprimer les mots de passe iphone
listEmail = deleteShortName(listEmail)
listEmail = check_regex(listEmail)
write_new_list(listEmail) # ecrire les nouvelles entrées
make_different_files_for_domain(listEmail,know_domain) # créer des fichiers contenant les emails en fonction des différents domaines connus

print('The New List Counts ' + str(len(listEmail)) + ' Email!')

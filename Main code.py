from lxml import etree
import module as stat 
import requests
import time
parkings=["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH","FR_MTP_GAMB",
"FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC",
"FR_CAS_SABL","FR_MTP_MOSS","FR_STJ_SJLC","FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
"FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE","FR_MTP_POLY"]

def recup(v):
    total_occup=0#pour le pourcentage
    total_libre=0#pour le pourcentage
    for i in (v):
        #Pour recupérer les liens de chaque parkings sur le site de montpellier
            a="https://data.montpellier3m.fr/sites/default/files/ressources/"+i+".xml"
            print(a)
            reponse=requests.get(a)
            #Ouvrir dans des fichiers le noms de chaque parking
            f1=open(i,"w", encoding='utf8')
            f1.write(response.text)
            f1.close()

            tree = etree.parse(i)
            for user in tree.xpath("Name"):
                print('Nom du parking :', user.text)
            #Récuperer les noms de chaque parking
            for user in tree.xpath("Total"):
                print('Nombre total de places :',user.text)
                q.user.text
                total_occupe+=int(q)
            #Récuperer les nombres total de places de chaque parking
            for user in tree.xpath("Free"):
                print('Nombres de places libres :',user.text)
                z=user.text
                total_libre+=int(z)
            #Récuperer les nombres de places libres de chaque parking
    
    o=stat.pourcentage(int(z),int(q))
    o=stat.pourcentage(int(total libre).int(total occupe))

    print("Le pourcentage de place libre est :", round(o,2),%)
        #Pourcentage de place libre pour chaque parking (arrondi au centième)
    print("Pour tous les Parkings de Montpellier :")

    m=stat.pourcentage(total_libre , total_occupe)
    print ("Le pourcentage total de place libre de tout les parkings réunis est de :", round(m,2),"%")
    #Pourcentage de place libre pour tout les parkings

recup(parkings)

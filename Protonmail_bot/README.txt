COMMING NEXT 

-Une ecriture du json jolie et non pas en une seule ligne 
-trouver un moyen de créer une boucle
-Créer un moyen d'éditer la page excel sans la reset pour pouvoir rajoutter des colonnes.

-detecter le message qui dit que je suis IP Ban pour changer d'IP



ARCHITECTURE DU PACKAGE 

                                    Webdriver.Chrome      (vient du package selenium)
                                    |
                                    |
                                    v
                                    DriverAugmente (vient de actions_de_base.py)
                                    |    [Contiens les options (chrome_options) et les fonctions de base 
                                    |    (ouvrir un onglet et aller dessus, ecrire comme un humain)]
                                    v
FonctionsYopmail (yopmail.py) --- > Proton         (vient de proton.py)
    [Contiens les fonctions liées      [Contiens les actions de la création du compte]
    à la recup du code de 
    verifications dans yopmail]                                 


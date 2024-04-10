import flet as ft


def main(page: ft.Page):

    page.title = 'Application de Salutations!'

    # Récupérer le nom et le prénom
    nom = ft.TextField(label="Veuillez saisir le nom", autofocus=True)
    prenom = ft.TextField(label="Veuillez saisir le prénom")

    # Colonne pour afficher le message
    ma_colonne = ft.Column()
    erreur = ft.Column()

    page.theme_mode = 'light'

    # Fonction de traitement
    def salutation(e):
        if nom.value and prenom.value:
            message = f'Bonjour {nom.value} {prenom.value}'
            ma_colonne.controls.append(ft.Text(message))
            nom.value = ""
            prenom.value = ""
        else:
            erreur.controls.append(ft.Alert("Le Nom & le prénom doivent être renseignés"))
        page.update()

    # Fonction de traitement
    def changement_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark' 
        page.update()

    # Mon Bouton de validation
    mon_bouton = ft.ElevatedButton("Cliquez Pour Saluer", on_click=salutation)
    mon_bouton_change_theme = ft.ElevatedButton("Cliquez Pour changer le thème", on_click=lambda e: changement_theme(e))

    page.add(
        nom,
        prenom,
        mon_bouton,
        ma_colonne,
        erreur,  # Ajout de la colonne d'erreur en bas
        mon_bouton_change_theme,
    )

ft.app(main)
# Exemple de Compteur Flet

Cet exemple présente un simple compteur réalisé avec la bibliothèque `flet`. Il s'agit d'un compteur où vous pouvez incrémenter et décrémenter un nombre affiché en utilisant des boutons.

## Structure du Code

Le code est écrit en Python et utilise la bibliothèque `flet`. Voici un aperçu de sa structure :

- `import flet as ft`: Importe la bibliothèque `flet` sous l'alias `ft`.
- La fonction `main(page: ft.Page)`: Cette fonction principale configure et construit l'interface utilisateur.
    - `page.title = "Flet counter example"`: Définit le titre de la page.
    - `page.vertical_alignment = ft.MainAxisAlignment.CENTER`: Aligne les éléments verticalement au centre.

    - `txt_number`: Crée un champ de texte pour afficher et entrer les valeurs du compteur.
    - `minus_click(e)`: Une fonction de rappel pour le clic sur le bouton "moins". Elle décrémente la valeur du champ de texte.
    - `plus_click(e)`: Une fonction de rappel pour le clic sur le bouton "plus". Elle incrémente la valeur du champ de texte.

    - Ajoute une rangée (`ft.Row`) contenant un bouton de soustraction, le champ de texte et un bouton d'addition. Les boutons sont associés à des fonctions de rappel pour effectuer les opérations correspondantes.

- `ft.app(main, view=ft.AppView.WEB_BROWSER)`: Lance l'application en utilisant la fonction `main` comme point d'entrée, avec une vue dans un navigateur Web.

## Utilisation

L'exemple crée une interface simple où vous pouvez cliquer sur les boutons "moins" et "plus" pour décrémenter et incrémenter respectivement la valeur affichée dans le champ de texte.

Pour exécuter le code, assurez-vous d'avoir la bibliothèque `flet` installée et exécutez le script Python.

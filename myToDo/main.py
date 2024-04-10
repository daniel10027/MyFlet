import flet as ft

# Couleurs pour le mode sombre et clair
_dark = ft.colors.with_opacity(0.5, "white")
_light = ft.colors.with_opacity(1, "black")

# Feuilles de style pour les différents éléments
toggle_style_sheet = {"icon": ft.icons.DARK_MODE_ROUNDED, "icon_size": 18}
add_style_sheet = {"icon": ft.icons.ADD_ROUNDED, "icon_size": 18}

item_style_sheet = {
    "height": 50,
    "expand": True,
    "border_color": _dark,
    "cursor_height": 24,
    "hint_text": "Veuillez saisir la tache ici ...",
    "content_padding": 15
}

to_do_item_style_sheet = {"height": 50, "border_radius": 4}

# Classe Hero représentant la partie principale de l'interface utilisateur
class Hero(ft.SafeArea):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(minimum=10, maintain_bottom_view_padding=True)
        self.page = page 
        self.title = ft.Text("MyTodo", size=20, weight="w800")  # Titre de l'application
        self.toogle = ft.IconButton(**toggle_style_sheet, on_click=lambda e: self.switch(e))  # Bouton pour basculer entre le mode sombre et clair
        self.item = ft.TextField(**item_style_sheet)  # Champ de texte pour ajouter une tâche
        self.add = ft.IconButton(**add_style_sheet, on_click=lambda e: self.add_item(e))  # Bouton pour ajouter une tâche
        self.todo_area = ft.Column(expand=True, spacing=18)  # Zone pour afficher la liste des tâches
        self.counter = ft.Text("0 Taches", italic=True)  # Texte pour afficher le nombre de tâches

        # Mise en page principale de l'application
        self.main = ft.Column(
            controls=[
                ft.Row(alignment="spaceBetween", controls=[self.title, self.toogle]),  # En-tête avec le titre et le bouton de thème
                ft.Divider(height=20),
                ft.Divider(height=10, color="transparent"),
                ft.Text("1. Ajoutez vos taches ici.", size=18),  # Instruction pour ajouter des tâches
                ft.Row(controls=[self.item, self.add], alignment="spaceBetween"),  # Champ de texte et bouton d'ajout de tâche
                ft.Divider(height=10, color="transparent"),
                ft.Row(
                    controls=[ft.Text("2. Listes de taches a effectuer.", size=18), self.counter],  # En-tête de la liste des tâches
                    alignment="spaceBetween",
                ),
                self.todo_area,  # Affichage de la liste des tâches
            ]
        )

        self.content = self.main

    # Méthode pour mettre à jour le nombre de tâches affichées
    def item_size(self):
        num_items = len(self.todo_area.controls[:])
        self.counter.value = f"{num_items} Tache{'s' if num_items != 1 else ''}"
        self.counter.update()

    # Méthode pour ajouter une tâche à la liste
    def add_item(self, e) -> None:
        if self.item.value != "":
            theme = "dark" if self.page.theme_mode == ft.ThemeMode.DARK else "light"
            self.todo_area.controls.append(TodoItem(self, self.item.value, theme))
            self.todo_area.update()
            self.item_size()
            self.item.value = ""
            self.item.update()

    # Méthode pour basculer entre le mode sombre et clair
    def switch(self, e) :
        border_color = _light if self.page.theme_mode == ft.ThemeMode.DARK else _dark
        self.page.theme_mode = ft.ThemeMode.LIGHT if self.page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.toogle.icon = ft.icons.LIGHT_MODE_ROUNDED if self.page.theme_mode == ft.ThemeMode.DARK else ft.icons.DARK_MODE_ROUNDED
        self.item.border_color = border_color
        for item in self.todo_area.controls[:]:
            item.border = ft.border.all(1, border_color)
        self.page.update()

# Classe représentant un élément de la liste de tâches
class TodoItem(ft.Container):
    def __init__(self, hero: object, description: str, theme: str) -> None:
        super().__init__(**to_do_item_style_sheet)
        border_color = _dark if theme == "dark" else _light
        self.hero = hero 
        self.description = description 
        self.tick = ft.Checkbox(on_change=lambda e: self.strike(e))  # Case à cocher pour marquer la tâche comme terminée
        self.text = ft.Text(spans=[ft.TextSpan(text=self.description)], size=15)  # Texte de la description de la tâche
        self.delete = ft.IconButton(icon=ft.icons.DELETE_ROUNDED, icon_color="red700", on_click=lambda e: self.delete_text(e))  # Bouton pour supprimer la tâche
        self.content = ft.Row(
            alignment="spaceBetween", 
            controls=[
                ft.Row(controls=[self.tick, self.text]),
                self.delete
            ]
        ) 

    # Méthode pour barrer le texte de la tâche si elle est marquée comme terminée
    def strike(self, e) -> None:
        self.text.spans[0].style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH, decoration_thickness=2) if e.control.value else ft.TextStyle()
        self.text.update()

    # Méthode pour supprimer la tâche de la liste
    def delete_text(self, e) -> None:
        self.hero.todo_area.controls.remove(self)
        self.hero.todo_area.update()
        self.hero.item_size()

# Fonction principale pour initialiser l'application
def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme()
    hero = Hero(page)
    page.add(hero)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

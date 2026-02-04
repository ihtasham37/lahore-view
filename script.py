def on_page_load():
    menu_button = "menu-btn element"
    nav_links = "nav-links element"
    def toggle_menu():
        if nav_links == "active":
            nav_links = "inactive"
        else:
            nav_links = "active"
    current_page = "index.html"
    nav_items = ["index.html", "about.html", "contact.html"]
    for link in nav_items:
        if link == current_page:
            print(f"{link} is ACTIVE")
        else:
            print(f"{link} is normal")
on_page_load()

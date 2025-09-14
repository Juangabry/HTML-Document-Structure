import reflex as rx


class HeaderState(rx.State):
    show_menu: bool = False

    def toggle_menu(self):
        self.show_menu = not self.show_menu
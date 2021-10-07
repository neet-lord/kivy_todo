from kivy.app import App
from kivy.uix.button import Button


class TodoApp(App):
    def on_add_todo_item(self, button, touch):
        if not button.collide_point(*touch.pos):
            return

        # Fetch a reference for the todo item panel
        todo_item_panel = self.root.ids.todo_item_panel
        
        # Fetch a reference for the new todo item text input
        todo_item_input = self.root.ids.todo_item_input
        
        # Fetch the text from the input
        todo_item_text = todo_item_input.text

        btn_todo_item = Button(
            text=todo_item_text,
            size_hint_y= None,
            height= 40
        )

        btn_todo_item.on_touch_down = lambda touch: self.on_delete_todo_item(todo_item_panel, btn_todo_item, touch)

        todo_item_panel.add_widget(
            btn_todo_item
        )

    def on_delete_todo_item(self, panel, button, touch):
        if not button.collide_point(*touch.pos):
            return

        panel.remove_widget(button)


if __name__ == '__main__':
    TodoApp().run()
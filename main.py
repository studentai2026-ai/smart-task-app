from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TaskApp(App):
    def build(self):
        self.title = "تطبيق المهام الذكي"
        
        # التصميم الرئيسي
        root_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # العنوان
        title_label = Label(
            text="📌 إدارة المهام اليومية", 
            size_hint=(1, 0.1),
            font_size=20,
            bold=True
        )
        root_layout.add_widget(title_label)
        
        # حقل الإدخال
        self.input_field = TextInput(
            hint_text="اكتب مهمة جديدة هنا...",
            size_hint=(1, 0.12),
            multiline=False
        )
        root_layout.add_widget(self.input_field)
        
        # زر الإضافة
        add_button = Button(
            text="إضافة المهمة",
            size_hint=(1, 0.12),
            background_color=(0.1, 0.5, 0.8, 1)
        )
        add_button.bind(on_press=self.add_new_task)
        root_layout.add_widget(add_button)
        
        # صندوق عرض المهام داخل ScrollView ليقبل التمرير
        self.tasks_box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.tasks_box.bind(minimum_height=self.tasks_box.setter('height'))
        
        scroll_view = ScrollView(size_hint=(1, 0.66))
        scroll_view.add_widget(self.tasks_box)
        root_layout.add_widget(scroll_view)
        
        return root_layout

    def add_new_task(self, instance):
        task_text = self.input_field.text.strip()
        if task_text:
            # تصميم صف لكل مهمة يحتوي على (النص + زر حذف)
            task_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=45, spacing=10)
            
            task_label = Label(
                text=f"• {task_text}",
                size_hint_x=0.75,
                font_size=16
            )
            
            delete_button = Button(
                text="حذف",
                size_hint_x=0.25,
                background_color=(0.8, 0.1, 0.1, 1)
            )
            
            # ربط زر الحذف بدالة الحذف الخاصة به
            delete_button.bind(on_press=lambda x: self.delete_task(task_row))
            
            task_row.add_widget(task_label)
            task_row.add_widget(delete_button)
            
            self.tasks_box.add_widget(task_row)
            self.input_field.text = ""

    def delete_task(self, task_row):
        # إزالة المهمة من القائمة
        self.tasks_box.remove_widget(task_row)

if __name__ == '__main__':
    TaskApp().run()

import tkinter as tk

def create_palette():
    def save_palette():
        palette_name = name_entry.get()
        background = bg_entry.get()
        button_color = btn_entry.get()
        special_button = sp_btn_entry.get()
        text_color = txt_entry.get()
        palette_line = f"button(root, '{palette_name}', '#{button_color}', lambda: change_colors(['#{background}', '#{button_color}', '#{special_button}', '#{text_color}']))"
        root.clipboard_clear()
        root.clipboard_append(palette_line)
        preview_window()

    def preview_window():
        preview = tk.Toplevel(root)
        preview.title('Preview')
        preview.configure(bg='#' + bg_entry.get())
        label = tk.Label(preview, text='Preview', font=("Arial", 25), bg='#' + bg_entry.get(), fg='#' + txt_entry.get())
        label.pack(fill='x')
        button = tk.Button(preview, text='Special Button', bg='#' + sp_btn_entry.get(), fg='#' + txt_entry.get())
        button.pack()


    root = tk.Tk()
    root.title('Create Palette')

    name_label = tk.Label(root, text='Palette Name:')
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    bg_label = tk.Label(root, text='Background Color:')
    bg_label.grid(row=1, column=0)
    bg_entry = tk.Entry(root)
    bg_entry.grid(row=1, column=1)

    btn_label = tk.Label(root, text='Button Color:')
    btn_label.grid(row=2, column=0)
    btn_entry = tk.Entry(root)
    btn_entry.grid(row=2, column=1)

    sp_btn_label = tk.Label(root, text='Special Button Color:')
    sp_btn_label.grid(row=3, column=0)
    sp_btn_entry = tk.Entry(root)
    sp_btn_entry.grid(row=3, column=1)

    txt_label = tk.Label(root, text='Text Color:')
    txt_label.grid(row=4, column=0)
    txt_entry = tk.Entry(root)
    txt_entry.grid(row=4, column=1)

    save_button = tk.Button(root, text='Save Palette', command=save_palette)
    save_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()

create_palette()

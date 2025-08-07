Scrollable Frame Tkinter
========================
    
* Instructions
    * Create a widget using the scrollframe class ``scroll_frame = ScrollFrame(window)``
    * Now use the main_frame from scrollframe to add your widgets `` main_frame = ttk.Frame(scroll_frame) ``
    * Now you can add a widgets to the main_frame `` ttk.button(main_frame, text='This is a button inside a scollable frame').pack(fill='both', expand=True)``
* Note
    * When there is a more than 100 widgets in the frame resizing it becomes a little laggy but works fine after that.
    

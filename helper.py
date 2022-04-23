'''
navigation_helper = """
Screen:
    MDNavigationLayout:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Demo Application'
                left_action_items: [["menu", lambda x: app.navigation_draw()]]
                right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
                elevation:5
            Widget:
"""
'''
navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "First-Aid Bot | Home Screen"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                    Widget:
                    MDTextField:
                        id: user_name
                        hint_text: "Enter injury/disease name"
                        helper_text: "Or select from common ones.."
                        helper_text_mode: "on_focus"
                        icon_right: "redhat"
                        icon_right_color: app.theme_cls.primary_color
                        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x:None
                        width:300
                        
                    MDRectangleFlatButton:
                        text: "Show"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.show_data()
                    
                    Widget:
                    
                    
                    
        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "Capture.PNG"
                MDLabel:
                    text: "First-aid Bot"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "gtanish2020@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                        
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon: "face-profile"
                                    
                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon: "upload"
                                    
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
                            
"""

# import webbrowser
# webbrowser.open('https://www.google.com/')

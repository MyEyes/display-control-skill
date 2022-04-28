from mycroft import MycroftSkill, intent_file_handler


class DisplayControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.display.intent')
    def handle_control_display(self, message):
        self.speak_dialog('control.display')


def create_skill():
    return DisplayControl()


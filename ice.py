import easygui
flavor = easygui.buttonbox("wHat is your favorite color?",
         choices = ['Red', 'Blue', 'Green'])
easygui.msgbox("Your flavor is" + flavor)
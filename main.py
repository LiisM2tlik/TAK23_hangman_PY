from View import View
from Controller import Controller
import Database


if __name__ == '__main__':
    Database.create_table()
    view = View()
    controller = Controller(view)
    view.controller = controller
    controller.new_game()
    view.bind("<Return>", controller.send_letter)
    view.main()
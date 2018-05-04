import tkinter
import dimensions
import bot_structure
import time
def mv(window, bot_rect):
    window.canvas.move(bot_rect, 1, 0)
class gui :
    def __init__(self, root):
        self.root = root
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.pack()

root = tkinter.Tk()
root.geometry(str(dimensions.root_x)+"x"+str(dimensions.root_y))

window = gui(root)

bot = bot_structure.object('rectangle', dimensions.no_of_wheels, 
                                        dimensions.bot_width, 
                                        dimensions.bot_height, 
                                        dimensions.x_offset,
                                        dimensions.y_offset)
bot_rect = bot.draw_rect(window.canvas)
for i in range(100):
    time.sleep(0.01)
    window.canvas.move(bot_rect, 0, 1)
    #window.canvas.after(100, mv(window, bot_rect))
    root.update()
root.mainloop()

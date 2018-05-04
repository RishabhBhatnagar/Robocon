import tkinter
from motor import motor
class object:
    def __init__(self, shape = 'rectangle', no_of_wheels = 4, width = 50, height = 50, x_offset = 0, y_offset = 0):
        self.shape = shape
        self.no_of_wheels = no_of_wheels
        if shape == 'rectangle' : self.init_rect_model(width, height, x_offset, y_offset)
        
    def init_rect_model(self, width = 50, height = 50, x_offset = 0, y_offset = 0):
        '''
        ul : upper left      dl : down left
        ur : upper right     dr : down right
        
        MODEL : 
        
        ul----------ur
        |            |
        |            |
        |    BOT     |
        |            |
        |            |
        dl-----------dr
        '''
        #Setting up motors : 
        self.ul_motor = motor()
        self.ur_motor = motor()
        self.dl_motor = motor()
        self.dr_motor = motor()
        
        #setting coordinates:
        self.width = width
        self.height = height
        "These parameters will remain constant."
        
        #Offsets:
        "This is the factor which will change the position of the bot."
        self.x_offset = x_offset
        self.y_offset = y_offset
        
    def draw_rect(self, canvas):
        x1, y1 = self.x_offset, self.y_offset
        x2, y2 = x1 + self.width, y1 + self.height
        return canvas.create_rectangle(x1, y1, x2, y2)
        
        
        
        
        
        
        

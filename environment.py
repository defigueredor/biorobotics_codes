import constants as c

class ENVIRONMENT:

    def __init__(self, ID):

        self.l = c.L
        self.w = c.L
        self.h = c.L
        self.x = 0
        self.y = 0
        self.z = 0
        if (ID == 0):
            self.Place_Light_Source_To_The_Front()
        if (ID == 1):
            self.Place_Light_Source_To_The_Right()
        if (ID == 2):
            self.Place_Light_Source_To_The_Back()
        if (ID == 3):
            self.Place_Light_Source_To_The_Left()

        #print(self.l, self.w, self.h, self.x, self.y, self.z)

    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = 30*c.L
        self.z = 0

    def Place_Light_Source_To_The_Right(self):
        self.x = 30*c.L
        self.y = 0
        self.z = 0

    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = -30*c.L
        self.z = 0

    def Place_Light_Source_To_The_Left(self):
        self.x = -30*c.L
        self.y = 0
        self.z = 0

    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=0.5, g=0.5, b=0.5)
        sim.send_light_source(body_id=lightSource)

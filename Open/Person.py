import arcade

RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename):
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class Person(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()
        self.main_path = "person/"
        self.person_face_direction = RIGHT_FACING
        self.curr_texture = 0

        self.scale = 1

        self.run_textures = []
        self.create_run_textures()

        self.idle = True
        self.idle_textures = []
        self.create_idle_textures()

        self.texture = self.idle_textures[0][0]

    def create_run_textures(self):
        for i in range(1, 5):
            texture = load_texture_pair(f"{self.main_path}/kitty_walk/kitty-walk-{i}.png")
            self.run_textures.append(texture)

    def create_idle_textures(self):
        for i in range(1, 5):
            texture = load_texture_pair(f"{self.main_path}/kitty_idle/kitty-idle-1.png")
            self.idle_textures.append(texture)

    def update_animation(self, delta_time: float = 1 / 60):

        if self.change_x < 0 and self.person_face_direction == RIGHT_FACING:
            self.person_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.person_face_direction == LEFT_FACING:
            self.person_face_direction = RIGHT_FACING

        if self.change_x == 0:
            self.curr_texture += 0.5
            if self.curr_texture % 2 == 0:
                self.texture = self.idle_textures[0][self.person_face_direction]
                if self.curr_texture >= 4:
                    self.curr_texture = 0
                self.texture = self.idle_textures[int(self.curr_texture)][self.person_face_direction]

        if not self.idle:
            self.curr_texture = int(self.curr_texture)
            self.curr_texture += 1
            if self.curr_texture >= 4:
                self.curr_texture = 0
            self.texture = self.run_textures[self.curr_texture][self.person_face_direction]


import random
import arcade

from Person import Person


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "My first window"

PERSON_MOVEMENT_SPEED = 2

GRAVITY = 1


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=1/30)
        self.bg_layer_one = arcade.load_texture("bg/background-1.png")
        self.bg_layer_two = arcade.load_texture("bg/background-2.png")
        self.ground_list: arcade.SpriteList | None = None
        self.person: Person | None = None
        self.physics_engine: arcade.PhysicsEnginePlatformer | None = None

    def setup(self):
        self.ground_list = arcade.SpriteList()
        self.create_ground()
        self.create_person()
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.person,
            gravity_constant=GRAVITY,
            walls=self.ground_list
        )

    def create_person(self):
        self.person = Person()
        self.person.center_x = 50
        self.person.bottom = self.ground_list[0].top



    def create_ground(self):
        for j in range(0, SCREEN_WIDTH + 1, 16):
            r_sprite = random.randint(1, 2)
            ground = arcade.Sprite(f"enviroment/wall-{r_sprite}.png")
            ground.center_x = j
            ground.center_y = 5
            self.ground_list.append(ground)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer_one)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer_two)
        self.ground_list.draw()
        self.person.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.person.update_animation()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.person.change_x = -PERSON_MOVEMENT_SPEED
            self.person.idle = False
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.person.change_x = PERSON_MOVEMENT_SPEED
            self.person.idle = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.person.change_x = 0
            self.person.idle = True
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.person.change_x = 0
            self.person.idle = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
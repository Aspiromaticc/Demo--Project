from sys import exit
from random import randint
class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)
class Trial:
    jazzy = [
    "We are money launderers and heartbreakers",
    "Don't be scared to get lost and be found",
    "You are not lonely, if you don't feel alone. ",
    "They tell the child to dream and then they fear what they may become"
]


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene.enter()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
a_map = Map('jon_bright')
a_game = Engine(a_map)
a_game.play()

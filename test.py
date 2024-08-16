
#
# # scary_monsters = []
# # for monster in monsters:
# #     if monster[1] > 16:
# #         scary_monsters.append(monster[0])
# # print(scary_monsters)
#
# scary_monsters = [monster for monster in monsters if monster[1] > 16]
# print(scary_monsters)


# from monster import Monster
# monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]

# for monster in monsters:
#     if monster[1] > 16 or monster[2] == "red":
#         m1 = Monster(monster[0], monster[1], monster[2])
#         print(m1)
# for monster in monsters:
#     scary_monster = is_scary(monster, monster[1], monster[2])
#     print(scary_monster)
# import datetime
#
# date_string = '1/1/2022'
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
# print(date)

# from kivy.app import App
# from kivy.lang import Builder


# class HelloKv(App):
#    def build(self):
#        self.title = "Hello world!"
#        self.root = Builder.load_file('widget.kv')
#        return self.root
# HelloKv().run()

data, x = list('1bc'), 3
print(data[int()])

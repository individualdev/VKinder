import VKinder

if __name__ == "__main__":

    token = input('Token: ')

    vk = VKinder.VKinder(token)

    vk.run()

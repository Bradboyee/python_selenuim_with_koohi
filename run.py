from kanjikoohi.koohi import Koohi
import kanjikoohi.constants as const
import kanjikoohi.csv_writer as csv_writer

file = csv_writer.csv_writer()
with Koohi() as bot:
    bot.signin_page()
    bot.login(my_username=const.username, my_password=const.password)
    bot.study()
    # write header first
    file.write(["kanji", "story"])
    for i in range(1, 3000):
        print(f'page = {i} \n title = {bot.title}')
        kanji = bot.get_kanji()
        story_list = bot.get_story_list(3)
        print(kanji)
        print(story_list)
        file.append([kanji, *story_list])
        bot.next_kanji()

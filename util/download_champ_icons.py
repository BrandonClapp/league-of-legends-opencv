import wget

# icons
# https://leagueoflegends.fandom.com/wiki/Free_champion_rotation

urls = open('champ-icon-urls.txt')

lines = urls.readlines()

for line in lines:
    print(line)
    filepath = wget.download(line, out='champions')
    print(filepath)
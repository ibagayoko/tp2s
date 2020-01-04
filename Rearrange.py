import sys
from os import walk, makedirs, path as p
from collections import defaultdict


path = outDir = sys.argv[1]
if len(sys.argv) > 2:
    outDir = sys.argv[2]
files = []
listes =defaultdict(lambda : 0)
cours = path.split('-')[0]

DUMMYRAPPORTPATH = './DummyRapport.md'

# Get our file list
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)

i =1
# Perform
for f in files:
    af = f.split('_')
    # Liste des etudiants
    listes[af[0]] = af[1]
    dirname = '_'.join(af[:2])

    newDirectory = p.join(outDir, dirname)

    # Create the nw dir if not exists
    if not p.exists(newDirectory) :
        makedirs(newDirectory)
        rap = ''
        with open(DUMMYRAPPORTPATH, 'r', encoding='utf-8') as fi: rap = fi.read() 
        rap = rap.replace('DummyNom', af[0])
        rap = rap.replace('DummyCours', cours)
        rap = rap.replace('DummyCodePermanent', '')
        rap = rap.replace('DummyCourrier', '')
        note = open(p.join(newDirectory, 'Note.md'), 'w', encoding='utf-8') 
        note.write(rap)



    # Unzip tp
    if f.endswith('.zip'):
        import zipfile
        filePath= p.join(path, f)
        zf = zipfile.ZipFile(filePath)
        uzipName = ''
        unzipFolder = 'tp2'
        if zf.infolist()[0].is_dir():
            unzipFolder = zf.infolist()[0].filename
            uzipName = newDirectory
        else:
            uzipName = p.join(newDirectory, unzipFolder)
        zf.extractall(uzipName)
        zf.close()

    else:
        # Copy les autres fichier
        import shutil
        shutil.copy(p.join(path, f), newDirectory) 

    

with open("liste_%s.md"%cours, 'w', encoding='utf-8') as f:
    f.write("# Liste %s\n" % cours)
    f.write("|  ID | Nom | Note | Commentaires |\n")
    f.write("| --- | --- | --- | --- |\n")
    i =1
    for etu in listes:
        f.write("|%d|%s| \t| \t|\n"%(i,etu))
        i+=1
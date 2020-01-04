# ! /bin/bash

oIFS=$IFS
IFS=$'\n'

# Variables
PERL_MD_SCRIPT_PATH=./Markdown.pl
MARKDOWN_BASE_DIR=./
HTML_BASE_DIR=../html


# Supprimer les anciens fichiers HTML avant la génération des 
# nouveaux fichiers à partir des fichiers markdown.
rm -rf $HTML_BASE_DIR;
mkdir $HTML_BASE_DIR;

#Convertir en html tous les fichiers markdown qui se trouvent
#dans MARKDOWN_BASE_DIR et les transférer (en conservant la 
#même hiérarchie de répertoires) vers le HTML_BASE_DIR
#find $MARKDOWN_BASE_DIR -name '*-RESULT.txt' | while read -r markdownpath; do
find $MARKDOWN_BASE_DIR -name '*.md' | while read -r markdownpath; do

   #Trouver le path du fichier html correspondant au fichier
   #markdown courant.
   bname=$(basename $markdownpath);
   bname2="${bname%.*}";  #enlever l’extension .txt
   htmlpath="${bname%.*}".html; #Ajouter l’extension .html
   htmlpath="${markdownpath%/*}"/$htmlpath; #Ajouter la hiérarchie
   htmlpath=$HTML_BASE_DIR/"${htmlpath:12}"; #Ajouter le base dir
   echo $htmlpath;
   #Obtenir le nom du répertoire parent (htmlDir) de htmlpath
   bname2=$(basename $htmlpath);
   let "length=${#htmlpath}-${#bname2}";
   htmlDir="${htmlpath:0:$length}";
   
   #créer le répertoire (et sous-répertoires s’il y a lieu) 
   #pour enregistrer le fichier html courant.
   mkdir -p $htmlDir;   
  
   #Convertir le fichier markdown en html et enregistrer la sortie dans le 
   #fichier donné par $htmlpath
   perl $PERL_MD_SCRIPT_PATH $markdownpath > $htmlpath

done

IFS=$oIFS

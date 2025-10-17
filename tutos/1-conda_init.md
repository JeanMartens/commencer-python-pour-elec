# Initialisation de conda et premier environement python + installation des premieres librairies

### On va d'abord initialiser conda:

Ouvre un terminal de commande et Tapes `conda init`

Tu vas surement obtenir ca:
<img width="979" height="769" alt="image" src="https://github.com/user-attachments/assets/73000615-11ae-4b89-a852-9d46d029258d" />

Ferme l'invite de commande et ouvre VScode (ferme et reouvre si tu as deja VScode d'ouvert)

Va dans ton dossier de test de code ou de bidoullage (creer en un si tu veux)

*A partir de maintenant on utilise le terminal VScode (c'est le meme que celui que tu accedes en cherchant `cmd` mais dans VS code)*

Dans mon cas: `C:\Users\jeanb\Documents\misc-code`

Tape les lignes suivantes dans le terminal: (acceptation des termes et conditions conda)

<img width="1194" height="155" alt="image" src="https://github.com/user-attachments/assets/9eddcaa4-47ef-4b76-9296-c8828f5c6aad" />


```
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```

Ensuite tape la ligne suivante:

```
conda create -n learning_env python=3.12 -y
```

Si tout se passes bien, tu obtiens:
<img width="1284" height="612" alt="image" src="https://github.com/user-attachments/assets/af8916c3-6c2a-4355-bca6-ed47f73eedb0" />

### Pour activer l'environement et commencer a coder avec, fais:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Tu ne vas pas recevoir de messages normalement mais si tu en recois, ecrit `A` a la premiere question pour dire "Yes to All"

Ensuite:

```
conda init powershell
```

Redemarre a nouveau vs code (ferme bien toutes les pages)
Si ca a marché tu vas voir ca maintenant:
<img width="1286" height="311" alt="image" src="https://github.com/user-attachments/assets/2e8ae702-3839-4f90-a7ee-44f34b666cf1" />

Maintenant:
```
conda activate learning_env
```

A chaque fois que tu veux utiliser python avec cet environement en particulier, tu vas devoir utiliser cette commande a la creation du terminal donc note la qq part ou retiens la. (C'est pas dtt relou en pratique meme si ca a l'air maintenant.)

Tu peux voir quel environement tu utilises comme ca:
<img width="1282" height="315" alt="image" src="https://github.com/user-attachments/assets/d380c3fb-c65d-4628-b084-6c3fd0a7b25a" />

Une fois que c'est fait, petite verification:

```
python --version
```

<img width="1287" height="319" alt="image" src="https://github.com/user-attachments/assets/a4061bde-4374-46d1-8dbc-0e92284fec96" />

*Tout est bon.*

### On va maintenant installer les premiers packages pour te donner un example:

Tape la ligne suivante: (installation de numpy ET pandas ET matplotlib, trois packages differents)
```
pip install numpy pandas matplotlib
```

Si tu as ca tout est bon:
<img width="1245" height="318" alt="image" src="https://github.com/user-attachments/assets/be989f8f-b77f-476e-9a74-adef29e6693d" />

### Maintenant petit test pratique pour etre sur qu'on ai bien le bon env et qu'on puisse l'utiliser

Tu vas trouver dans le dossier `scripts` un petit code qui affiche la fonction `f(x) = sin(x) + 1` pour x de 0 a 2*`pi`

Je t'invite a copier le code et a le coller dans un nouveau fichier que tu vas appeller `plot_sin.py`

Une fois que c'est fait, lance le programme d'abord a l'aide tu terminal, dans mon cas: (tu peux clic droit sur le fichier puis `Copy Path` pour avoir l'adresse de ton fichier)

```
python C:\Users\jeanb\Documents\misc-code\commencer-python-pour-elec\scripts\plot_sin.py
```

On remarque que je suis bien sur l'env `learning_env`

<img width="1284" height="377" alt="image" src="https://github.com/user-attachments/assets/c79fd155-327e-45a4-9aa7-382035fa1ee5" />

J'obtiens le resultat suivant:
<img width="1920" height="1080" alt="{61BAF465-B920-4C07-8158-E71D25375E67}" src="https://github.com/user-attachments/assets/5603a6d4-8621-4118-bc89-d62ebdd0c74f" />

ainsi que le fichier `commencer-python-pour-elec\sin_plus_un.png` trouvable dans ce repo. 

### Maintenant, si tu veux pouvoir utiliser le debug ou faire tourner ton code a l'aide de VScode et non du terminal, voici la marche a suivre:

Regarde les icones a droite pour trouver le marketplace des extensions et tape `Python`

<img width="627" height="615" alt="image" src="https://github.com/user-attachments/assets/fabbd08f-2b70-4895-b09b-0d3dd08e2044" />

Installe les extensions soulignées.

Maintenant tu devrais voir une fleche en haut a droite et un bouton `Select Interpreter` en bas a gauche quand tu ouvres des `.py` avec VScode

<img width="1400" height="986" alt="image" src="https://github.com/user-attachments/assets/5f018a41-9ec1-4ca6-8b4a-d387065f24d9" />

C'est ici que tu choisis ton environement par defaut:

<img width="768" height="211" alt="image" src="https://github.com/user-attachments/assets/2678dd76-0605-4f83-a8ce-c61fc3e37b35" />

Tu choisis ca et tu peux cliquer sur la fleche pour faire tourner ton code sans ligne de commande (Attention, ton code sera lancé depuis le dossier VScode que tu as choisi au debut quand tu as `Open folder`, pas problematique ici mais bon a savoir...)

<img width="1381" height="703" alt="image" src="https://github.com/user-attachments/assets/623201ce-45ed-4664-a930-deb5eea1136f" />

**Tu obtiendras la meme chose qu'avant si tout marche bien.**



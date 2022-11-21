# Facial-Recognition-Python
Facial Recognition and image manipulation using Python and OpenCV


Introduction à la reconnaissance faciale :
La reconnaissance faciale est indispensable à la sécurité informatique.
Le visage est au cœur de l’identité humaine. Il nous distingue les uns des autres. C’est pour cela 
que la reconnaissance faciale est très importante.
La reconnaissance faciale est une tache facile pour le cerveau humain mais infiniment 
complexe pour une machine comme on connait peut des mécanismes employés par le 
cerveau. En effet, jusqu’à ce jour on ne sait pas comment notre cerveau reconnait un visage ou 
quels sont les traits qu’il prend comme repère .
C’est pour cela qu’on a décidé d’entamer ce projet qui emploie une forme basique de 
reconnaissance faciale avec le Haar Cascades Classifier, OpenCV et l’algorithme K-Nearest
Neighbors.


Technologies employées :
Python 3.11 , OpenCV (CV2) , Haar Cascades Classifier , IDE VS Code



Introduction à K-Nearest Neighbors : L’algorithme KNN (K-Nearest Neighbors) est un algorithme de Machine 
Learning Supervisé simple et facile à implémenter qui peut être utilisé pour 
résoudre des problèmes de régression et aussi de classification (comme on l’a 
employé dans notre projet)


Implémentation – Génération des données du Training
Nous avons :
Ecrit un script Python qui capte des image depuis la diffusion vidéo de la webcam
Extrait les visages du cadre d’image en utilisant Haar Cascades
Enregistre les données des visage dans une table (Array) Numpy
1. On lit et affiche la diffusion vidéo, tout en capturant des images
2. On détecte les visages et affiche leur Bounding Box avec Haar Cascade
3. On aplatit l’image qui est en niveaux de gris maintenant et la sauvegarde dans une 
table Numpy
4. On répète ce processus pour plusieurs personnes pour générer des données de Training


Implémentation – Construction du Classifier des visages
On utilise l’algorithme KNN pour reconnaitre les visages
Les étapes de la reconnaissance sont les suivants :
1. Chargement de la Training Data (des tables Numpy de toutes les 
personnes)
• Les valeurs x- sont stockées dans les Arrays Numpy
• On doit attribuer les valeurs y- pour chaque personne
2. Lecture de la diffusion video avec OpenCV
3. Extraction des visages de la vidéo
4. Utilisation de KNN pour trouver une prédiction du visage (int)
5. Cartographie de l’id prédit au nom de l’utilisateur
6. Affichage des prédictions sur l’écran – Bounding Box et nom

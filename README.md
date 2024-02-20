# Deep Learning Projet Zalando


Contexte

Fashion-MNIST est un ensemble de données d'images d'articles de Zalando, composé d'un ensemble d'entraînement de 60 000 exemples et d'un ensemble de test de 10 000 exemples. Chaque exemple est une image en niveaux de gris de 28x28 pixels, associée à une étiquette parmi 10 classes. Zalando a l'intention que Fashion-MNIST serve de remplacement direct à l'ensemble de données MNIST d'origine pour le benchmarking des algorithmes d'apprentissage automatique. Il partage la même taille d'image et la même structure de divisions d'entraînement et de test.

L'ensemble de données MNIST d'origine contient beaucoup de chiffres manuscrits. Les membres de la communauté IA/ML/Science des données adorent cet ensemble de données et l'utilisent comme référence pour valider leurs algorithmes. En fait, MNIST est souvent le premier ensemble de données que les chercheurs essaient. "Si ça ne fonctionne pas sur MNIST, ça ne fonctionnera pas du tout", disent-ils. "Eh bien, si ça fonctionne sur MNIST, ça peut quand même échouer sur d'autres."

Zalando cherche à remplacer l'ensemble de données MNIST d'origine.

Contenu

Chaque image mesure 28 pixels de hauteur et 28 pixels de largeur, pour un total de 784 pixels au total. Chaque pixel a une seule valeur de pixel associée, indiquant la clarté ou l'obscurité de ce pixel, les nombres plus élevés signifiant plus sombre. Cette valeur de pixel est un entier entre 0 et 255. Les ensembles de données d'entraînement et de test ont 785 colonnes. La première colonne se compose des étiquettes de classe (voir ci-dessus), et représente l'article de vêtement. Le reste des colonnes contient les valeurs de pixel de l'image associée.

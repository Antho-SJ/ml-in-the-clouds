# ML in the cloud

## Solution d'analyse des sentiments dans le cloud

Bienvenue dans ce projet ayant pour dessin de proposer une application prédictive s'appuyant sur des outils d'AutoML.

Qu'est ce que l'AutoML ?
Il permet d'automatiser une grande partie du processus de création d'un modèle de machine learning.
Ces outils proposant une interface graphique plus ou moins intuitive et ergonomique rendent plus abordable
l'utilisation du machine learning. Effectivement, la plupart de ces outils sont en no-code ou low-code.
Les Avantages !
La performance, l'éfficacité (gain de temps et de d'argent), on ajoute à ça qu'il n'est pas necessaire d'être un expert
pour manipuler ces outils.

Les outils d'AutoML les plus connus sont notamment Vertex AI, Sagemaker, Azure et DataRobot
Google Cloud Platform et Vertex AI sont le service could mis en place par google ainsi que sont outils d'AutoML déployé sur le cloud.
Cet outils permet d'utiliser le l'IA générative.
AWS et Sagemaker sont la plateforme cloud et le service d'AutoML de Amazon 
De même pour Azure et Azure machine learning, associés à Microsoft

Pour créer une telle application, nous allons nous servir du MLaaS. 

Qu'est ce que le MLaaS ?
Le machine learning as a service (MLaaS) est un service cloud mettant à disposition par exemple des outils d'AutoML
Les Avantages sont que le service cloud résout les fortes demandes en ressource de calcul du machine learning.
De plus il permet aux entreprises par exemple de se reposer sur quelque chose de déjà exsistant et donc laisser l'infrastructure
de ses solutions hors de leurs locaux.

Revenons au sujet, nous allons donc créer une application qui prédit le "thème émotionnel" d'une phrase donnée. Pour ce faire, nous avons à disposition deux jeux de données : un qui est censé être dédié à l'entraînement et un autre au test du modèle prédictif. N'étant pas satisfait de l'échantillon d'entraînement, nous avons fait quelque fusion entre nos jeux de données afin de créer des jeux de données "meilleurs" mais nous verrons que ce n'est pas forcément la meilleure méthode qui apportera les meilleurs résultats.

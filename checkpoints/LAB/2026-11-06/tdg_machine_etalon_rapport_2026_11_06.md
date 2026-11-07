# TDG — Machine étalon de relativité générale et diagnostic par substitution

**Statut :** laboratoire exploratoire; code exécuté et tests numériques/symboliques vérifiés; **aucune dérivation de la relativité générale à partir du Q microscopique de TDG revendiquée**.  
**Date de l'expérience :** 6 novembre 2026.  
**Fichiers :** `tdg_machine_etalon_2026_11_06.py`, `tdg_machine_etalon_resultats_2026_11_06.json`.

## 1. Question et protocole

Construire d'abord une machine de gravitation **dont le fonctionnement est connu**, injecter l'obstruction mathématique documentée de TDG, puis remplacer seulement l'élément qui échoue par une loi de référence. Une réparation n'est pas promue en théorème TDG tant qu'elle n'est pas obtenue à partir du Q de TDG.

Sous-systèmes :

1. Gravitation **linéarisée**, avec un tenseur symétrique sans trace (STF) à cinq composantes et les contraintes transverses en espace de Fourier qui laissent **deux modes**.
2. Gravitation **non linéaire**, avec une métrique de Kasner du vide qui satisfait exactement `Ricci=0` et dont la courbure de Riemann est non nulle.
3. **Lentille d'actualisation** indépendante : carte de décohérence CPTP à deux états, enregistrement durable seulement comme interprétation opérationnelle; la sélection d'un résultat individuel (Born) est importée et n'est pas dérivée.
4. **Injection de panne TDG** : le représentant de l'unique canal S4 documenté, `J=-(1/sqrt(3))[yz→x,xz→y,xy→z]`, et son coefficient formel `c_inf≈10.769201` (lecture de septembre 2026). Son identification aux tenseurs **spatiaux physiques** ordinaires reste une hypothèse du banc d'essai, pas une équivalence Q/GR établie.

Sources primaires du projet :

- [`CURRENT_FRONT_LATEST.md`](https://github.com/jonathanduchesne-lab/TDG/blob/main/CURRENT_FRONT_LATEST.md), front MRP9B et limites physiques en cours.
- [`TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md`](https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-09-18/TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md), forme canonique de J.
- [`TDG_B5_TO_GR_BRANCH_STOP_CURRENT_ROOT2_2026-10-06.md`](https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-10-06/TDG_B5_TO_GR_BRANCH_STOP_CURRENT_ROOT2_2026-10-06.md), limite scalaire de B5 et obstruction STF.

## 2. La machine fonctionne sur deux tests GR indépendants

### Ondes gravitationnelles linéaires

Une perturbation symétrique sans trace `h_ij` possède cinq composantes indépendantes. Pour chaque vecteur d'onde `k`, l'opérateur `D_k(h)_i = k^j h_ij` impose trois conditions indépendantes, d'où deux polarisations physiques `+` et `×`.

- Dimension du noyau TT : **2**.
- Évolution harmonique à fréquence `omega=1.7` : variation relative maximale de l'énergie **7,69×10^-16** sur 601 échantillons.
- Violation maximale de divergence : **0** dans le repère k=z.
- Défaut de covariance rotationnelle de la divergence `D_(Rk) U_5(R) = R D_k`, sur 300 rotations aléatoires : **1,05×10^-15** au maximum.

### Solution exacte, non linéaire

La métrique de Kasner

`ds² = -dt² + t^(2p1) dx² + t^(2p2) dy² + t^(2p3) dz²`

avec `p=(-1/3,2/3,2/3)` satisfait `Σ p = Σ p² = 1`.

Calcul direct des symboles de Christoffel et du Ricci par SymPy : **les 16 composantes Ricci sont exactement nulles**. La contrainte hamiltonienne du vide est exactement nulle. Pourtant la métrique est courbe :

`R_0101=-4/(9 t^(8/3))`, `R_0202=2/(9 t^(2/3))`, et `R_abcd R^abcd=64/(27 t^4)>0`.

C'est une vraie solution d'Einstein, mais **très particulière**, pas un solveur de toute la relativité générale.

## 3. Injection de l'obstruction TDG J dans la machine

Dans la base STF orthonormée

`E0=(xx-yy)/sqrt(2); E1=(xx+yy-2zz)/sqrt(6); E2=(xy+yx)/sqrt(2); E3=(xz+zx)/sqrt(2); E4=(yz+zy)/sqrt(2)`, le représentant physique tenté est

`J(E4)=-ex/sqrt(3); J(E3)=-ey/sqrt(3); J(E2)=-ez/sqrt(3); J(E0)=J(E1)=0`.

Pour une onde se propageant suivant z, les deux polarisations TT sont `E0` et `E2`. Ainsi :

- `D_z(E0)=D_z(E2)=0` : les deux modes sont admissibles en GR.
- `J(E0)=0`, mais `J(E2)=-ez/sqrt(3)≠0` : **le couplage J affecte une polarisation physique**.
- Si l'on impose directement `J h=0`, **une seule** polarisation TT subsiste pour k=z.
- Pour 300 directions génériques de k, `ker(J) ∩ ker(D_k)` est de dimension **0**, donc la contrainte naïve supprimerait **les deux** polarisations.
- Dans cette identification, aucune combinaison `D_k` ne reproduit `J` : la meilleure approximation linéaire a un écart relatif de **100 %**, parce que le canal J est orthogonal à toutes les divergences simples D_k dans la norme de Frobenius.

La covariance rotationnelle du J fixe échoue (défaut relatif médian sur 300 rotations aléatoires : **1,401**). Dans le même banc, celle de D_k est exacte au plan numérique.

**Point de prudence décisif :** la source historique J est un entrelaceur `S4` entre représentations Q. Le passage à une base tensorielle physique STF et à l'action SO3 de l'Univers n'a pas été dérivé du Q. La gravité de cette panne est donc **conditionnelle à cette identification**. Elle précise le défaut d'un pont tenté; elle ne prouve pas que toute représentation possible du modèle microscopique échoue.

## 4. Les réparations testées

### A — Remplacer J par une divergence covariante

Échange de la loi algébrique fixe `J` pour `D_k(h)_i=k^j h_ij`.

Résultat : les deux modes TT survivent, leur fuite vectorielle via D_k est exactement nulle et la covariance de rotation est restaurée.

Dans un diagnostic dynamique **inventé uniquement pour comparer les deux lois** `dv/dt=-0.7v+c_inf M h_TT(t)` :

- `M=J` : fuite vectorielle maximale **1,23977** (unités arbitraires du banc).
- `M=D_k` : fuite maximale **0**.

Cette réparation *fait fonctionner la machine* mais **ne dérive pas D_k de TDG**. C'est la cible précise d'une nouvelle loi Q-native qui relierait une réponse locale à la direction physique de propagation et aux transports entre cellules.

### B — Moyenner les orientations

Un moyenneur isotrope sur les 24 rotations propres du cube annule exactement l'intertwiner J **en moyenne**, mais sa norme quadratique est conservée : `E||J_R||²=||J||²=1`. La moyenne n'élimine donc pas le couplage physiquement possible au niveau d'un événement ou d'une région. C'est une réparation cosmétique, non retenue.

### C — Activer la correction scalaire B5

L'extension documentée `DeltaW=(15/4)|I><I|` ne produit aucune action sur les cinq bases STF : défaut maximal **0**. Elle ne peut réparer ce couplage non scalaire, quel que soit son coefficient. C'est un défaut de **type**, pas d'intensité.

### D — Surveillance quantique très fréquente (Zénon)

J'ai construit un Hamiltonien jouet 8×8 couplant 5 composantes tensorielles à 3 composantes vectorielles selon J. Après une durée totale de 6 unités, une succession de contrôles projectifs du sous-espace TT donne :

| Nombre de contrôles | Probabilité de rester dans le sous-espace TT à tous les contrôles |
|---:|---:|
| 1 | 70,50 % |
| 10 | 29,67 % |
| 100 | 88,69 % |
| 1 000 | 98,81 % |
| 2 000 | 99,40 % |

Non-monotonie possible à faible nombre de mesures à cause de l'évolution cohérente entre les contrôles. À fréquence infinie, la survie tend vers 100 % dans ce jouet : **l'effet Zénon fournit un mécanisme physique réel de confinement d'un secteur**. Cependant le projecteur TT surveillé a été **importé de GR**, et rien dans l'actuel Q/TDG ne démontre que son environnement mesure précisément ce projecteur ni qu'il garantit la symétrie voulue.

### E — Lentille de décohérence

Carte CPTP de déphasage `rho -> K0 rho K0†+K1 rho K1†`, avec visibilité `eta=e^(-gamma t)`; trace et positivité vérifiées. À `gamma=0,8`, `t=2`, la cohérence vaut `0,2018965` tandis que la probabilité diagonale reste `0,5`.

La carte permet de stabiliser effectivement les enregistrements; elle ne dérive ni la sélection ontologique d'un résultat unique ni les contraintes de gravité. Aucun « clic » ne transforme automatiquement J en D_k.

## 5. Diagnostic de l'architecture TDG

La question **n'est plus seulement** pourquoi TDG ne donne pas Einstein. Nous avons isolé la condition mathématique d'un pont viable :

1. Au lieu d'un entrelaceur algébrique fixe `STF5 -> V3`, il faut un opérateur **conditionné par des données géométriques qui se transforment** (momentum `k`, dérivée covariante, repère et connexion dynamique), par exemple `D_k` ou sa version courbe `nabla^j h_ij`.
2. Les contraintes qui annulent les canaux auxiliaires doivent être **de première classe**, préserver deux degrés de liberté et respecter les opérations régionales/cellulaires du modèle.
3. Si la courbure SU2 interne détectée par TDG devait devenir une connexion de jauge, il faudrait une véritable identité de Gauss dérivée du Q, pas simplement la rebaptiser comme telle.
4. La sélection par décohérence pourrait *stabiliser* le secteur ainsi dérivé; elle ne justifie pas à elle seule pourquoi le projecteur physique est celui d'Einstein.
5. Une extension non linéaire doit ensuite fermer l'algèbre de déformation des hypersurfaces et conserver la structure h^-1 de GR sans être ajoutée en tant qu'axiome cible.

## 6. Verdict et seuil de réussite du pont

- **Dérivé/vérifié dans la machine étalon :** deux modes TT, covariance du mécanisme D_k, conservation de l'énergie, métrique non linéaire Kasner exacte du vide, échec de J comme divergence et de la contrainte J h=0, capacités et limites du Zénon conditionnel.
- **Conditionnel :** l'identification du J de TDG à des tenseurs spatiaux physiques; les équations de comparaison pour fuite vectorielle; les projecteurs mesurés par l'environnement.
- **Non dérivé :** le fait que le Q de TDG engendre `D_k`, une connexion de jauge et des contraintes de première classe, et finalement les équations d'Einstein dans toutes les configurations.

**Le pont n'est pas encore trouvé à partir de TDG. En revanche, une machine de gravitation qui fonctionne et un banc de substitution sont maintenant reproductibles. Le premier défaut à chercher à la source n'est pas un mauvais coefficient : c'est l'absence démontrée d'une promotion naturelle de l'entrelaceur S4 vers un opérateur spatial différentiel covariant qui protège les polarisations TT.**

À reprendre sur le Q exact de TDG : calculer si le canal J devient un opérateur `k`/connexion-dépendant après réponse de cellule, prolongation de processus et passage au quotient prédictif. Le front MRP9B comporte une lacune de provenance pour les cartes numériques Q-B1592, donc aucun résultat « source Q réparé » ne doit être revendiqué sans ces données.

**Aucun fichier canonique TDG ni dépôt GitHub n'a été modifié.**

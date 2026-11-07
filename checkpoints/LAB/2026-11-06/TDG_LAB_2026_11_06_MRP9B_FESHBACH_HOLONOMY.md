# TDG / Root2 — MRP9B : réponse de Feshbach, holonomie et obstacle de courbure interne

**Date :** 6 novembre 2026 (heure de Toronto)  
**Type :** laboratoire exploratoire / comparateur de structure Q, NON canonique.  
**Statut :** dérivations exactes et contrôles numériques positifs DANS le comparateur ; **aucune dérivation du vrai Q-B1592, de GR ou de HDA**.  
**Auteur / attribution du programme TDG :** Jonathan Duchesne ; banc d'essai élaboré en collaboration avec ChatGPT.  
**Reproduction :** `tdg_mrp9b_feshbach_holonomy_2026_11_06.py`, résultats JSON, journal d'exécution et manifeste SHA-256.

## 1. Question et provenance

Notre projet cherche un transport physique entre deux cellules B4 partageant la même face B3/M2, avant toute comparaison avec Einstein. Les checkpoints `MRP9` et `MRP9A` du 14 octobre attestent historiquement une carte non compacte GL2/SL2 issue de Q-B1592/Q-B1602, mais **n'en fournissent pas l'implémentation numérique exacte**. Les rapports de récupération historiques contiennent la prescription de réponse par blocs du résolvant

`C_{p|e}=R_{pe}R_{ee}^{-1}` et sa normalisation déterminant pour des ports M2 ; cette prescription est un antécédent de la famille Q, **non la preuve que le nouveau Σ ci-dessous est identique à la carte Q-B1592**.

Documentation de référence :

- `CURRENT_FRONT_LATEST.md`, dépôt `jonathanduchesne-lab/TDG` ;
- `checkpoints/SENTRY/2026-10-14/TDG_MRP9_PREDICTIVE_FIBRE_CHART_LOCALIZATION_PARTIAL_2026-10-14.md` ;
- `checkpoints/SENTRY/2026-10-14/TDG_MRP9A_SAME_FACE_LINK_PROVENANCE_GAP_2026-10-14.md` ;
- `checkpoints/SENTRY/2026-10-06/TDG_B5_EXTENSION_V0_4_COMB_HDA_INSUFFICIENT_FRAME_CURVATURE_WALL_2026-10-06.md` ;
- archive de Library `Complete_TDG_Root1_Root2_Recovery_A_to_Z_2026-08-15_QB1592.md`, rubrique Q-B1191–1204 et Q-B1592.

### Choix délibérément non canonique

Le Hamiltonien et les valeurs de ses sources internes sont **synthétiques**. Nous conservons exclusivement les types dimensionnels documentés : cœur B4 de dimension complexe 6, port B3 de dimension complexe 2, incidence bare 6×2 et identité interne M2. Nous ne récupérons pas l'exécutable Q-B1592. Aucun paramètre n'est ajusté sur des observables gravitationnelles ou des valeurs du TDG gelé.

## 2. La construction minimale, sans pseudoinverse

Partitionner un Hamiltonien hermitien en port e de dimension 2 et cœur B de dimension 6 :

\[
H=\begin{pmatrix}0 & B^\dagger\\ B&H_B\end{pmatrix},\quad R(z)=(zI_8-H)^{-1}.
\]

L'identité de blocs est exacte :

\[
R_{Be}R_{ee}^{-1}=(zI_6-H_B)^{-1}B.
\]

La contraction par le **même B** produit la réponse effective bien typée M2 :

\[
\Sigma=B^\dagger R_{Be}R_{ee}^{-1}=B^\dagger(zI_6-H_B)^{-1}B\in M_2(\mathbb C).
\]

Il s'agit d'une auto-énergie de Schur/Feshbach, pas d'une réduction arbitraire du bloc rectangulaire 6×2. Son utilisation comme *attachment chart* MRP est une **nouvelle hypothèse de travail, pas le théorème Q-B1592**.

Pour la vérification analytique, poser `z=2`, `w=(1,2,1)/sqrt(6)`, `B=a(w⊗I2)` et `H_B=I3⊗[a(v·σ)]`. Les matrices de Pauli sont notées `σ_i`. Alors :

\[
\Sigma(a,v)=a^2(2I_2-a\,v\cdot\sigma)^{-1}.
\]

Pour `|v|=1`, son normalisé déterminant est :

\[
K(a,v)=\frac{\Sigma}{\sqrt{\det\Sigma}}=
\frac{2I_2+a\,v\cdot\sigma}{\sqrt{4-a^2}}\in SL(2,\mathbb C).
\]

Au voisinage de `v=0`, les trois dérivées suivant `v_x,v_y,v_z` sont indépendantes : **rang 3**, de type boost hermitien. La construction factorisée purement scalaire `H_B∝I2` donne `K=I2` exactement.

## 3. Le test essentiel : lien non central versus courbure

Le lien de deux cellules C,D sur une face commune F prend la forme relative

\[
L_{D\leftarrow C;F}=K_{D,F}K_{C,F}^{-1}.
\]

**No-go de pure jauge.** Si `K_{C,F}=G_C H_F` avec un cadre `G_C` dépendant de la cellule et `H_F` commun à la face, alors, exactement,

\[
L_{D\leftarrow C;F}=G_DG_C^{-1},\qquad
\prod_{\partial\square}L=I_2.
\]

Même des liens **non centraux** peuvent donc être parfaitement plats. Le test contrôle ce fait numériquement, avec erreur de boucle environ `10^-15` alors que les liens individuels diffèrent de l'identité d'environ 0,05 à 0,20.

**Construction de courbure possible, mais hypothétique.** Un anneau de quatre faces différentes possède des réponses internes de directions successives `x,y,-x,-y`, chacune reconstruite par la même règle de Schur, avec des contrastes dépendant de la face. Avec composition ordonnée, le produit de boucle `P(a)` satisfait :

\[
\boxed{\lim_{a\to0}\frac{\log P(a)}{a^2}
=\frac{[\sigma_y,\sigma_x]}{4}
=-\frac{i}{2}\sigma_z\neq0.}
\]

La norme de Frobenius du générateur limite vaut `sqrt(1/2)=0.7071067811865476`. Rien ne garantit encore que de telles variations par face soient générées par le même Q de TDG.

### Résultats de raffinement

| a | `||P−I||` | `||log(P)/a²||` | erreur au générateur limite |
|---:|---:|---:|---:|
| 0,4 | 0,1276721 | 0,7982841 | 0,2256777 |
| 0,2 | 0,0291471 | 0,7286924 | 0,1030493 |
| 0,1 | 0,0071243 | 0,7124330 | 0,0503765 |
| 0,05 | 0,0017711 | 0,7084340 | 0,0250469 |
| 0,025 | 0,0004421 | 0,7074383 | 0,0125059 |
| 0,0125 | 0,0001105 | 0,7071897 | 0,0062507 |

La covariance sous changement commun de repère SU2 sur chaque boucle, l'identité exacte de résolvant, l'annulation de facteur droit commun aux faces et les déterminants unitaires sont vérifiés entre `10^-15` et `10^-14` dans l'éventail testé.

## 4. Le test d'échelle microscopique

Si l'amplitude du contraste interne suit `a^p`, l'holonomie de deux directions non commutatives est d'ordre `a^(2p)`. Une courbure `log(P)/a²` finie et non nulle exige **p=1 dans cette famille** :

- `p=0` : courbure normalisée divergeant comme `a^-2` (facteur 4 quand a est divisé par 2) ;
- `p=1` : courbure convergeant vers un non-zéro (rapports 0,978 ; 0,994 ; 0,999) ;
- `p=2` : courbure tendant vers zéro (facteurs ~0,25 à chaque division de a par 2).

**La loi p=1 est un résultat conditionnel de la demande de courbure limite finie ; elle n'est pas dérivée du Q microscopique.**

## 5. Pourquoi ce résultat ne résout PAS encore GR

Le groupe des réponses est `SL(2,C)`. Par congruence `X→KXK†` sur `Herm2`, il préserve exactement le déterminant lorentzien. Le contrôle au pas `a=0,05` donne un défaut de la relation `Lambda^T eta Lambda=eta` de `1,33×10^-14`.

**Mais** les commutateurs de deux générateurs hermitiens de type boost produisent des générateurs antihermitiens de rotation :

\[
[\sigma_x,\sigma_y]=2i\sigma_z,\quad
[\sigma_y,\sigma_z]=2i\sigma_x,\quad
[\sigma_z,\sigma_x]=2i\sigma_y.
\]

Leur rang réel est **3**. C'est précisément la forme d'un secteur de courbure verticale SU2/repère qui bloque déjà la fermeture dynamique dans Q-B1846/47 et B5 v0.4, faute de loi de Gauss démontrée. Le laboratoire montre ainsi deux choses simultanément :

1. une origine possible de courbure lorentzienne et de la connexion par réponses de Schur ;
2. **une reproduction du type de l'obstruction de courbure interne**, pas son élimination.

Nous n'avons ni une métrique différentielle issue du Q exact, ni la contrainte de Gauss première classe, ni la fermeture HDA, ni le secteur non linéaire d'Einstein. Le canal tensoriel `l=2→l=1` reste non annulé dans le Q canonique et n'a pas été recalculé ici.

## 6. Verdict et prochaine expérience

### DERIVED, dans le comparateur

- Identité de Schur résolvante 6×2 → M2, sans pseudoinverse ;
- rang 3 des directions de réponse Herm2 ;
- links non centraux, mais holonomie exactement nulle lorsqu'ils factorisent cellule×face ;
- courbure de boucle non nulle et convergente pour des charts dépendant réellement de la face, avec loi a^1 ;
- préservation du déterminant lorentzien ;
- génération inévitable d'un sous-secteur vertical SU2 de rang3 à partir de boosts non commutatifs.

### ASSUMED / NON DERIVED

- Hamiltonien 8×8 synthétique et ses sources face-dépendantes ;
- utilisation de `detnorm(Σ)` comme chart prédictif Q-B1592 ;
- transport des chartes entre deux cellules réellement présentes dans le Q-B1852 gelé ;
- loi d'échelle microscopique `a^1`.

### OPEN / NEXT — MRP9B et au-delà

1. Retrouver l'implémentation effective de Q-B1592/Q-B1602, ou une reconstruction unique à partir du Q gelé et des données d'intervention.
2. Sur deux cellules B4 voisines du **même Q**, construire leurs deux charts d'une face B3 commune, sans `C6→C2` choisi à la main.
3. Tester non seulement la **non-centralité**, mais aussi la **non-factorisation cellule×face** sur des boucles ; comparer `log(P)/a²` entre raffinements b4 et b24.
4. Mesurer si le secteur SU2 vertical est une vraie contrainte première classe ou s'il reste observable ; ne pas le déclarer jauge par analogie.
5. Seulement ensuite revenir aux tests SAME-h, au défaut `l=2→l=1` et aux contraintes d'Einstein.

**Décision :** le programme de géométrie relationnelle gagne un nouveau banc discriminant, mais MRP9B demeure ouvert. Le Q, le front scientifique et les checkpoints historiques restent intacts.

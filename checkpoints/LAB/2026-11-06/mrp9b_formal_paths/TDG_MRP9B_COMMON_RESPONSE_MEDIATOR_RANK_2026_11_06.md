# TDG / Root2 — MRP9B : borne minimale du médiateur commun des deux réponses

**Date :** 2026-11-06 (America/Toronto).  
**Statut :** CONSÉQUENCE MATHÉMATIQUE CONDITIONNELLE + RÉANALYSE DES DONNÉES DÉJÀ SAUVEGARDÉES.  
**Portée :** carte de laboratoire Q-B1592 transplantée sur le Hamiltonien Q-B1852, à point spectral complexe fini.  
**Aucun nouveau calcul sur le Q historique n'a été exécuté pour cette note.** Les valeurs numériques sont recopiées sélectivement depuis les résultats de laboratoire vérifiables.  
**Autorité canonique :** Q-B1858L, CURRENT_FRONT_LATEST.md et MASTER_RECOVERY_LIVE.md inchangés. Aucune GR ni loi d'actualisation n'est dérivée.

## 1. Question précise

Les deux réponses du laboratoire sont des applications linéaires de la même fibre parentale :

\[
F=L_{\mathrm{pre}}(z):\mathbb C^6\to\mathbb C^2,\qquad
G=L_{\mathrm{post}}(z):\mathbb C^6\to\mathbb C^2.
\]

On voulait un transport exact de dimension 2, donc une matrice \(K\in M_2(\mathbb C)\) telle que \(G=KF\). Le rapport antérieur a trouvé numériquement \(\operatorname{rank}(G|_{\ker F})=2\) sur les cas b4 testés, ce qui interdit déjà cette factorisation.

Question supplémentaire : si l'on demande seulement un *médiateur linéaire commun* \(M:\mathbb C^6\to W\) permettant \(F=AM\) et \(G=BM\), quelle dimension doit nécessairement avoir \(W\), **sans imposer de loi de Q à ce médiateur** ?

## 2. Lemme algébrique exact, indépendant d'une pseudo-inverse

Pour toute paire d'applications linéaires \(F:V\to X\) et \(G:V\to Y\) de dimension finie, définissons

\[
\Phi=(F,G):V\to X\oplus Y,\quad v\mapsto(Fv,Gv).
\]

La projection de \(\operatorname{im}\Phi\) vers \(\operatorname{im}F\) est surjective et son noyau est isomorphe à \(G(\ker F)\). La suite exacte correspondante donne

\[
\boxed{\operatorname{rank}\Phi =
\operatorname{rank}F+\operatorname{rank}(G|_{\ker F}).}
\]

Si \(F=AM\) et \(G=BM\), alors \(\Phi=(A,B)M\). Par conséquent,

\[
\boxed{\dim W\ \ge\ \operatorname{rank}M\
\ge\ \operatorname{rank}\Phi.}
\]

La borne est atteignable *en algèbre linéaire abstraite* en posant \(W=\operatorname{im}\Phi\) et \(M=\Phi\). Cette construction tautologique **n'est pas** la dérivation d'un médiateur physique Q-natif ni une sélection canonique de fibre prédictive.

Ainsi, si \(\operatorname{rank}F=2\) et \(\operatorname{rank}(G|_{\ker F})=2\), tout médiateur linéaire reproduisant exactement les deux réponses a **dimension au moins 4**. Aucun transport exact \(2\times2\) ne descend de ces seules cartes.

## 3. Pourquoi le rang de F vaut 2 dans la portée examinée

Les programmes précédents prennent \(F=C^\dagger R_{TT}\) avec \(C^\dagger:\mathbb C^6\to\mathbb C^2\) de rang 2, \(R=(zI-H)^{-1}\), \(H=H^\dagger\), et \(z=2+0.7i\). Pour tout vecteur non nul \(v\), lorsque \(\operatorname{Im}z>0\),

\[
\operatorname{Im}\langle v,Rv\rangle
=-(\operatorname{Im}z)\|Rv\|^2<0.
\]

La compression \(R_{TT}=P_T^\dagger RP_T\) sur les six colonnes indépendantes du parent a donc partie imaginaire strictement négative, donc est inversible. Puisque \(C^\dagger\) est de rang 2, \(F=C^\dagger R_{TT}\) a rang 2. Cette justification est propre au résolvant d'un Hamiltonien hermitien et au readout complexe indiqué.

## 4. Appui numérique déjà archivé — neuf cas b4

Données originales : formal_descent_results.json, généré par verify_mrp9b_formal_descent.py. Les trois couples cellule/face suivants ont été vérifiés à chacun des trois cutoffs :

- T=(0,1,2,3), F=(0,1,2) ;
- T=(0,1,2,4), F=(0,1,2) ;
- T=(0,1,2,3), F=(0,1,3).

Sur les **neuf cas** à \(z=2+0.7i\), la restriction \(G|_{\ker F}\) a le **rang numérique 2**. Pour le premier couple :

| a | Première valeur singulière | Seconde valeur singulière | Rang numérique |
|---:|---:|---:|---:|
| 0.05 | 4.141588e-5 | 4.130858e-5 | 2 |
| 0.025 | 5.095991e-6 | 5.092694e-6 | 2 |
| 0.0125 | 6.344907e-7 | 6.343881e-7 | 2 |

Les neuf valeurs de rang sont tirées des champs finite_readout.null_response_rank. L'obstruction formelle à l'ordre 3 a elle aussi rank_null=2 dans ces neuf entrées, avant lecture spectrale. Ces vérifications restent **numériques**, sur ces configurations, pas un théorème universel pour tous les cutoffs, tous les readouts, toutes les faces ou toutes les réalisations de Q.

**Corollaire restreint :** pour les neuf cartes à readout fini ainsi examinées, la donnée jointe \((F,G)\) a rang 4. Un médiateur commun linéaire exact de dimension 2 ou 3 est impossible, même si un raccordement approché de dimension 2 devient de plus en plus précis en norme.

## 5. Piège de limite : petitesse et rang ne sont pas la même chose

Les valeurs singulières de la réponse sur le noyau décroissent quand \(a\) est divisé par deux, mais restent strictement positives dans les cas calculés. Une norme qui tend vers zéro peut permettre une **descente asymptotique approchée**, sans fournir la **descente exacte à cutoff fini**. En général :

\[
\operatorname{rank}\!\left(\lim_{a\to0}\Phi_a\right)
\quad\text{ne doit pas être identifié à}\quad
\lim_{a\to0}\operatorname{rank}(\Phi_a).
\]

L'égalité ou non au continuum doit être décidée par une construction contrôlée du quotient physique et de son sens de convergence, pas par un seuil de petite norme arbitraire.

## 6. Ce que cela ne démontre PAS

- Cela n'oblige pas la **fibre physique** de TDG à devenir 4D. La borne porte sur la représentation linéaire *jointe des deux cartes du résolvant persistant* dans cette transplantation de laboratoire.
- Cela ne dérive pas un état physique supplémentaire, un spinor à quatre composantes, une variable de jauge, une loi de Born ou une nouvelle connexion canonique.
- Un véritable processus selected-future/fresh-comb pourrait modifier l'une des deux réponses : la borne ne lui est pas automatiquement transférable.
- Le rang algébrique de \((F,G)\) ne prouve aucune naturalité au changement de face, aucune covariance au raffinement, aucune géométrie SO(3), aucune HDA et aucune GR.
- Les résultats b24 de l'audit de moments montrent un défaut d'ordre 3, mais ce fichier ne certifie **pas** le même tableau de rang joint à readout fini pour b24 ; ne pas étendre silencieusement l'énoncé.

## 7. NEXT : test falsifiable qui respecte les firewalls

1. Construire, **à partir d'une loi de processus Q effectivement autorisée**, des réponses conditionnelles \(F_{\mathrm{sf}},G_{\mathrm{sf}}\), et non seulement remplacer \(H\) par un opérateur triangulaire non hermitien.
2. Vérifier explicitement, sur faces communes, \(\operatorname{rank}(G_{\mathrm{sf}}|_{\ker F_{\mathrm{sf}}})\) et le comportement du médiateur prédictif sous composition et raffinement. Un rang 0 donnerait la porte algébrique nécessaire au transport M2 exact ; un rang non nul imposerait soit plus de données effectivement prédictives soit une notion de transport/quotient différente, à dériver.
3. Séparer cette vérification du no-go indépendant sur le couplage \(l=2\to l=1\) et de la courbure interne SU2 ; aucune amélioration du premier défaut ne suffit à déduire Einstein.
4. Avant tout changement du front, exiger des résultats Q-natifs, reproduits et target-blind ; ne pas modifier les coefficients de Q ni les checkpoints historiques.

## 8. Provenance

- Rapport source : [REPORT.md](REPORT.md).
- Résultats calculés : [formal_descent_results.json](formal_descent_results.json).
- Programme d'origine : [verify_mrp9b_formal_descent.py](verify_mrp9b_formal_descent.py).
- Source historique certifiée : qb1852_full_refined.py, SHA-256 ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7.

**Classification finale : DERIVED (lemme général), CONDITIONAL + NUMERIC (application aux neuf cartes du laboratoire), ASSUMED/OPEN (statut physique de la carte, naturalité et selected-future), NOT DERIVED (GR).** Aucun fichier canonique n'a été modifié.
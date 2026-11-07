# TDG — Lentille scientifique de decoherence et enregistrements

**Date :** 2026-11-06  
**Statut :** SANDBOX de diagnostic, non promotion scientifique, sans modification du modele TDG original.

## Modele source et perimetre

Le depot canonique de travail est `jonathanduchesne-lab/TDG`.
- Dynamique post-initiale : `S_n = (K_n, Q_n, P_n, L_n)` et `S_(n+1)=U_e(S_n)` pour un evenement factuel legal `e`.
- Q predictif global non effondre et ledger des faits separe, append-only.
- Selection de l'evenement `Sigma` distincte du pont structurel `U_e`.
- Born NON DERIVE; MRP9B en attente de reconstruction/provenance du chart Q-B1592.
- Test structurel additionnel : B5 v0.3, `L=6I-J`, spectre `(0,6,6,6,6,6)`.
- B5 v0.4 : l'extension scalaire ne ferme pas HDA et ne supprime pas le canal de courbure frame/SU2 de rang 3.

## Lentille importee de la science connue

1. Dynamique ouverte GKSL/Lindblad (decoherence):
   `d(rho)/dt = -i[H,rho]/hbar + sum_k gamma_k(L_k rho L_k^dag - 1/2 {L_k^dag L_k,rho})`.
2. Mesure/instrument quantique: `p_e = Tr(M_e rho M_e^dag)` et conditionnement sur `e`.
3. Decoherence microscopique : interaction unitaire systeme+environnement et perte de visibilite reduite.
4. Darwinisme quantique : information accessible a des fragments de l'environnement, via une quantite d'information Holevo.
5. Recoherence : inversion de toutes les interactions dans un modele fini ideal, sans supposer un effondrement physique nouveau.

**La lentille ne pose ni effondrement ontologique ni present universel comme axiome.** La production objective de traces durables est le phenomene empirique; une selection unique fondamentale reste une question ouverte d'interpretation.

## Test A : deux chemins et fragments d'environnement

Etat initial `(ket(0)+ket(1))/sqrt(2)` ; chaque fragment est couple au chemin de maniere telle que le recouvrement des deux etats environnementaux vaut `cos(theta)`, avec `theta=0.7 rad` comme **parametre de laboratoire arbitraire**, et non valeur mesuree de TDG.

Alors: `V_N = cos(theta)^N`; `chi_m = H_2((1+cos(theta)^m)/2)` borne de Holevo (chi, upper bound) pour m fragments. L'information effectivement accessible par la mesure binaire optimale est `Iacc_m = 1-H_2((1-sqrt(1-cos(theta)^(2m)))/2)`. La redondance R ci-dessous emploie Iacc, et non la borne de Holevo.

| Fragments N | Visibilite locale V | Borne Holevo (bits) | Info accessible (bits) | Fragments disjoints >= 0.9 bit |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1.00000000 | 0.00000000 | 0.00000000 | 0 |
| 1 | 0.76484219 | 0.52236123 | 0.32455812 | 0 |
| 2 | 0.58498357 | 0.73669271 | 0.54875910 | 0 |
| 4 | 0.34220578 | 0.91379559 | 0.80466879 | 0 |
| 8 | 0.11710480 | 0.99008504 | 0.96689308 | 1 |
| 16 | 0.01371353 | 0.99986434 | 0.99925623 | 2 |
| 32 | 0.00018806 | 0.99999997 | 0.99999975 | 5 |

Resultat : **l'information se stabilise de maniere redondante et la visibilite reduite s'efface progressivement, sans seuil d'actualisation obligatoire.**

Sur N=16, annuler les 16 interactions restaure exactement `V=1`. N'en annuler que 8 laisse `V=0.117104795`. Le modele est reversible globalement mais peut etre irreversiblement *pratique* si l'environnement echappe au controle.

## Test B : deux enregistreurs distants, correlations

Sur un etat de Bell `(|00>+|11>)/sqrt(2)`, deux instruments de mesure locaux projectifs sont appliques dans les ordres A->B et B->A.

- Distribution jointe : `P(00)=1/2`, `P(11)=1/2`, `P(01)=P(10)=0`.
- Defaut d'ordre : `0.0` a la precision du calcul.
- Defaut de signalisation locale B apres mesure A non lue : `0.0`.

**La correlation et l'histoire des faits n'imposent pas l'ordre de selection des mesures spatialement separees.** Ce test n'interdit pas un present cache; il montre qu'il n'est pas derive de cette lentille.

## Test C : projection sur le registre B5 certifie

Structure officielle du modele TDG B5 v0.3 : `L=6I-J`, projecteurs `P1=J/6` et `P5=I-P1`. Le singlet constant est une redondance; la partie physique non constante est Standard5.

Une dephasing projective naivement faite sur les **six etiquettes** donne une population du singlet non physique de `1/6 = 16.6667 %` pour l'etat de test. C'est un mauvais raccordement d'une lentille deja connue a un quotient TDG.

Nous avons teste un instrument compatible avec le quotient :

`M_j = sqrt(6/5) P5 |j><j| P5`, `j=1..6`.

Il satisfait `sum_j M_j^dag M_j=P5` et agit uniquement sur Standard5.

| Controle | Resultat |
| --- | ---: |
| Spectre de L | `(0,6,6,6,6,6)` |
| Fuite singlet, mesure naive | `0.1666666667` |
| Fuite singlet, instrument projete | `3.25e-17` |
| Defaut completude instrument | `9.72e-16` |
| Defaut covariance sur 720 permutations | `3.52e-16` |
| Defaut du secteur TT spectateur | `1.11e-16` |
| Action pure trace B5 sur 5 directions STF | `3.30e-17` |

**Limite capitale : B5 est un registre de relations/representations, pas un sous-systeme quantique microscopique dont le Hilbert et le couplage avec un detecteur sont derives. Ce test est un test de typage et de symetrie, PAS une derivation du canal physique a partir de Q.**

## Ce que change la lentille pour TDG

Le raccord mathematiquement leger est :

`rho_predictive_accessible --[instrument physique M_e]--> {p_e, trace environnementale}`

puis, *conditionnellement au fait e retenu* :

`(K_n,Q_n,P_n,L_n) --[U_e]--> (Ext_e K_n, Q_(n+1), Phi_e P_n, L_n concat e)`.

On n'ecrase pas le Q global en une branche par decret. La statistique de Born est **utilisee** par l'instrument quantique connu, mais **non derivee** de TDG.

## Verdict

**PASS (diagnostic):** la lentille scientifique est compatible avec l'interface selection/structure de TDG; la decoherence et les traces produisent une factualite operationnelle sans effondrement supplementaire; le registre B5 peut accueillir un test de mesure compatible avec le quotient Standard5 sans creer le singlet non physique.

**NON PROUVE:** derivation fondamentale de la selection unique, de la Born rule depuis TDG, d'un present universel, du canal actif->dark beta non nul et de l'architecture HDA/GR. La lentille, sans couplage physique microscopique supplementaire, ne repare pas les no-go certifies du programme B5 ou l'obstruction STF->gradient.

**PROVENANCE BLOQUANTE:** la reconstruction numerique exacte du chart Q-B1592 necessaire au front actif MRP9B n'est pas documentee comme recertifiee dans le depot. Il serait incorrect de presenter ce laboratoire comme une execution du Q global MRP9B complet.

## Reproduction

Script : `tdg_lentille_decoherence_2026_11_06.py` (numpy 2.3.5).  
Resultats numeriques : `tdg_lentille_decoherence_resultats.json`.  
Executer : `python tdg_lentille_decoherence_2026_11_06.py`.

## References

- TDG: `https://github.com/jonathanduchesne-lab/TDG/blob/main/CURRENT_FRONT_LATEST.md`.
- TDG B5 v0.3: `https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-10-06/TDG_B5_EXTENSION_V0_3_OVERLAP_HIGHERCONS_PASS_2026-10-06.md`.
- TDG B5 v0.4: `https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-10-06/TDG_B5_EXTENSION_V0_4_COMB_HDA_INSUFFICIENT_FRAME_CURVATURE_WALL_2026-10-06.md`.
- TDG MRP9A: `https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-10-14/TDG_MRP9A_SAME_FACE_LINK_PROVENANCE_GAP_2026-10-14.md`.
- Schlosshauer, Reviews of Modern Physics (2005): `https://doi.org/10.1103/RevModPhys.76.1267`.
- Schlosshauer, Physics Reports (2019): `https://doi.org/10.1016/j.physrep.2019.10.001`.
- Zurek, Quantum Darwinism, Nature Physics (2009): `https://doi.org/10.1038/nphys1202`.
- Englert/Bergou, Quantitative Quantum Erasure (2000): `https://doi.org/10.1016/S0030-4018(99)00718-X`.

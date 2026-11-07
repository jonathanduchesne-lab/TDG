# TDG LAB — octupôle Q, mémoire fraîche et horizon (6 novembre 2026)

**NON CANONIQUE.** Branche expérimentale post-`mrp9b_formal_paths`. Aucun passage à GR/HDA dérivé de Q.

## Lire

- `REPORT.md` : hypothèses, dérivations, résultats, échecs, décisions scientifiques.
- `verify_fresh_chiral_octupole.py` + `results.json` : extraction véritable Q-B1852 / ray J, canal CPTP binaire, biais et compatibilité avec l'enregistrement B2.
- `verify_fullQ_octahedral_refresh.py` + `fullQ_24_results.json` : contrôle **sans projection** de la matrice Q A21, toutes les 24 orientations, histoire fraîche contre histoire statique.
- `verify_tt_uniform_and_limits.py` + `adversarial_results.json` : 40 directions TT et contre-exemple à horizon fixe `dt`.
- `verify_adaptive_horizon.py` + `adaptive_results.json` : borne de trace à horizon arbitraire lorsque `δ_n=a/n^p` et `1/2<p<=1`.
- `verify_selected_trajectories.py` + `selected_results.json` : 1 600 histoires factuelles conditionnelles par réglage (Monte Carlo).
- `*_execution.log` : sorties brutes des cinq programmes.
- `SHA256SUMS.txt` : empreintes de tous les éléments avant archive.

## Reproduire

```sh
export TDG_Q1852_SOURCE=/path/to/qb1852_full_refined.py
sh run_all.sh
sha256sum -c SHA256SUMS.txt
```

Vérifier que `TDG_Q1852_SOURCE` correspond à `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7` et que ses dépendances `deps` sont présentes.

**Ne pas promouvoir cette expérience sans dériver depuis le Q réel une loi de réorientation PHYSIQUE, les poids de sélection, l'échelle des durées, les contraintes TT et HDA.** Une rotation passive de coordonnées ne répare rien.

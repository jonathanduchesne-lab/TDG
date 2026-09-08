# Complete TDG / Root 2.0 — Strategy C

Sauvegarde de recherche A→Z du **6 septembre 2026** : **P10O CLOSED LOCALLY / P10P NOT STARTED**.

Ce dépôt conserve le handoff P10O et sert désormais aussi de mémoire documentaire versionnée du programme TDG. Les documents historiques sont archivés sans être automatiquement promus au canon scientifique courant.

## Commencer ici

| Besoin | Document |
| --- | --- |
| Connaître le front scientifique actuel | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Comprendre le projet P10O | [Guide « grand-mère »](docs/01_GRANDMOTHER_GUIDE_TDG_A_TO_Z_P10O_2026-09-06.md) |
| Reconstituer l'historique A→Z | [Recovery complet](docs/Complete_TDG_ROOT2_A_TO_Z_GRANDMOTHER_WORK_RECOVERY_P10O_CLOSED_P10P_NOT_STARTED_2026-09-06.md) |
| Connaître l'état canonique P10O | [État canonique P10O](docs/02_TDG_CURRENT_CANONICAL_STATE_P10O_2026-09-06.md) |
| Examiner P10O | [Audit P10O](docs/03_TDG_P10O_AUDIT_v1_0_2026-09-06.md) et [delta P10N→P10O](docs/04_TDG_A2Z_DELTA_P10N_TO_P10O_2026-09-06.md) |
| Reprendre dans une conversation | [Prompt exact](docs/06_EXACT_WORK_RESUME_PROMPT.txt) |
| Retrouver une étape historique | [Chronologie](indexes/CHECKPOINT_TIMELINE_INDEX.txt) et [index des titres](indexes/FULL_RECOVERY_HEADING_INDEX.tsv) |
| Examiner le patrimoine TDG antérieur | [history/README.md](history/README.md) et [statut des add-ons](history/ADDONS_STATUS.md) |
| Examiner les sources historiques retrouvées | [Inventaire Library → GitHub](provenance/HISTORICAL_LIBRARY_INVENTORY_2026-09-08.md) |
| Examiner la provenance P10O et les limites | [Reproduction](docs/05_REPRODUCTION_AND_PROVENANCE.md) et [lacunes connues](docs/07_KNOWN_GAPS_AND_DO_NOT_FABRICATE.md) |

## Statut scientifique courant

Le front actif est maintenant piloté par `CURRENT_STATE.md`. Le point défendable reste :

- noyau **retained-memory / effective-history** fort conservé;
- forte cohérence relativiste linéaire et premier non-linéaire dans les scopes gelés;
- **full nonlinear GR from TDG : NOT ESTABLISHED**.

La Sentinelle ne doit signaler que des prémisses microscopiques réellement nouvelles, des no-go décisifs ou de vrais jalons de fermeture non linéaire. Un scan négatif ou répétitif ne justifie ni notification scientifique ni commit.

## État scientifique P10O préservé

- Autorité historique **FINAL-CERTIFIED : Q-B1858L**, inchangée.
- P10O : fermeture locale sur le carrier scalaire Cons/Feshbach documenté ; **1812/1920 wedges non nuls**, **16/16 mouvements séparés**, vérificateur **29/29 PASS**.
- La pertinence physique de ce défaut D4 à l'IR reste ouverte dans le scope P10O/P10P.
- Root1/UAP conservé ; `A_path` retiré ; Q global non effondré ; ledger factuel append-only, séparé de Q.
- Born et durée métrique/propre : **NOT DERIVED** ; QSC candidat nonbinding ; O(3) : **FAIL / NOT CLOSED** ; Lambda : **OPEN**.
- Les statuts historiques HDA/spin-2/GR restent limités à leurs scopes documentés.

Les PASS du vérificateur sont des contrôles de certificat et de reproductibilité, pas des confirmations physiques indépendantes.

## Patrimoine historique

Le vieux TDG n'est pas jeté. Les anciens manuscrits, add-ons, stress tests, branches de reconstruction et anciens bridges sont conservés comme banque de données et de provenance. Leur règle est :

**ARCHIVÉ ≠ CANONIQUE ≠ DÉRIVÉ ≠ VALIDÉ PHYSIQUEMENT.**

Ils peuvent redevenir utiles comme couche IR/downstream, comparator ou source d'intuition seulement si le front courant les re-dérive ou montre explicitement qu'ils défont un no-go antérieur.

## Vérifier et reproduire P10O

Prérequis : **Python 3.12 ou ultérieur**. Depuis la racine du dépôt :

```sh
python3 tools/verify_handoff.py
```

Pour rejouer les deux scripts P10O archivés :

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-repro.txt
.venv/bin/python tools/verify_handoff.py --replay
```

Sous Windows, utiliser `.venv\Scripts\python.exe` à la place de `.venv/bin/python`.

## Organisation

- `CURRENT_STATE.md` : front scientifique courant et firewalls de Sentinelle.
- `docs/` : documentation canonique du handoff P10O.
- `history/` : patrimoine historique et statuts des anciens add-ons.
- `indexes/` : index historiques d'origine.
- `repro/` : archive P10O originale et éléments de reproduction.
- `provenance/` : provenance P10O et inventaires historiques.
- `tools/` : vérification d'intégrité et rejeu P10O.
- `verification/` : journaux historiques et rapports de vérification.

## Limites de complétude

Le handoff P10O ne prétend pas disposer des éléments déjà déclarés manquants : **Q-B506→555**, **Q-B759→878**, et certains raw repro **Q-B1831→1835**. Ces trous ne doivent jamais être reconstruits par interpolation.

L'inventaire patrimonial du 8 septembre confirme que plusieurs originaux historiques restent actuellement ancrés dans la Library ChatGPT et ne sont pas encore tous importés byte-identical dans GitHub. Leur présence dans l'inventaire ne doit donc pas être confondue avec une copie binaire déjà présente dans le dépôt.

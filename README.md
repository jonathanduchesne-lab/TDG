# Complete TDG / Root 2.0 — Strategy C

Sauvegarde de recherche A→Z du **6 septembre 2026** : **P10O CLOSED LOCALLY / P10P NOT STARTED**.

Ce dépôt rassemble le recovery autonome, le guide « grand-mère », les audits,
les index et le bundle de reproductibilité du handoff P10O. L'import conserve
les sources octet par octet. Il n'introduit aucun nouveau résultat scientifique.

## Commencer ici

| Besoin | Document |
| --- | --- |
| Comprendre le projet | [Guide « grand-mère »](docs/01_GRANDMOTHER_GUIDE_TDG_A_TO_Z_P10O_2026-09-06.md) |
| Reconstituer l'historique A→Z | [Recovery complet](docs/Complete_TDG_ROOT2_A_TO_Z_GRANDMOTHER_WORK_RECOVERY_P10O_CLOSED_P10P_NOT_STARTED_2026-09-06.md) |
| Connaître l'état courant | [État canonique P10O](docs/02_TDG_CURRENT_CANONICAL_STATE_P10O_2026-09-06.md) |
| Examiner le dernier résultat | [Audit P10O](docs/03_TDG_P10O_AUDIT_v1_0_2026-09-06.md) et [delta P10N→P10O](docs/04_TDG_A2Z_DELTA_P10N_TO_P10O_2026-09-06.md) |
| Reprendre dans une conversation | [Prompt exact](docs/06_EXACT_WORK_RESUME_PROMPT.txt) |
| Retrouver une étape historique | [Chronologie](indexes/CHECKPOINT_TIMELINE_INDEX.txt) et [index des titres](indexes/FULL_RECOVERY_HEADING_INDEX.tsv) |
| Examiner la provenance et les limites | [Reproduction](docs/05_REPRODUCTION_AND_PROVENANCE.md) et [lacunes connues](docs/07_KNOWN_GAPS_AND_DO_NOT_FABRICATE.md) |

Le recovery dépasse 6 Mo : son téléchargement peut être nécessaire pour le lire
entièrement. Ses anciens « next gate » appartiennent à l'historique ; le point
de reprise actuel est P10P.

## État scientifique préservé

- Autorité historique **FINAL-CERTIFIED : Q-B1858L**, inchangée.
- P10O : fermeture locale sur le carrier scalaire Cons/Feshbach documenté ;
  **1812/1920 wedges non nuls**, **16/16 mouvements séparés**, vérificateur **29/29 PASS**.
- La pertinence physique de ce défaut D4 à l'IR reste ouverte : c'est la cible P10P.
- Root1/UAP conservé ; `A_path` retiré ; Q global non effondré ; ledger factuel
  append-only, séparé de Q. L'actualisation soustractive est attribuée à Jonathan Duchesne.
- Born et durée métrique/propre : **NOT DERIVED** ; QSC candidat nonbinding ;
  O(3) : **FAIL / NOT CLOSED** ; Lambda : **OPEN**.
- Les statuts historiques HDA/spin-2/GR restent limités à leurs scopes documentés.

Les PASS du vérificateur sont des contrôles de certificat et de reproductibilité.
Ils ne constituent pas autant de confirmations physiques indépendantes.

## Vérifier et reproduire

Prérequis : **Python 3.12 ou ultérieur**. Le contrôle d'intégrité utilise seulement
la bibliothèque standard. Depuis la racine du dépôt :

```sh
python3 tools/verify_handoff.py
```

Pour rejouer les deux scripts P10O archivés dans un répertoire temporaire :

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-repro.txt
.venv/bin/python tools/verify_handoff.py --replay
```

Sous Windows, utiliser `.venv\Scripts\python.exe` à la place de `.venv/bin/python`.
L'environnement vérifié lors de l'import était Python 3.12.13 / NumPy 2.3.5.

Le vérificateur contrôle les 18 entrées du manifeste Work, les 11 entrées du
manifeste P10O, les 25 entrées du manifeste interne P10O, la copie verbatim du
recovery source et la correspondance des cinq pièces jointes. Avec `--replay`,
il exige aussi **29/29 PASS** et compare les deux JSON régénérés **octet par octet**
aux résultats archivés. Aucun calcul P10P n'est exécuté.

Le [rapport de vérification de cet import](verification/REPOSITORY_IMPORT_CHECK_2026-09-06.json)
consigne le rejeu effectivement effectué. Les autres journaux de `verification/`
sont les journaux historiques importés.

Pour contrôler tous les fichiers de ce commit, outils et documentation d'accueil
compris, avec GNU coreutils :

```sh
sha256sum -c SHA256SUMS
```

## Organisation et déduplication

- `docs/` : documentation canonique et un seul exemplaire du MASTER, en Markdown.
- `indexes/` : index historiques d'origine.
- `repro/` : archive P10O originale, avec ses scripts, résultats, entrées P10M,
  documents parents et bundle P10M imbriqué ; manifeste original associé.
- `provenance/` : origine de l'import, empreintes et correspondance des fichiers.
- `tools/` : vérification d'intégrité et rejeu P10O sans modifier les sources.
- `verification/` : journaux historiques et rapport du présent import.

Les suffixes de téléchargement `-1`, `-2`, `-3` sont absents des noms canoniques.
La copie `.txt` du MASTER était strictement identique au `.md` ; elle est omise.
Le [manifeste Work d'origine](TDG_WORK_A2Z_MANIFEST_SHA256_2026-09-06.txt) reste
inchangé pour la provenance. Il référence donc encore cet alias `.txt` :
`tools/verify_handoff.py` le vérifie explicitement contre le `.md` conservé.
Pour un contrôle direct par `sha256sum`, utiliser le manifeste du dépôt `SHA256SUMS`.

L'archive scientifique P10O est conservée telle quelle, y compris ses redondances
historiques internes, afin de préserver son empreinte. L'archive de transport
externe n'est pas ajoutée une seconde fois ; son empreinte est enregistrée dans
[la provenance d'import](provenance/IMPORT_2026-09-06.json).

## Limites de complétude

Ce dépôt est exhaustif par rapport au handoff P10O retrouvé et aux cinq documents
fournis. Il ne prétend pas disposer des éléments déjà déclarés manquants :
**Q-B506→555**, **Q-B759→878**, et certains raw repro **Q-B1831→1835**.
Le rejeu vérifié porte sur P10O à partir des entrées P10M archivées ; il ne
régénère pas toutes les étapes historiques ni les enclosures P10M depuis zéro.

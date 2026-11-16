# Pistes d'amélioration — Régression logistique multinomiale

## C'est quoi
Article de synthèse sur la régression logistique multinomiale (LaTeX) + application
sur les données SEER + travaux pratiques R.

## État actuel
- Article LaTeX : `article_rlm.tex`, `article_rlm_complete.tex`, `beamer_application_rlm.tex`.
- Rapport R Markdown : `SEER_Regression_Multinomiale_FINAL.Rmd` (+ variante `code_EPURE`).
- Données : `10.21037atm-2020-57-1*.xlsx` / `.pdf`.
- Plusieurs copies du même fichier (`copy`, `(3)`, `(1)`, `- Copy`).

## Pistes (courtes)
- Supprimer les doublons de données et de rapports (garder une seule version de chaque).
- Compiler l'article en un seul PDF final et le nommer clairement (`article_rlm.pdf`).
- Remplacer `\author{Votre nom}` par le vrai nom dans le `.tex`.
- Ajouter un `README.md` : objectif, données, comment compiler, résultats.
- Déplacer les scripts `_inspect_*.py` / `_extract_*.py` dans un dossier `outils/`.
- Ajouter un `requirements.txt` (R : `FactoMineR`, `nnet`, `readxl`...).

## Mini-prompt
> Nettoie les doublons, compile `article_rlm_complete.tex` en `article_rlm.pdf`,
> corrige l'auteur, et écris un README (objectif, données, compilation, résultats).

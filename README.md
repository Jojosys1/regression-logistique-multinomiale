# Régression logistique multinomiale — application aux données SEER

Synthèse théorique de la **régression logistique multinomiale (RLM)** et application
à des données cliniques (base **SEER**) pour classifier la cause de décès de patients
atteints de cancer. Travail réalisé à l'ENSGMM.

**Auteurs :** DOSSOU YOVO Thérèse & GLODJO Jolémon.

## Contenu

| Dossier / fichier | Rôle |
|---|---|
| `article_rlm_complete.tex` | Article complet (théorie + application) — version principale |
| `article_rlm.tex` | Article court |
| `beamer_application_rlm.tex` | Support de présentation (beamer) |
| `SEER_Regression_Multinomiale_FINAL.Rmd` | Notebook d'analyse complet (données SEER) |
| `SEER_Regression_Multinomiale_code_EPURE.Rmd` | Version épurée du code |
| `TP_regression_logistique_multinomiale_*.Rmd` | Travaux pratiques |
| `images/` | Figures utilisées dans l'article et le rapport |
| `outils/` | Scripts Python d'inspection / extraction (annexe) |
| `*.pdf`, `*.xlsx` | Articles de référence et base de données |

## Méthode

Le notebook suit un plan en 6 étapes : présentation des données, analyse exploratoire,
vérification des conditions d'application, modélisation (`nnet::multinom`, `VGAM`),
tests de significativité/validation, puis interprétation (odds-ratios, matrice de confusion).

## Prérequis

- **R** (≥ 4.2) et **RStudio** pour les `.Rmd`.
- Packages R : `readxl`, `nnet`, `VGAM`, `dplyr`, `tidyr`, `ggplot2`, `ggpubr`, `scales`,
  `knitr`, `kableExtra`, `car`, `pROC`, `caret`, `reshape2`, `forcats`, `RColorBrewer`.
- **LaTeX** (MiKTeX/TeX Live) pour compiler les `.tex`.

```r
install.packages(c("readxl","nnet","VGAM","dplyr","tidyr","ggplot2","ggpubr",
  "scales","knitr","kableExtra","car","pROC","caret","reshape2","forcats","RColorBrewer"))
```

## Utilisation

1. Ouvrir `SEER_Regression_Multinomiale_FINAL.Rmd` et **Knit**.
2. Compiler l'article : `pdflatex article_rlm_complete.tex` (deux passes pour la table des matières).
3. Compiler le beamer : `pdflatex beamer_application_rlm.tex`.

## Résultats

Figures clés dans `images/` : ajustement du modèle, odds-ratios (`OR1.png`), courbes de
survie par catégorie, matrice de confusion, tests de Wald.

## Licence

Travail académique. Voir `LICENSE` si présent.

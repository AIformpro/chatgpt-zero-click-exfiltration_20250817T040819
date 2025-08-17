
# 🚨 ChatGPT Zero-Click Exfiltration (POC)

## ⚠️ Alerte
Nouvelle surface d’attaque : **exfiltration furtive de données via IA connectée, déclenchée par la simple lecture d’un document piégé**.

- Aucune action requise.
- Aucun clic nécessaire.
- **Juste la lecture suffit.**

## 🔍 Contexte
Avec la multiplication des connecteurs (#Drive, CRM, SaaS) et des agents IA à mémoire, implanter un agent malveillant devient trivial.  
Une seule intégration vulnérable → l’ensemble du SI peut être compromis.

## 🧩 Risques
- Exfiltration de données critiques.
- Persistance de l’agent malveillant dans la mémoire IA.
- Escalade via connecteurs (Drive, Mail, Slack, Teams).

## ✅ Recommandations
- Stopper l’intégration aveugle d’agents IA.
- Auditer chaque connecteur avant mise en production.
- Vérifier en continu les comportements et logs IA.

## 🛡️ Objectif du dépôt
- Centraliser les POC et scripts de simulation.
- Fournir une grille d’audit IA↔connecteurs.
- Démontrer l’attaque par un **Zero-Click Exfiltration Demo**.

## 📦 Structure
```
poc/
  exfil_demo.py
  poisoned_doc.txt
audit/
  checklist.md
  connector_risks.md
docs/
  threat_model.md
  mitigations.md
```

## 📜 Licence
MIT – Usage éducatif et sensibilisation uniquement.

# 📊 Mercado Laboral TI — Analista de Datos Chile 2026

> Análisis exploratorio de 89 ofertas laborales del área de datos en Chile, recopiladas desde LinkedIn Jobs y Trabajando.cl durante mayo–junio 2026.

**Autor:** Emilio Rubina Salinas  
**LinkedIn:** [linkedin.com/in/emilio-rubina-salinas-b1436a253](https://www.linkedin.com/in/emilio-rubina-salinas-b1436a253/)

---

## 🎯 Objetivo

Identificar patrones del mercado laboral para roles de analista de datos en Chile:
- Skills técnicos más demandados
- Distribución de seniority y modalidad de trabajo
- Sectores e industrias con mayor demanda
- Herramientas BI prevalentes (Power BI vs Tableau vs Looker)
- Calidad metodológica de las plataformas de empleo

---

## 📁 Estructura del proyecto

```
├── ofertas_ti_chile_clean.csv        # Dataset limpio (89 ofertas, 25 columnas)
├── analisis_mercado_datos_chile.ipynb # Notebook de análisis y visualizaciones
├── outputs/
│   ├── 01_calidad_datos.png
│   ├── 02_skills_demandados.png
│   ├── 03_seniority_modalidad.png
│   ├── 04_industrias.png
│   ├── 05_herramientas_bi.png
│   └── 06_heatmap_skills_rol.png
└── README.md
```

---

## 🔍 Metodología

1. **Recopilación manual** de ofertas en LinkedIn Jobs y Trabajando.cl bajo keywords: "analista de datos", "data analyst", "analista BI", "data scientist"
2. **Estructuración** en Excel con 12 columnas: cargo, empresa, industria, región, modalidad, seniority, salario, skills, experiencia mínima, fuente y notas
3. **Limpieza con Python (pandas):**
   - Detección y marcado de duplicados
   - Normalización de campos categóricos
   - Extracción de 18 skills como columnas booleanas
   - Clasificación de tipo de rol
4. **Análisis exploratorio** con matplotlib

---

## 📈 Principales hallazgos

| Insight | Dato |
|---|---|
| Skill más demandado | **SQL** (~75% de las ofertas) |
| Herramienta BI líder | **Power BI** (~60% de las ofertas) |
| Modalidad dominante | **Híbrido** (~52%) |
| Seniority más común | **Junior** (27%) |
| Ofertas con salario explícito | Solo **~3%** |
| Duplicados detectados | **~6%** del total |
| IA generativa como requisito | **Tendencia emergente** (2+ ofertas) |

---

## 🛠️ Stack técnico utilizado

- **Python:** pandas, matplotlib, numpy
- **Jupyter Notebook**
- **Excel / Power BI** (para dashboard complementario)

---

## 🚀 Cómo ejecutar

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/mercado-datos-chile-2026.git
cd mercado-datos-chile-2026

# Instalar dependencias
pip install pandas matplotlib numpy jupyter openpyxl

# Ejecutar notebook
jupyter notebook analisis_mercado_datos_chile.ipynb
```

---

## 📊 Dashboard Power BI

El dashboard interactivo complementario está disponible en:  
🔗 *(link Power BI Service — próximamente)*

---

*Datos recopilados con fines académicos y de portafolio profesional.*

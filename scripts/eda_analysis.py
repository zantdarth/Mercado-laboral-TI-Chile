import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Cargar datos
df = pd.read_csv('data/ofertas_ti_chile_limpio.csv')

print("=" * 60)
print("GENERANDO GRÁFICOS EDA")
print("=" * 60)

# 1. SENIORITY
print("\n[1/10] Generando: Distribución de Seniority...")
fig, ax = plt.subplots(figsize=(10, 5))
seniority_counts = df['Seniority'].value_counts(dropna=False)
seniority_counts.plot(kind='bar', color='steelblue', ax=ax)
ax.set_title('Distribución de Ofertas por Seniority', fontsize=14, fontweight='bold')
ax.set_xlabel('Seniority')
ax.set_ylabel('Cantidad de Ofertas')
ax.grid(axis='y', alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/01_seniority_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/01_seniority_distribution.png")

# 2. MODALIDAD
print("[2/10] Generando: Distribución de Modalidad...")
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#95a5a6']
modalidad_counts = df['Modalidad'].value_counts(dropna=False)
modalidad_counts.plot(kind='pie', autopct='%1.1f%%', colors=colors[:len(modalidad_counts)], ax=ax)
ax.set_title('Distribución de Ofertas por Modalidad', fontsize=14, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('plots/02_modalidad_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/02_modalidad_distribution.png")

# 3. SALARIOS
print("[3/10] Generando: Distribución de Salarios...")
fig, ax = plt.subplots(figsize=(12, 5))
salarios = df[df['Salario'].notna()]['Salario']
ax.hist(salarios, bins=15, color='steelblue', edgecolor='black', alpha=0.7)
ax.axvline(salarios.mean(), color='red', linestyle='--', linewidth=2, label=f'Promedio: ${salarios.mean():,.0f}')
ax.axvline(salarios.median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: ${salarios.median():,.0f}')
ax.set_title('Distribución de Salarios', fontsize=14, fontweight='bold')
ax.set_xlabel('Salario (CLP)')
ax.set_ylabel('Cantidad de Ofertas')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/03_salary_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/03_salary_distribution.png")

# 4. SALARIOS POR SENIORITY
print("[4/10] Generando: Salarios por Seniority...")
fig, ax = plt.subplots(figsize=(12, 5))
seniority_order = ['Junior', 'Mid', 'Senior']
df_sal = df[df['Salario'].notna()]
df_sal_filtered = df_sal[df_sal['Seniority'].isin(seniority_order)]
sns.boxplot(data=df_sal_filtered, x='Seniority', y='Salario', order=seniority_order, ax=ax, palette='Set2')
ax.set_title('Distribución de Salarios por Seniority', fontsize=14, fontweight='bold')
ax.set_xlabel('Seniority')
ax.set_ylabel('Salario (CLP)')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/04_salary_by_seniority.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/04_salary_by_seniority.png")

# 5. EXPERIENCIA
print("[5/10] Generando: Experiencia Mínima Requerida...")
fig, ax = plt.subplots(figsize=(12, 5))
exp = df[df['Exp. mínima'].notna()]['Exp. mínima']
exp_counts = exp.value_counts().sort_index()
exp_counts.plot(kind='bar', color='coral', ax=ax)
ax.set_title('Experiencia Mínima Requerida', fontsize=14, fontweight='bold')
ax.set_xlabel('Años de Experiencia')
ax.set_ylabel('Cantidad de Ofertas')
ax.grid(axis='y', alpha=0.3)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('plots/05_experience_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/05_experience_distribution.png")

# 6. TOP EMPRESAS
print("[6/10] Generando: Top 10 Empresas...")
fig, ax = plt.subplots(figsize=(12, 6))
top_empresas = df['Empresa'].value_counts().head(10)
top_empresas.plot(kind='barh', color='mediumpurple', ax=ax)
ax.set_title('Top 10 Empresas con Más Ofertas', fontsize=14, fontweight='bold')
ax.set_xlabel('Cantidad de Ofertas')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/06_top_companies.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/06_top_companies.png")

# 7. TOP CARGOS
print("[7/10] Generando: Top 10 Cargos...")
fig, ax = plt.subplots(figsize=(12, 6))
top_cargos = df['Cargo'].value_counts().head(10)
top_cargos.plot(kind='barh', color='lightseagreen', ax=ax)
ax.set_title('Top 10 Cargos Más Solicitados', fontsize=14, fontweight='bold')
ax.set_xlabel('Cantidad de Ofertas')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/07_top_positions.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/07_top_positions.png")

# 8. TOP REGIONES
print("[8/10] Generando: Top 10 Regiones...")
fig, ax = plt.subplots(figsize=(12, 6))
top_regiones = df['Región'].value_counts().head(10)
top_regiones.plot(kind='barh', color='skyblue', ax=ax)
ax.set_title('Top 10 Regiones con Más Ofertas', fontsize=14, fontweight='bold')
ax.set_xlabel('Cantidad de Ofertas')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/08_top_regions.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/08_top_regions.png")

# 9. TOP INDUSTRIAS
print("[9/10] Generando: Top 10 Industrias...")
fig, ax = plt.subplots(figsize=(12, 6))
top_industrias = df['Industria'].value_counts().head(10)
top_industrias.plot(kind='barh', color='lightcoral', ax=ax)
ax.set_title('Top 10 Industrias con Más Ofertas', fontsize=14, fontweight='bold')
ax.set_xlabel('Cantidad de Ofertas')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/09_top_industries.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/09_top_industries.png")

# 10. TOP SKILLS
print("[10/10] Generando: Top 20 Skills...")
all_skills = []
for skills in df['Skills requeridos'].dropna():
    parts = str(skills).replace(' y ', ',').replace(' / ', ',').replace(';', ',').split(',')
    for skill in parts:
        skill_clean = skill.strip().lower()
        if skill_clean and len(skill_clean) > 2:
            all_skills.append(skill_clean)

skills_counter = Counter(all_skills)
top_skills = dict(skills_counter.most_common(20))

fig, ax = plt.subplots(figsize=(12, 8))
skills_df = pd.DataFrame(list(top_skills.items()), columns=['Skill', 'Frecuencia']).sort_values('Frecuencia')
skills_df.plot(x='Skill', y='Frecuencia', kind='barh', ax=ax, color='gold', legend=False)
ax.set_title('Top 20 Skills Más Solicitados', fontsize=14, fontweight='bold')
ax.set_xlabel('Frecuencia')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/10_top_skills.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: plots/10_top_skills.png")

# RESUMEN
print("\n" + "=" * 60)
print("RESUMEN EJECUTIVO")
print("=" * 60)
print(f"\n📊 DATASET")
print(f"  • Total de ofertas: {df.shape[0]}")
print(f"  • Empresas: {df['Empresa'].nunique()}")
print(f"  • Cargos diferentes: {df['Cargo'].nunique()}")
print(f"  • Regiones: {df['Región'].nunique()}")
print(f"  • Industrias: {df['Industria'].nunique()}")

print(f"\n💼 SENIORITY MÁS DEMANDADO")
top_seniority = df['Seniority'].value_counts()
if len(top_seniority) > 0:
    print(f"  • {top_seniority.index[0]}: {top_seniority.iloc[0]} ofertas ({top_seniority.iloc[0]/len(df)*100:.1f}%)")

print(f"\n📍 MODALIDAD MÁS COMÚN")
top_modalidad = df['Modalidad'].value_counts()
if len(top_modalidad) > 0:
    print(f"  • {top_modalidad.index[0]}: {top_modalidad.iloc[0]} ofertas ({top_modalidad.iloc[0]/len(df)*100:.1f}%)")

print(f"\n💰 SALARIOS")
sal_ok = df[df['Salario'].notna()]
if len(sal_ok) > 0:
    print(f"  • Promedio: ${sal_ok['Salario'].mean():,.0f}")
    print(f"  • Rango: ${sal_ok['Salario'].min():,.0f} - ${sal_ok['Salario'].max():,.0f}")
    print(f"  • Datos disponibles: {len(sal_ok)}/{len(df)} ({len(sal_ok)/len(df)*100:.1f}%)")

print(f"\n📚 EXPERIENCIA")
exp_ok = df[df['Exp. mínima'].notna()]
if len(exp_ok) > 0:
    print(f"  • Promedio requerido: {exp_ok['Exp. mínima'].mean():.1f} años")
    print(f"  • Rango: {int(exp_ok['Exp. mínima'].min())} - {int(exp_ok['Exp. mínima'].max())} años")

print(f"\n🏆 TOP 3 EMPRESAS")
for i, (empresa, count) in enumerate(df['Empresa'].value_counts().head(3).items(), 1):
    print(f"  {i}. {empresa}: {count} ofertas")

print(f"\n🎯 TOP 3 CARGOS")
for i, (cargo, count) in enumerate(df['Cargo'].value_counts().head(3).items(), 1):
    print(f"  {i}. {cargo}: {count} ofertas")

print("\n" + "=" * 60)
print("✓ ANÁLISIS COMPLETADO - 10 gráficos guardados en /plots")
print("=" * 60)

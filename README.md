# Algoritmo k/D: Optimización y Trascendencia del Sistema Radial

![Licencia](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![Campo](https://img.shields.io/badge/Campo-Ingeniería_Estructural-orange.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18445774.svg)](https://doi.org/10.5281/zenodo.18445774)

**Referencia oficial:** [https://doi.org/10.5281/zenodo.18445774](https://doi.org/10.5281/zenodo.18445774)


## 📌 Introducción
Este repositorio documenta el desarrollo y la implementación del **Método k/D**, un algoritmo predictivo diseñado para transformar ángulos sexagesimales a radianes mediante la identificación de familias geométricas, eliminando la dependencia del cálculo reactivo por Máximo Común Divisor (MCD).

## 🚀 El Laboratorio Tutor (Software)
En la carpeta `/Calculadora_Tutor_KD` encontrarás una aplicación interactiva desarrollada en Python que desglosa el proceso en 4 fases críticas:

1. **Análisis Geométrico:** Determinación del ángulo de referencia ($\alpha$) y cuadrante.
2. **Obtención de Variables:** Cálculo de la familia $D$ ($180/\alpha$) y el predictor $k$.
3. **Procedimiento k/D:** Construcción de la estructura radial predictiva.
4. **Normalización de Base 10:** Conversión de estructuras decimales a fracciones canónicas para asegurar precisión absoluta.

### Ejemplo de Normalización k/D
Para un ángulo de $850^\circ$, el algoritmo detecta la familia $D = 3.6$. 
* **Estructura k/D:** $(17 / 3.6)\pi$
* **Normalización:** $(170 / 36)\pi \rightarrow \mathbf{85/18 \pi}$
* **Resultado:** Convergencia total con el método tradicional pero con mayor trasfondo geométrico.

## 📊 Comparativa Técnica
| Característica | Método Tradicional (MCD) | Algoritmo k/D |
| :--- | :--- | :--- |
| **Enfoque** | Aritmético (Reactivo) | Geométrico (Predictivo) |
| **Carga Cognitiva** | Alta (Simplificación manual) | Baja (Identificación de estados) |
| **Eficiencia** | Variable según magnitud | Constante (< 3 segundos) |
| **Aplicación** | General | Ingeniería y Ciencia de Materiales |

## 📂 Contenido del Repositorio
* `Documentacion_Final/`: Contiene la **Memoria Técnica Integrada**, el documento formal que sustenta la investigación.
* `Documentos_Sustento/`: Archivos originales que muestran la evolución del método desde 2025.
* `Laboratirio_Metodo_KD/`: Suite educativa para experimentar con el algoritmo.

## 📦 Descargas (Releases)
¿No tienes Python? No hay problema. Puedes descargar la versión ejecutable para tu sistema operativo:
* 📥 [Descargar para Windows] https://github.com/BrianRodriguezQ/Algoritmo_Estructural_Optimizado_KD/releases/download/v1.0.1/Calculadora_Metodo_KD_Windows.exe
* 📥 [Descargar para Linux] https://github.com/BrianRodriguezQ/Algoritmo_Estructural_Optimizado_KD/releases/download/v1.0.0/Calculadora_KD_Linux

---
**Autor:** Ing. Brian A. Rodriguez Q.  
**Investigación 2026** - *Optimizando la ingeniería a través del pensamiento computacional.*

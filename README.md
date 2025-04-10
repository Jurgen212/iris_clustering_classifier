# 🌸 Clasificador de Flores Iris con Flask + AdaBoost + Docker

Este proyecto es una aplicación web desarrollada con **Flask** que permite predecir la especie de una flor del dataset **Iris** a partir de medidas morfológicas. El modelo ha sido entrenado utilizando **AdaBoost** con `scikit-learn` y guardado como un archivo `.pkl` para su posterior inferencia desde la web.

## 📚 Dataset utilizado

Se utilizó el clásico dataset **Iris** de la UCI Machine Learning Repository, que contiene tres especies de flores:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Cada flor está descrita por 4 características numéricas.

## 📦 Características del proyecto

- Clasificación en tiempo real con un modelo entrenado con AdaBoost
- Interfaz web sencilla, elegante y en español (usando Bootstrap)
- Inputs con validación y valores por defecto
- Estilo visual en modo oscuro
- Despliegue con Docker listo para producción

---

## 📊 Variables utilizadas

Estas son las variables de entrada que utiliza el modelo para hacer la predicción:

| Variable            | Descripción                              |
|---------------------|------------------------------------------|
| `sepalLengthCm`     | Longitud del sépalo en centímetros       |
| `sepalWidthCm`      | Ancho del sépalo en centímetros          |
| `petalLengthCm`     | Longitud del pétalo en centímetros       |
| `petalWidthCm`      | Ancho del pétalo en centímetros          |

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/clasificador-iris.git
cd clasificador-iris

```bash
docker-compose up --build

🧑‍💻 Autor
Juan Pablo Tascón y Jurgen Sanclemente
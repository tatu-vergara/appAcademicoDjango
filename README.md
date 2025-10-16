# 🧠 Proyecto Académicos

Este proyecto fue desarrollado en equipo como parte del módulo 7 del Bootcamp Fullstack Python.

La aplicación **Académicos** es una plataforma educativa básica que modela las relaciones entre **profesores, cursos, estudiantes y evaluaciones**, siguiendo las mejores prácticas del **Django ORM**.

---

## 👥 Equipo de desarrollo

- **Tatu Vergara**
- **Damián Martínez**
- **Paulina Huentel**
- **Paulina Rojas**

---

## 🎯 Objetivo del proyecto

Modelar y relacionar entidades del contexto académico usando **Django**, representando los tres tipos de relaciones principales en una base de datos relacional:

| Tipo de relación | Django ORM | Ejemplo en el proyecto |
|------------------|-------------|--------------------------|
| **Uno a Muchos (1:N)** | `ForeignKey` | Un **Profesor** imparte varios **Cursos** |
| **Muchos a Muchos (N:N)** | `ManyToManyField` con modelo intermedio (`through`) | Un **Estudiante** se inscribe en varios **Cursos** mediante una **Inscripción** |
| **Uno a Uno (1:1)** | `OneToOneField` | Un **Estudiante** tiene un solo **PerfilEstudiante** |

---

## 🧩 Modelos implementados

- **Profesor** → nombre, email, especialidad  
- **Curso** → nombre, descripción, relación con Profesor  
- **Estudiante** → nombre, email  
- **Inscripción** → relación intermedia entre Estudiante y Curso  
  - fecha de inscripción  
  - estado (Activo / Finalizado)  
  - nota final (opcional)  
- **PerfilEstudiante** → biografía, foto, redes sociales  

---

## ⚙️ Tecnologías utilizadas

- **Python 3.13**
- **Django 5.1**
- **SQLite / MySQL**
- **Pillow** (para manejo de imágenes)
- **PyMySQL** o **mysqlclient** (dependiendo del entorno)

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<usuario>/<nombre-repo>.git
   cd <nombre-repo>

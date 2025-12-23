# proyecto-Django-antequera
tp3 comision 84995


# 🌍 Agencia de Viajes – Proyecto Django

Proyecto web desarrollado con **Django** siguiendo el **patrón MVT (Model–View–Template)**.  
La aplicación permite gestionar destinos, viajeros y viajes, además de realizar búsquedas en la base de datos.

---

## 📌 Objetivo del proyecto

- Desarrollar una web en Django utilizando el patrón MVT.
- Aplicar herencia de plantillas HTML.
- Crear modelos, formularios y vistas funcionales.
- Implementar una búsqueda en la base de datos.
- Presentar una interfaz mejorada con Bootstrap.

---

## 🛠️ Tecnologías utilizadas

- Python 3.13
- Django 6.0
- SQLite3
- HTML5
- Bootstrap 5
- Git / GitHub

---

## 📂 Estructura del proyecto

proyecto/
│
├── proyecto/
│ ├── settings.py
│ ├── urls.py
│
├── viajes/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
│ └── viajes/
│ ├── base.html
│ ├── inicio.html
│ ├── formulario.html
│ └── buscar.html
│
├── manage.py
└── README.md



---

## 📘 Modelos creados

### Destino
- nombre
- país

### Viajero
- nombre
- email

### Viaje
- destino (ForeignKey)
- viajero (ForeignKey)
- fecha
- descripción

---

## 🧾 Formularios

- Formulario para crear **Destinos**
- Formulario para crear **Viajeros**
- Formulario para crear **Viajes**
- Formulario para **buscar viajes por destino**

---

## 🔍 Funcionalidad de búsqueda

Se puede buscar un viaje ingresando el nombre del destino.  
La búsqueda se realiza sobre el modelo **Viaje**, filtrando por el campo `destino.nombre`.

---

## 🧭 Navegación del sitio

| URL | Función |
|----|--------|
| `/` | Página de inicio |
| `/destino/` | Crear destino |
| `/viajero/` | Crear viajero |
| `/viaje/` | Crear viaje |
| `/buscar/` | Buscar viaje por destino |
| `/admin/` | Panel de administración |

---

## 🧱 Herencia de plantillas

El archivo `base.html` contiene la estructura principal del sitio (navbar, footer, Bootstrap).  
Las demás vistas heredan de esta plantilla utilizando `{% extends %}`.

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/janteq03-lang/proyecto-Django-antequera.git

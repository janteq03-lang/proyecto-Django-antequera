# 🌍 Agencia de Viajes – Proyecto Final Django

Proyecto web desarrollado con **Django**, correspondiente al **Trabajo Práctico Final** de la comisión **84995**.  
La aplicación permite gestionar destinos, viajes y usuarios, incorporando autenticación, perfiles y una interfaz moderna con Bootstrap.

---

## 📌 Información general

- **Autor:** José Luis Antequera  
- **Edad:** 33 años  
- **Nacionalidad:** Venezolano  
- **Comisión:** 84995  
- **Trabajo Práctico:** Final  

El proyecto nace a partir del interés personal por los viajes y la idea de contar con una plataforma que permita organizar y documentar destinos, experiencias y actividades realizadas.

---

## 🎯 Objetivo del proyecto

- Desarrollar una aplicación web con Django utilizando el patrón **MVT (Model–View–Template)**.
- Implementar múltiples aplicaciones dentro del proyecto.
- Gestionar usuarios autenticados (registro, login, perfiles).
- Aplicar herencia de plantillas HTML.
- Crear modelos, formularios y vistas funcionales.
- Implementar búsquedas en la base de datos.
- Presentar una interfaz clara y moderna utilizando Bootstrap 5.

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

```text
proyecto/
│
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│
├── viajes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── viajes/
│           ├── base.html
│           ├── inicio.html
│           ├── formulario.html
│           └── buscar.html
│
├── usuarios/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── usuarios/
│           ├── login.html
│           ├── registro.html
│           ├── perfil_detail.html
│           └── perfil_edit.html
│
├── manage.py
└── README.md
```

---

## 📘 Modelos creados

### Destino
- nombre
- país

### Viaje
- destino (ForeignKey)
- usuario (ForeignKey)
- fecha
- descripción

### Usuario (App usuarios)
- username
- email
- avatar (opcional)
- datos de perfil

---

## 🧾 Formularios implementados

- Crear **Destinos**
- Crear **Viajes**
- Buscar viajes por destino
- Registro de usuarios
- Inicio de sesión
- Edición de perfil de usuario

---

## 🔐 Autenticación y usuarios

El sistema cuenta con:
- Registro de usuarios
- Login y logout
- Perfil de usuario
- Edición de datos personales
- Visualización de avatar
- Menú dinámico según el estado de autenticación

Solo los usuarios autenticados pueden acceder a las funcionalidades principales de gestión.

---

## 🔍 Funcionalidad de búsqueda

Se permite buscar viajes ingresando el nombre del destino.  
La búsqueda se realiza sobre el modelo **Viaje**, filtrando por el campo:

```python
destino__nombre
```

---

## 🧭 Navegación del sitio

| URL | Función |
|----|--------|
| `/` | Página de inicio |
| `/destino/` | Crear destino |
| `/viaje/` | Crear viaje |
| `/buscar/` | Buscar viaje |
| `/login/` | Iniciar sesión |
| `/registro/` | Registrar usuario |
| `/perfil/` | Ver perfil |
| `/admin/` | Panel de administración |

---

## 🧱 Herencia de plantillas

El archivo `base.html` contiene la estructura principal del sitio:
- Barra de navegación
- Footer
- Integración con Bootstrap
- Modal informativo "Acerca de mí"

Las demás vistas heredan de esta plantilla utilizando:

```django
{% extends "viajes/base.html" %}
```

---

## ℹ️ Acerca de mí

La página principal incluye un botón **"Acerca de mí"**, que muestra un modal con:
- Información general del proyecto
- Presentación personal del autor
- Motivación y contexto del desarrollo

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/janteq03-lang/proyecto-Django-antequera.git
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install django
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

7. Acceder desde el navegador:
```
http://127.0.0.1:8000/
```

---

## ✅ Estado del proyecto

✔ Proyecto funcional  
✔ Cumple los requisitos del Trabajo Práctico Final  
✔ Interfaz moderna y responsiva  
✔ Código organizado y modular  
✔ Listo para evaluación y presentación

---

📌 **Proyecto desarrollado con fines educativos**
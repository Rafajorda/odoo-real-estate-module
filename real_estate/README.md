# Real Estate Management Module - Odoo 19

Módulo de gestión inmobiliaria desarrollado siguiendo el tutorial oficial de Odoo.

## Características

### Capítulo 3: Modelo y Campos Básicos

- Modelo `estate.property` con campos básicos (nombre, descripción, código postal, precio, etc.)
- Atributos de campos (valores por defecto, readonly, copy=False)
- Campos reservados: `active` y `state`

### Capítulo 4: Vistas Personalizadas

- Vista de lista personalizada
- Vista de formulario organizada con grupos y notebook
- Menús de navegación

### Capítulo 5: Búsqueda y Filtros

- Vista de búsqueda por nombre y código postal
- Filtro "Available" para propiedades disponibles
- Agrupación por código postal

### Capítulo 6: Relaciones entre Modelos

- Modelo `estate.property.type` (Many2one)
- Modelo `estate.property.tag` (Many2many)
- Menú de Settings para gestionar tipos y etiquetas

## Instalación

1. Copiar el módulo a la carpeta `addons` de Odoo
2. Actualizar la lista de aplicaciones
3. Instalar el módulo "Real Estate Management"

## Estructura del Módulo

```
real_estate/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── estate_property.py
│   ├── estate_property_type.py
│   └── estate_property_tag.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── estate_property_views.xml
    ├── estate_property_type_tag_views.xml
    └── estate_menus.xml
```

## Autor

Rafa Jorda

## Versión

Odoo 19.0

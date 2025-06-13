# Cuestionario de HTML, CSS3 y JavaScript

1. ¿Cuál es la forma correcta de agregar un evento DOMContentLoaded en JavaScript?

```javascript
a) document.addEventListener('DOMContentLoaded', () => {
    // código aquí
});

b) document.onload = function() {
    // código aquí
};

c) window.addEventListener('load', () => {
    // código aquí
});

d) document.ready(function() {
    // código aquí
});
```
Respuesta correcta: a)

2. En CSS3, ¿cómo se define correctamente una transición suave para todos los cambios de propiedades?

```css
a) .elemento {
    transition: 0.3s ease;
}

b) .elemento {
    transition: all 0.3s ease;
}

c) .elemento {
    animation: all 0.3s;
}

d) .elemento {
    transform: transition 0.3s;
}
```
Respuesta correcta: b)

3. ¿Cuál es la sintaxis correcta para crear una función asíncrona que carga datos JSON en JavaScript?

```javascript
a) function loadData() {
    fetch('data.json').then(response => response.json());
}

b) async function loadData() {
    const data = fetch('data.json');
    return data.json();
}

c) async function loadData() {
    const response = await fetch('data.json');
    const data = await response.json();
    return data;
}

d) function loadData() {
    return await fetch('data.json').json();
}
```
Respuesta correcta: c)

4. En HTML, ¿cuál es la forma correcta de crear una barra de navegación semántica?

```html
a) <div class="navbar">
    <div class="menu">...</div>
</div>

b) <navigation>
    <menu>...</menu>
</navigation>

c) <nav>
    <ul>
        <li><a href="/">Home</a></li>
        ...
    </ul>
</nav>

d) <header class="navbar">
    <list>...</list>
</header>
```
Respuesta correcta: c)

5. En CSS3, ¿cómo se aplica correctamente un efecto de sombra a una imagen?

```css
a) img {
    shadow: 0 0 20px black;
}

b) img {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

c) img {
    image-shadow: 0 0 20px #000000;
}

d) img {
    filter: shadow(0 0 20px);
}
```
Respuesta correcta: b)

6. ¿Cuál es la forma correcta de crear un elemento dinámicamente en JavaScript y agregarle una clase?

```javascript
a) const element = document.new('div').addClass('myClass');

b) const element = document.createElement('div');
   element.class = 'myClass';

c) const element = document.createElement('div');
   element.setAttribute('class', 'myClass');

d) const element = new Element('div', {
    class: 'myClass'
});
```
Respuesta correcta: c)

7. En CSS3, ¿cómo se implementa correctamente un diseño flexible usando flexbox?

```css
a) .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

b) .container {
    display: grid;
    justify: space-between;
    align: center;
}

c) .container {
    position: flex;
    space-between: true;
    center-items: true;
}

d) .container {
    flex: display;
    justify: space-between;
    alignItems: center;
}
```
Respuesta correcta: a)

8. ¿Cuál es la manera correcta de manejar errores en una función asíncrona en JavaScript?

```javascript
a) async function handleData() {
    try {
        const response = await fetch('data.json');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

b) async function handleData() {
    const response = await fetch('data.json');
    const data = await response.json();
    if (error) {
        console.log(error);
    }
    return data;
}

c) function handleData() {
    fetch('data.json')
        .success(data => data.json())
        .error(err => console.log(err));
}

d) async function handleData() {
    await fetch('data.json').then(response => {
        return response.json();
    }).catch();
}
```
Respuesta correcta: a)

9. En HTML, ¿cuál es la forma correcta de vincular un archivo JavaScript y CSS en el head?

```html
a) <head>
    <script href="main.js"></script>
    <style href="style.css"></style>
</head>

b) <head>
    <script src="main.js"></script>
    <link rel="stylesheet" href="style.css">
</head>

c) <head>
    <javascript src="main.js"></javascript>
    <css href="style.css"></css>
</head>

d) <head>
    <script link="main.js"></script>
    <style src="style.css"></style>
</head>
```
Respuesta correcta: b)

10. En CSS3, ¿cómo se aplica un estilo específico a un elemento solo cuando está en la página principal?

```css
a) .element:if-page(home) {
    color: red;
}

b) .element[page="home"] {
    color: red;
}

c) .homepage-element {
    color: red !important;
}

d) .element:root {
    color: red;
}
```
Respuesta correcta: c)

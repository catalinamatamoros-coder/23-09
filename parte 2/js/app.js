// Lista de tareas en memoria
let tareas = ["Poner precios", "Recibir mercadería", "Reponer productos"];
let editandoIndice = -1;

// Mostrar tareas
function mostrarTareas() {
    const lista = document.getElementById('listaTareas');
    lista.innerHTML = '';
    
    tareas.forEach((tarea, indice) => {
        const li = document.createElement('li');
        
        if (editandoIndice === indice) {
            li.innerHTML = 
                '<input type="text" value="' + tarea + '" id="editInput">' +
                '<div>' +
                    '<button class="btn-edit" onclick="guardarEdicion(' + indice + ')">Guardar</button>' +
                    '<button class="btn-delete" onclick="cancelarEdicion()">Cancelar</button>' +
                '</div>';
        } else {
            li.innerHTML = 
                '<span>' + tarea + '</span>' +
                '<div>' +
                    '<button class="btn-edit" onclick="editarTarea(' + indice + ')">Editar</button>' +
                    '<button class="btn-delete" onclick="eliminarTarea(' + indice + ')">Eliminar</button>' +
                '</div>';
        }
        
        lista.appendChild(li);
    });
}

// Agregar tarea
function agregarTarea() {
    const input = document.getElementById('nuevaTarea');
    const texto = input.value.trim();
    
    if (texto !== '') {
        tareas.push(texto);
        input.value = '';
        mostrarTareas();
    }
}

// Eliminar tarea
function eliminarTarea(indice) {
    tareas.splice(indice, 1);
    mostrarTareas();
}

// Editar tarea
function editarTarea(indice) {
    editandoIndice = indice;
    mostrarTareas();
}

// Guardar edición
function guardarEdicion(indice) {
    const nuevoTexto = document.getElementById('editInput').value.trim();
    
    if (nuevoTexto !== '') {
        tareas[indice] = nuevoTexto;
        editandoIndice = -1;
        mostrarTareas();
    }
}

// Cancelar edición
function cancelarEdicion() {
    editandoIndice = -1;
    mostrarTareas();
}

// Inicializar
mostrarTareas();
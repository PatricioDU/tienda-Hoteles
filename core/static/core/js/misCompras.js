var misComprasVisible = false;

if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}

function ready(){
    
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for(var i=0;i<botonesEliminarItem.length; i++){
        var button = botonesEliminarItem[i];
        button.addEventListener('click',eliminarItemMisCompras);
    }

    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for(var i=0;i<botonesSumarCantidad.length; i++){
        var button = botonesSumarCantidad[i];
        button.addEventListener('click',sumarCantidad);
    }

    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for(var i=0;i<botonesRestarCantidad.length; i++){
        var button = botonesRestarCantidad[i];
        button.addEventListener('click',restarCantidad);
    }

    var botonesAgregarMisCompras = document.getElementsByClassName('boton-item');
    for(var i=0; i<botonesAgregarMisCompras.length;i++){
        var button = botonesAgregarMisCompras[i];
        button.addEventListener('click', agregarMisComprasClicked);
    }

    document.getElementsByClassName('btn-pagar')[0].addEventListener('click',pagarClicked)

}
function pagarClicked(){
    alert("Gracias por la compra");
    var misComprasItems = document.getElementsByClassName('Mis-Compras-items')[0];
    while (misComprasItems.hasChildNodes()){
        misComprasItems.removeChild(misComprasItems.firstChild)
    }
    actualizarTotalMisCompras();
    ocultarMisCompras();
}
function agregarMisComprasClicked(event){
    var button = event.target;
    var item = button.parentElement;
    var titulo = item.getElementsByClassName('titulo-item')[0].innerText;
    var precio = item.getElementsByClassName('precio-item')[0].innerText;
    var imagenSrc = item.getElementsByClassName('img-item')[0].src;
    console.log(imagenSrc);

    agregarItemMisCompras(titulo, precio, imagenSrc);

    hacerVisibleMisCompras();
	
}

function hacerVisibleMisCompras(){
    misComprasVisible = true;
    var misCompras = document.getElementsByClassName('Mis Compras')[0];
    misCompras.style.marginRight = '0';
    misCompras.style.opacity = '1';

    var items =document.getElementsByClassName('contenedor-items')[0];
    items.style.width = '60%';
}

function agregarItemMisCompras(titulo, precio, imagenSrc){
    var item = document.createElement('div');
    item.classList.add = ('item');
    var itemsMisCompras = document.getElementsByClassName('Mis-Compras-items')[0];

    var nombresItemsMisCompras = itemsMisCompras.getElementsByClassName('mis-compras-item-titulo');
    for(var i=0;i < nombresItemsMisCompras.length;i++){
        if(nombresItemsMisCompras[i].innerText==titulo){
            alert("El item ya se encuentra en el menú Mis compras");
            return;
        }
    }

    var itemsMisComprasContenido = `
        <div class="misCompras-item">
            <img src="${imagenSrc}" width="80px" alt="">
            <div class="misCompras-item-detalles">
                <span class="misCompras-item-titulo">${titulo}</span>
                <div class="selector-cantidad">
                    <i class="fa-solid fa-minus restar-cantidad"></i>
                    <input type="text" value="1" class="misCompras-item-cantidad" disabled>
                    <i class="fa-solid fa-plus sumar-cantidad"></i>
                </div>
                <span class="misCompras-item-precio">${precio}</span>
            </div>
            <button class="btn-eliminar">
                <i class="fa-solid fa-trash"></i>
            </button>
        </div>
    `
    item.innerHTML = itemMisComprasContenido;
    itemsMisCompras.append(item);

     item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemMisCompras);

    var botonRestarCantidad = item.getElementsByClassName('restar-cantidad')[0];
    botonRestarCantidad.addEventListener('click',restarCantidad);
    var botonSumarCantidad = item.getElementsByClassName('sumar-cantidad')[0];
    botonSumarCantidad.addEventListener('click',sumarCantidad);

    actualizarTotalMisCompras();
}
function sumarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('mis-compras-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('mis-compras-item-cantidad')[0].value;
    cantidadActual++;
    selector.getElementsByClassName('mis-compras-item-cantidad')[0].value = cantidadActual;
    actualizarTotalMisCompras();
}
function restarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('mis-compras-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('mis-compras-item-cantidad')[0].value;
    cantidadActual--;
    if(cantidadActual>=1){
        selector.getElementsByClassName('mis-compras-item-cantidad')[0].value = cantidadActual;
        actualizarTotalMisCompras();
    }
}

function eliminarItemMisCompras(event){
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
    actualizarTotalMisCompras();
    ocultarMisCompras();
}
function ocultarMisCompras(){
    var misComprasItems = document.getElementsByClassName('mis-compras-items')[0];
    if(misComprasItems.childElementCount==0){
        var misCompras = document.getElementsByClassName('misCompras')[0];
        misCompras.style.marginRight = '-100%';
        misCompras.style.opacity = '0';
        misComprasVisible = false;
    
        var items =document.getElementsByClassName('contenedor-items')[0];
        items.style.width = '100%';
    }
}
function actualizarTotalMisCompras(){
    var misComprasContenedor = document.getElementsByClassName('misCompras')[0];
    var misComprasItems = misComprasContenedor.getElementsByClassName('misCompras-item');
    var total = 0;
    for(var i=0; i< misComprasItems.length;i++){
        var item = misComprasItems[i];
        var precioElemento = item.getElementsByClassName('mis-compras-item-precio')[0];
        var precio = parseFloat(precioElemento.innerText.replace('$','').replace('.',''));
        var cantidadItem = item.getElementsByClassName('mis-compras-item-cantidad')[0];
        console.log(precio);
        var cantidad = cantidadItem.value;
        total = total + (precio * cantidad);
	
    }
    total = Math.round(total * 100)/100;

    document.getElementsByClassName('mis-compras-precio-total')[0].innerText = '$'+total.toLocaleString("es") + ",00";


}

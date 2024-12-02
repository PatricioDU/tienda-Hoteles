$(document).ready(function() {
    // Realizar la solicitud a la API cuando la página cargue
    $.get('https://fakestoreapi.com/products', function(data) {
        $('#productos').empty();

        $.each(data, function(i, item) {
            var card = `
                <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3 text-center">
                    <div class="card h-100">
                        <img src="${item.image}" class="card-img-top" alt="${item.title}">
                        <div class="card-body">
                            <h5 class="card-title">${item.title}</h5>
                            <p class="card-text">${item.description}</p>
                            <p class="card-price">$${item.price}</p>
                        </div>
                    </div>
                </div>
            `;
            $('#productos').append(card);
        });
    });
});

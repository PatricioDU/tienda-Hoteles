$(document).ready(function() {
    $("form").validate();

    $.validator.addMethod("validURL", function(value, element) {
        return /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i.test(value);
    }, "Ingrese una URL válida.");
    
    $("li.list-group-item").each(function() {
        $(this).click(function(e) {
            e.preventDefault(); 
            var href = $(this).find("a").attr("href");
            if ($(this).find("a").validURL()) {
                window.location.href = href;
            } else {
                alert("URL inválida.");
            }
        });
    });
});


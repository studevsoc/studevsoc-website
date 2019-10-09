$(window).on('load',function(){
    var delayMs = 700; // delay in milliseconds

    setTimeout(function(){
        $('#myModal').modal('show');
    }, delayMs);
});

function connect_contact()
{
     location.href = "#contact";
}

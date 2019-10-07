new WOW().init();

       $('#myModal').on('shown.bs.modal', function () {
         $('#myInput').trigger('focus')
       })

jQuery(function($){
    // ready
    jQuery(document).ready(function(){
        $('#select_type_buttom').hide();
        $('#title_buttom').hide();
    });

    $('input[name="toggle"]').change(function() {
        var prop = $('#toggle').prop('checked');
        if(prop){
            $('#select_type_buttom').show();
            $('#title_buttom').show();
            $('tr').each(function() {
                $(this).find('#cardTypeName').remove();
                $(this).find('#image').remove();
                $(this).find('#cardName').remove();
            });
        } else {
            location.reload();
        }
        $('.filter').multifilter();
    });
});



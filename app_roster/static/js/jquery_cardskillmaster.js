jQuery(function($){
    // ready
    jQuery(document).ready(function(){
        displayFlag = $("#displayFlag").text();
        if(displayFlag == 1 || displayFlag == 2 || displayFlag == 3 || displayFlag == 4 || displayFlag == 5 || displayFlag == 6){
            $('#select_type_buttom').hide();
            $('#title_buttom').hide();
            $('#card_type_name').hide();
        }
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



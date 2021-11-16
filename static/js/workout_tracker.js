$(document).ready(function() {

    $("#id_name").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()
    })

    $("#id_notes").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()
    })


    $(document).on('focusout', "input[id*='id_set_set-']", function(){
        console.log("Focus out!")
        frm = $(this).closest("form")
        token = $(this).closest("[name='csrfmiddlewaretoken']")
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            header: {'X-CSRFToken':token},
            success: function (data) {
                console.log(data);
            },
            error: function(data) {
                console.log("Something went wrong!");
            }
        });
        return false;
    })



    $("button[name^='add-set-']").click(function(e){
        e.preventDefault()
        frm = $(this).closest("form")
        token = $(this).closest("[name='csrfmiddlewaretoken']")
        set_table = $(this).siblings("#add-set")
        load_target = " #set-list-" + set_table.attr('value')
        console.log(set_table.attr('value'))
        console.log(window.location.pathname + " #set-list-" + set_table.attr('value') + " tr")
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            header: {'X-CSRFToken':token},
            success: function (data) {
                $(load_target).load(window.location.pathname + " #set-list-" + set_table.attr('value') + " tr");
                console.log("Success!");
            },
            error: function(data) {
                console.log("Something went wrong!");
            }
        });
        return false;
    })
})




// $('#fail-btn').each(function () {
//     alert($(this).closest('.btn-check').id);
// });
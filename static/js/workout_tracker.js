$(document).ready(function() {


    $("#id_name").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()

    })
    $("#id_notes").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()

    })
    $("input[id*='id_set_set-']").focusout(function() {
        console.log("Focus out!")
        frm = $(this).closest("form")
        token = $(this).closest("[name='csrfmiddlewaretoken'")
        frm.submit(function () {
            console.log("Submit!")
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
        });
        frm.submit()
    })
})

// $('#fail-btn').each(function () {
//     alert($(this).closest('.btn-check').id);
// });
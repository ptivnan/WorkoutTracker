$(document).ready(function() {


    $("#id_name").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()

    })
    $("#id_notes").focusout(function() {
        console.log("Focus out!")
        $("#form_workout_update").submit()

    })
})

// $('#fail-btn').each(function () {
//     alert($(this).closest('.btn-check').id);
// });
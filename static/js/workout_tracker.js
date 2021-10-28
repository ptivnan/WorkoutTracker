$(document).ready(function() {
    console.log("Ready!")
    console.log($("#fail-btn").siblings().get(0).id)
    console.log($('.btn-check').attr('id'))
    $("#fail-btn").each(function () {
        var sib_id = $(this).siblings().get(0).id
        $(this).attr('for', sib_id)
    })

    $()

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
$("#username").change(function () {
    var username = $(this).val();

    $.ajax({
        type: 'GET',
        url: '/usernamevalidation',
        data: {
            "username": username,
        },
        dataType: 'json',
        success: function (result) {
            if (result.is_taken) {
                $("#username_validation").html(result.error_message);
            }
            else {
                $("#username_validation").html(result.success_message);
            }
        },
        error: function (result) {
            $("#username_validation").html(result.request_error)
        }
    });
});

$('#password, #confirm_password').on('keyup', function () {
    if ($('#password').val() != $('#confirm_password').val()) {
        $('#validation_msg').html('Passwords do not match!');
    }
    else {
        $('#validation_msg').html('');
    }
});

function checkIsOwner() {
    checkbox = document.getElementById("isOwner");
    if (checkbox.checked) {
        checkbox.value = 'True';
        //console.log(checkbox.value);
    }

}

$("#phone").change(function () {
    //console.log($(this).val());
    var phone = $(this).val();
    if ((phone.length == 10) && isNaN(phone) == false) {
        $("#phone_validation").html("");
    }
    else {
        $("#phone_validation").html("Please enter a valid phone number!");
    }
});

function changeState() {
    checkbox = document.getElementById("multipleFlats");
    if (checkbox.checked) {
        //console.log("TRUE");
        checkbox.value = 'True';
        $('#divFlat2').css('visibility', 'visible');
        $('#flat_1').html("Enter your first flat no:");
        $("#flatNo1").attr("placeholder", "First flat no:");
    }
    else {
        //console.log("FALSE");
        checkbox.value = 'False';
        $('#divFlat2').css('visibility', 'hidden');
        $('#flat_1').html("Enter your flat no:");
        $("#flatNo1").attr("placeholder", "Your flat no:");
    }
}

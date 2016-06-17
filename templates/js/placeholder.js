$(function () {
    // check placeholder browser support
    if (!Modernizr.input.placeholder) {
        // set placeholder values
        $(this).find('[placeholder]').each(function () {
            if ($(this).val() == '') // if field is empty
            {
                $(this).val($(this).attr('placeholder'));
            }
        });
        // focus and blur of placeholders
        $('[placeholder]').focus(function () {
            if ($(this).val() == $(this).attr('placeholder')) {
                $(this).val('');
                $(this).removeClass('placeholder');
            }
        }).blur(function () {
            if ($(this).val() == '' || $(this).val() == $(this).attr('placeholder')) {
                $(this).val($(this).attr('placeholder'));
                $(this).addClass('placeholder');
            }
        });
        // remove placeholders on submit
        $('[placeholder]').closest('form').submit(function () {
            $(this).find('[placeholder]').each(function () {
                if ($(this).val() == $(this).attr('placeholder')) {
                    $(this).val('');
                }
            })
        });
    }
});


function checkUserName() {
    if ($("#txtUserName").val().length == 0) {
        $("#txtUserName").next("span").css("color", "red").text("*用户名不为空");
        return false;
    }

    else {
        $("#txtUserName").next("span").css("color", "red").text("");
        return true;
    }
}
//check the pwd 
function checkUserPwd() {
    if ($('#txtUserPwd').val().length == 0) {
        $('#txtUserPwd').next("span").css("color", "red").text("*密码不为空");
        return false;
    }
    else {
        $('#txtUserPwd').next("span").css("color", "red").text("");
        return true;
    }
}

$(document).ready(function () {
    $("#checkit").click(function () {
        if (checkUserName() && checkUserPwd()) {
            var data = {
                user_id: $('#txtUserName').val(),
                password: $('#txtUserPwd').val()
            };
//提交数据给Login.ashx页面处理 
            $.post("/do/login", data, function (result) {
                if (result == "0") //登录成功
                {
                    alert("登录成功！您可以进行其他操作了！");
// 关闭模拟窗口 
                    window.parent.window.jBox.close();
                }

                else {
                    alert("登录失败！请重试");
                }
            });
        }
        else {
            checkUserName();
            checkUserPwd();
        }
    });
});


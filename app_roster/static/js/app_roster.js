jQuery(document).ready(function(){
 //jQueryで実行する内容
$(function(){
    $('#btn_login').click(function() {
            uid = $("#txt_userid").val()
            pwd = $("#txt_password").val()
            // 初期化
            $("#txt_userid").css("background-color","white");
            $("#txt_password").css("background-color","white");
            // 空チェック
            if(uid == ""){
                $("#txt_userid").css("background-color","red");
            } else if (pwd == ""){
                $("#txt_password").css("background-color","red");
            }
            if(uid=="" || pwd==""){
                $("#txt_userid").css("background-color","red");
                $("#txt_password").css("background-color","red");
                $("#div_errorMessage").html("ユーザーIDまたはパスワードが入力されていません。<br/>入力してください。");
            } else {
                // サーバーチェック
                $("form").submit()
            }
        });
    });
 });

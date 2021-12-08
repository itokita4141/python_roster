jQuery(document).ready(function(){
 //jQueryで実行する内容
$(function(){
    // login画面load時
    $(document).ready(function(){
//  const data = $.parseJSON('{{ data_json|safe }}');
//
//  console.log(data.sample1);  // [1, 2, 3]
//        alert("document.load");
//        const data = JSON.parse("{{ data_json|safe }}");
//        var data_json = JSON.parse('{{data_json | safe}}');
//        var json = $.parseJSON("{{ data_json | safe }});
//        var data_json={{"errorMessage"|returnMessageParams}};
//        $("div_errorMessage").html(json.errorMessage);
    });

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

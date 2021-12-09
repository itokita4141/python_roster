jQuery(function($){
    // ready
    jQuery(document).ready(function(){
    //jQueryで実行する内容
    });

    // login画面load時
    $(document).ready(function(){
        // ボタン押下時の入力チェック時の結果をDjangoより取得
        // djangoより値を受け取れない
        // todo
    });

    // ログイン
    $('#btn_login').click(function(){
        console.log("jqueryのlogin関数 start");
        // ユーザー名パスワードの値を取得
        uid = $("#txt_userid").val();
        pwd = $("#txt_password").val();
        console.log("uid=" + uid);
        console.log("password" + pwd);
        // 画面上のデータ取得
        $("#txt_userid").css("background-color","white");
        $("#txt_password").css("background-color","white");
        // 空チェック
        if(uid == "" || pwd==""){
            if(uid == "")$("#txt_userid").css("background-color","red");
            if(pwd == "")$("#txt_password").css("background-color","red");
            $("#div_errorMessage").html("ユーザーIDまたはパスワードが入力されていません。<br/>入力してください。");
        } else {
            console.log("画面上入力チェックok");
            console.log("ajax start");
            $.ajax({
                'url': 'ajaxlogincheck/',
                'type': 'POST',
                'data': {
                        'uid': uid,
                        'pwd': pwd,
                },
                'dataType': 'json'
            }).done((data) => {
                // 成功時はserver側のredirectで次画面へ遷移
                console.log("ajax_roster_login:success");
                if(data.result == 'ok'){
                    // 次ページへ遷移
                    window.location.href = '../input/';
                } else if (data.result == 'ng'){
                    // エラーメッセージをセット
                    $("#div_errorMessage").html(data.errorMessage);
                } else {
                    alert('ログイン結果の戻り値が不正です。result');
                }
            }).fail(() => {
              console.log("ajax end");
              // 失敗した時の処理
              alert("メッセージの送信に失敗しました。");
              console.log("ajax_roster_login:fail");
            });
        }
        console.log("jqueryのlogin関数 end");
    });
});

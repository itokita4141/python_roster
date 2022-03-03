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
        var csrf_token = getCookie("csrftoken");
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
                'dataType': 'json',
                // 送信前にヘッダにcsrf_tokenを付与。
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                    }
                },
                success: function(data) {
//                    alert("beforeSend:success");
                    console.log(data);
                },
                error: function(xhr, status, error) {
//                    alert("beforeSend:error");
                    alert(status + "\n" +
                            "Status: " + xhr.status + "\n" + error);
                }
            }).done((data) => {
//                alert("done:success");
                // 成功時はserver側のredirectで次画面へ遷移
                console.log("ajax_roster_login:success");
                if(data.result == 'ok'){
                    // 次ページへ遷移
                    window.location.href = '../loginList/' + uid + '/' + pwd + '/';
                } else if (data.result == 'ng'){
                    // エラーメッセージをセット
                    $("#div_errorMessage").html(data.errorMessage);
                } else {
                    alert('ログイン結果の戻り値が不正です。result');
                }
            }).fail(() => {
                alert("done:fail");
                console.log("ajax end");
                // 失敗した時の処理
                alert("メッセージの送信に失敗しました。");
                console.log("ajax_roster_login:fail");
            });
        }
        console.log("jqueryのlogin関数 end");
    });

    // csrf_tokenの取得に使う
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $(document).on("click", "#button_id", function() {
        var button = $(this);
        var csrf_token = getCookie("csrftoken");
        var rslt = window.confirm("Do you really want to do?");
        if (rslt) {
            $.ajax({
               type: "POST",
               url: "ajaxlogincheck/",
               data: {
                   "key1": "value1",
                   "k2": "v2",
               },
               contentType: "application/json",
               // 送信前にヘッダにcsrf_tokenを付与。
               beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                    }
                },
                success: function(data) {
                    alert(data);
                },
                error: function(xhr, status, error) {
                    alert(status + "\n" +
                            "Status: " + xhr.status + "\n" + error);
                }
            });
        }
    });
});

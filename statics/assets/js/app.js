$(function () {
    $.backstretch("assets/img/bg.jpg");
    //www.bootstrapmb.com
	var count = 0;
    var classes = [ "theme_1", "theme_2", "theme_3", "theme_4" ];
    var length = classes.length;
    $(function () {
        $('.pvr_chat_wrapper').toggleClass('active');

        $('.pvr_chat_button, .pvr_chat_wrapper .close_chat').on('click', function () {
            $('.pvr_chat_wrapper').toggleClass('active');
            return false;
        });

        $('.message-input').on('keypress', function (e) {
            if (e.which == 13) {
                var val = ($(this).val() !== '') ? $(this).val() : "Lorem Ipsum is simply dummy text of the printing.";
                $('.chat-messages').append('<div class="message self"><div class="message-content">' + val + '</div></div>');
                $(this).val('');
                setTimeout(function () {
                    $('.chat-messages').append('<div class="message"><div class="message-content">' + val + '</div></div>');
                    $messages_w.scrollTop($messages_w.prop("scrollHeight"));
                    $messages_w.perfectScrollbar('update');
                }, 200)
                var $messages_w = $('.pvr_chat_wrapper .chat-messages');
                $messages_w.scrollTop($messages_w.prop("scrollHeight"));
                $messages_w.perfectScrollbar('update');
                return false;
            }
        });

        $('.pvr_chat_wrapper .chat-messages').perfectScrollbar();
        //www.bootstrapmb.com
        $(".change_chat_theme").on('click', function () {
            $(".chat-messages").removeAttr("class").addClass("chat-messages " + classes[ count ]);
            if (parseInt(count, 10) === parseInt(length, 10) - 1) {
                count = 0;
            } else {
                count = parseInt(count, 10) + 1;
            }
            var $messages_w = $('.pvr_chat_wrapper .chat-messages');
            $messages_w.scrollTop($messages_w.prop("scrollHeight"));
            $messages_w.perfectScrollbar('update');
        })
    });
});

$(document).ready(function(){
$.material.init();
        $(document).on("submit","#register-form",function(e){
            e.preventDefault();
            var form = $('#register-form').serialize();
            $.ajax({
                url: '/postregistration',
                type:'POST',
                data: form,
                success: function(response){
                }
            });

        });


        $(document).on("submit","#login-form",function(e){
            e.preventDefault()
            var form = $('#login-form').serialize()
            $.ajax({
                url: '/checklogin',
                type:'POST',
                data: form,
                success: function(response){
                    if(response== 'error')
                        alert("Could not login")
                    else
                        console.log("Logged in as ",response)
                        window.location.href="/"

                }
            });

        });

})

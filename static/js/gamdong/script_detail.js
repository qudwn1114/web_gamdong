$(document).ready(function(){
    if($("#article").length){
        $('#article')[0].scrollIntoView();
        $('#btn-list').click(function(){
            window.location.href = window.location.pathname;
        });
    }
});
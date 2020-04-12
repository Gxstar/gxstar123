$(function(){
    // 处理ckeditor
    function CKupdate() {
        for (instance in CKEDITOR.instances)
            CKEDITOR.instances[instance].updateElement();
    }

    // 文章编辑提交
    $('#articleEdit').click(function() {
        CKupdate();
        $.post("saveArticle/",{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            id:articleid,
            title:$("#id_title").val(),
            author:$("#id_author").val(),
            category:$("#id_category").val(),
            cover:$("#id_cover").val(),
            body:CKEDITOR.instances.id_body.getData(),
        },function(result,status){
            alert(result);
        })
    });

    // 处理分类选项样式
    $("#id_category").addClass("form-control");
});
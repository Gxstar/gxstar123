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
            title:$("#id_title").val(),
            author:author,

        })
    });

    // 处理分类选项样式
    $("#id_category").addClass("form-control");
});
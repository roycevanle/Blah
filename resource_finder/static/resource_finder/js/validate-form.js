function validateForm(form_id) {
    var errors = false;

    var selects = $("#" + form_id).find("select");

    $(selects).each(function() {
        var that = $(this);
        var selected = that.val();

        if(selected === null && that.prop("required")) {
            that.parent().addClass("has-error");
            errors = true;
        } else {
            that.parent().removeClass("has-error");
        }
    });

    var inputs = $("#" + form_id).find("input");

    $(inputs).each(function() {
        var that = $(this);

        if(that.val() === "" && that.prop("required")) {
            that.parent().addClass("has-error");
            errors = true;
        } else {
            that.parent().removeClass("has-error");
        }
    });

    return !errors;
}
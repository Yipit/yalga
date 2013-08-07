$(function(){
    var REMOVE_BUTTON = '<a class="remove btn btn-danger" href="#">Not going</a>';
    var ADD_BUTTON = '<a class="add btn btn-success" href="#">Going</a>';

    function make_item(person_id, person_name, button) {
        var $li = $('<li></li>');
        var $input = $('<input />');
        var $span = $('<span class="name"></span>');
        $input.attr("name", "person-id");
        $input.attr("type", "hidden");
        $input.attr("value", person_id);

        $span.text(person_name);
        $li.append($input)
        $li.append($span)
        $li.append(button)
        return $li;
    }

    $(".comment textarea").on("keydown", function(e){
        var currentLength = $(this).text().length;
        if (currentLength >=140) {

            $(this).text($(this).text().substr(0, 140));
            return e.preventDefault();
        }
    });
    $(".remove").on("click", function(e){
        var $self = $(this);
        var $li = $(this).parents("li");
        var person_id = $li.data("id");
        var person_name = $li.find(".name").text()

        var item = make_item(person_id, person_name, '');
        $("#no-list").append(item);
        $li.remove();
        return e.preventDefault();
    });
    $("#generate-now").on("click", function(e){
        e.preventDefault();
        var ids_of_people_going = [];
        $("#yes-list li input.person-id").each(function(i){
            ids_of_people_going.push($(this).val());
        });
        var data = {
            "json_list": JSON.stringify(ids_of_people_going),
            "number_of_groups": $("#total_groups").val()
        }
        $.post("/generate", data, function(raw){
            var data = JSON.parse(raw);
            var codes = [];
            _.each(data, function(value, key) {
                codes.push(value["code"])
            });
            var url = "/show-groups/" + codes.join("|")
            location.href = url;
        });

    });
});
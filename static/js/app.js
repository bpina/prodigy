$(document).ready(function(){
  characterForm = $("#create-character")
  if(characterForm) {
    characterForm.submit(function() {
      $.post($(this).attr("action"),$(this).serialize(), function(data) {
        alert(data)
      })
      return false
    })
  }

  $(".character-list-item").each(function() {
    $("td>.character-make-default-link",this).click( function() {
      character_id = $(this).attr("id").replace("-character-make-default-link", "")
      $(".character-list-item").each(function() {
        id = $(this).attr("id").replace("-user-character", "")
        $.post("/characters/update/", {id: parseInt(id), is_default: false}, function(data) {
          $("td>.character-is-default-label",this).text("")
        })
      })
      $.post("/characters/update/", {id: parseInt(character_id), is_default: true}, function(data) {
        $("#" + character_id + ">td>.character-is-default-label").text("default")
      })
    })
  })
});

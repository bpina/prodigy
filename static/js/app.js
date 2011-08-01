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
});

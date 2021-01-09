enableImageOverlay()
document.getElementById("dropdownMenuLink").click()
function enableImageOverlay() {
    var profileImage = document.getElementById("profile_img_display")
    console.log(profileImage)
    profileImage.style.opacity = "1"
    profileImage.style.display = "block"
    profileImage.style.width = "100%"
    profileImage.style.height = "auto"
    profileImage.style.transition = "0.5s ease"
    profileImage.style.backfaceVisibility = "hidden"
    profileImage.style.cursor = "pointer"

    var text = document.getElementById("id_text")
    // text.style.background = "#dc3545"
    // text.style.color = "white"
    text.style.borderRadius = "10%"
    text.style.fontSize = "30px"
    text.style.padding = "16px 32px"
    text.style.cursor = "pointer"

    var middleContainer = document.getElementById("text_container")
    // middleContainer.style.transition = "0.5s ease"
    middleContainer.style.opacity = "0"
    middleContainer.style.position = "absolute"
    middleContainer.style.top = "50%"
    middleContainer.style.left = "50%"
    middleContainer.style.transform = "translate(-50%, -50%)"

    var imageContainer = document.getElementById("image_container")
    imageContainer.addEventListener('mouseover', function(event) {
        profileImage.style.opacity = "0.3"
        middleContainer.style.opacity = "1"
    })

    imageContainer.addEventListener('mouseout', function(event) {
        profileImage.style.opacity = "1"
        middleContainer.style.opacity = "0"
    })

    imageContainer.addEventListener('click', function(event) {        
        document.getElementById('profile_image').click()
    })

    var cropConfirm = document.getElementById('img_crop_confirm')
    cropConfirm.classList.add("d-none")
  }

  function disableImageOverlay() {
      var profileImage = document.getElementById("profile_img_display")
      var middleContainer = document.getElementById("text_container")
      var imageContainer = document.getElementById("image_container")
      var text = document.getElementById("id_text")
      imageContainer.removeEventListener('mouseover', function(event) {
        // profileImage.style.opacity = "0.3"
        // middleContainer.style.opacity = "1"
    })

    imageContainer.removeEventListener('mouseout', function(event) {
        // profileImage.style.opacity = "1"
        // middleContainer.style.opacity = "0"
    })

    profileImage.style.opacity = "1"
    middleContainer.style.opacity = "0"
    text.style.opacity = "0"
    text.style.cursor = "default"

    imageContainer.removeEventListener('click', function(event) {
        event.preventDefault()
    })

    profileImage.addEventListener('click', function(event) {
        event.preventDefault()
    })

    console.log('here')
    var cropConfirm = document.getElementById('img_crop_confirm')
    cropConfirm.classList.remove('d-none')
    console.log('sucs')

    var confirm = document.getElementById('confirm')
    var cancel = document.getElementById('cancel')

    confirm.addEventListener('click',function(event){
        // todo
        enableImageOverlay()                
    })

    cancel.addEventListener('click',function(event){
        // todo        
        window.location.reload();
    })
  }
  
  function readURL(input){
      if(input.files && input.files[0]){
          var reader = new FileReader()
          reader.onload = function(e){
              disableImageOverlay()
              var image= e.target.result
              var imageField= document.getElementById("profile_img_display")
              imageField.src = image
          }
          reader.readAsDataURL(input.files[0])
      }
  }
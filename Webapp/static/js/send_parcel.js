var user = document.getElementById("search_user")
var search = document.getElementById("search_user_btn")
var ddBtn = document.getElementById("dropdownMenuButton")
var values = []
ddBtn.click()
search.onclick = async function(){
    if(user.value != '' || user != null){
        var api = '/user/api/get-user/?data'
        let response = await fetch(api.concat("=", user.value))
        let data = await response.json()
        if(data.found){
            data.data.forEach(element => {
                values.push(JSON.parse(element)[0]['fields'])
            });
//            console.log(values[0])
            search_result(values)
        }        
    }
}
function search_result(values){
    var content = ''
    values.forEach(value =>{
        content = content + `
            <div class="search-result" id='${values.indexOf(value)}'>
                        <img src="https://scontent.fbdq2-1.fna.fbcdn.net/v/t1.0-9/87552205_2527685700812338_1281628682191896576_o.jpg?_nc_cat=103&ccb=3&_nc_sid=09cbfe&_nc_ohc=bzpK1mCsZsoAX9p2BS0&_nc_ht=scontent.fbdq2-1.fna&oh=4fc5afe6be7b44bb63e5eadcef5b865e&oe=60649E4B" alt="">
                        <span>${value.username}</span>
                      </div>
        `
    })
    $(".search-result-container").removeClass("d-none");
    if(content == ''){
        content = `<h6>No result found....</h6>`
    }
    else{
        document.querySelector(".search-result-container").innerHTML  = content;
        $(".search-result").click(function(){
                var data = values[this.id]
                document.getElementById('id_r_full_name').value = data.username;
                  document.getElementById('id_r_number1').value = data.number1;
                  document.getElementById('id_r_address1').value = data.address1;
                  document.getElementById('id_r_address2').value = data.address2;
                  document.getElementById('id_r_city').value = data.city;
                  document.getElementById('id_r_state').value = data.state;
                  document.getElementById('id_r_zip').value = data.zip;
                  document.getElementById('r_country').value = data.country;
                  document.querySelector(".search-result-container").innerHTML  = '';
                  $(".search-result-container").addClass("d-none");
                  user.value = ""
            })
    }
}
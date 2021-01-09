var user = document.getElementById("search_user")
var search = document.getElementById("search_user_btn")
var ddBtn = document.getElementById("dropdownMenuButton")
ddBtn.click()
search.onclick = async function(){
    if(user.value != '' || user != null){
        var api = '/user/api/get-user/?data'
        let response = await fetch(api.concat("=", user.value))
        let data = await response.json()
        var values = []
        if(data.found){
            data.data.forEach(element => {
                values.push(JSON.parse(element)[0]['fields'])
            });
            search_result(values)
        }        
    }
}

function search_result(data){
    var users = new Array(data.length)
    var list = document.getElementById("id_dropdown_menu")
    for(var i=0;i<data.length;i++){
        var anc = document.createElement("div")
        var node = document.createTextNode("hello")
        anc.appendChild(node)        
        console.log(data[i])
    }
    list.appendChild(anc)
    ddBtn.click()    
} 
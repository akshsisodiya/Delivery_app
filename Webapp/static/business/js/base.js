// slider collapse button 
$(function(){
    $('#sliderCollapse').on('click',function(){
        $('#sidebar, #content').toggleClass('active');        
    });
});

// multiple list action button disable/enable if any of checkbox is checked or not
$(function(){
    $('.form-check-input').on('change',function(){
        $('div.list-'+this.id).toggleClass('border-primary');
        $('div.list-'+this.id+'>.btn-grp>button').prop('disabled', function(i,v){return !v})
        if($('input[type=checkbox]').is(':checked')){
            $('.multilist-action').prop('disabled',false);
        }
        else{
            $('.multilist-action').prop('disabled',true);
        }
    })
})

// request accept button
function request_accept(order_id) {
    $.post('/business/change-status/', {id:order_id, status:2, csrfmiddlewaretoken : token}, function(response){       
    if (window.location.pathname == "/business/pending-requests/"){
        $('div.list-'+order_id+'>.btn-grp>button').addClass('d-none')  
        $('div.list-'+order_id+'>.btn-grp>.accepted').removeClass('d-none')  
    }
    else{
        location.reload()
    }
});    
}

// request decline button
function request_decline(order_id) {
    $.post('/business/change-status/', {id:order_id, status:3, csrfmiddlewaretoken : token}, function(response){       
        if (window.location.pathname == "/business/pending-requests/"){
            $('div.list-'+order_id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+order_id+'>.btn-grp>.declined').removeClass('d-none')  
        }
        else{
            location.reload()
        }
    });
}

// multiple list accept button
function mass_request_accept() {
    const order_ids = $('.pending-requests-list-checkbox:checked').map(function(){
        return this.id
    }).get()

    $.post('/business/mass-change-status/', {orders:order_ids, status:2, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.accepted').removeClass('d-none')
        })
      });
}

// multiple list decline button
function mass_request_decline(){
    const order_ids = $('.pending-requests-list-checkbox:checked').map(function(){        
        return this.id
    }).get()
    
    $.post('/business/mass-change-status/', {orders:order_ids, status:3, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.declined').removeClass('d-none')
        })
      });
}

// collect package button
function package_collected(order_id) {
    $.post('/business/change-status/', {id:order_id, status:4, csrfmiddlewaretoken : token}, function(response){       
        if (window.location.pathname == "/business/pending-delivery/"){
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.collected').removeClass('d-none')
        }
        else{
            location.reload()  
        }
      });
}

// delivered button
function delivered(order_id){
    $.post('/business/change-status/', {id:order_id, status:6, csrfmiddlewaretoken: token}, function(response){
        if (window.location.pathname == "/business/pending-delivery/"){
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.delivered').removeClass('d-none')
        }
        else{
            location.reload()  
        }
    })
}

// cancel delivery button
function cancel_delivery(order_id){
    $.post('/business/change-status/', {id:order_id, status:5, csrfmiddlewaretoken: token}, function(response){
        if (window.location.pathname == "/business/pending-delivery/"){
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.canceled').removeClass('d-none')
        }
        else{
            location.reload()  
        }
    })
}

// multiple list collected button
function mass_package_collected(){
    const order_ids = $('.pending-collection-list-checkbox:checked').map(function(){        
        return this.id
    }).get()
    
    $.post('/business/mass-change-status/', {orders:order_ids, status:4, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.collected').removeClass('d-none')
        })
      });
}

// multiple collection pending list canceled button
function mass_collection_cancel_delivery(){
    const order_ids = $('.pending-collection-list-checkbox:checked').map(function(){        
        return this.id
    }).get()
    
    $.post('/business/mass-change-status/', {orders:order_ids, status:5, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.canceled').removeClass('d-none')
        })
      });
}

// multiple delivery pending list canceled button
function mass_delivery_cancel_delivery(){
    const order_ids = $('.pending-delivery-list-checkbox:checked').map(function(){        
        return this.id
    }).get()
    
    $.post('/business/mass-change-status/', {orders:order_ids, status:5, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.canceled').removeClass('d-none')
        })
      });
}

// multiple delivery pending list canceled button
function mass_delivered(){
    const order_ids = $('.pending-delivery-list-checkbox:checked').map(function(){        
        return this.id
    }).get()
    
    $.post('/business/mass-change-status/', {orders:order_ids, status:6, csrfmiddlewaretoken : token}, function(response){       
        order_ids.map(function(id) {
            $('div.list-'+id+'>.btn-grp>button').addClass('d-none')  
            $('div.list-'+id+'>.btn-grp>.delivered').removeClass('d-none')
        })
      });
}

// list box onclick function, to show order details
$(function(){
    $('.list-box').on('click',function(){
        var list_id = this.id.slice(5)
        window.location = '/business/order-detail/'+list_id
    })
})



//--------------------------- //
// change status for development
const development_status = 2
function change_status(order_id, status_no){
    $.post('/business/change-status/', {id:order_id, status:status_no, csrfmiddlewaretoken : token}, function(response){       
        console.log('done')
      });  
} 
function change_all_status(){
    for(var i=1;i<=2;i++){
        change_status(i,development_status);
    }
}
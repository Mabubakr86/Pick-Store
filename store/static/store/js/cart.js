var cart_btns = document.getElementsByClassName('update-cart')
var cartTotal = document.getElementById('cart-total')

for(var i=0;i<cart_btns.length;i++){
    cart_btns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var endpoint = document.getElementById('endpoint').getAttribute('href');
        $.ajax({
            type:'POST',
            url: endpoint,
            data:{
                'product_id':productId,
                'action':action,
                'csrfmiddlewaretoken':csrftoken,
            },
            success:function(response){
                cartTotal.innerHTML =`${response['order_total']}`
            }
        })
    })

}
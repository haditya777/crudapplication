const addToCart = document.getElementsByClassName('addToCart')
//console.log((addToCart))
if(localStorage.getItem('cartList'))
   {console.log('a')}
else{
    localStorage.setItem('cartList', JSON.stringify({}))
}
    var count = 0
if(localStorage.getItem['count']){
    var count = localStorage.getItem['count']
}
else{
    localStorage.setItem['count'] = count
}

Array.from(addToCart).forEach(element => {
    //console.log(element.id)
    element.addEventListener('click', ()=>{
    
        button = event.currentTarget
        productSrno = button.id.split(':')[1]
        console.log('name'+productSrno)
        console.log(document.getElementById('name:'+productSrno))
        productName = document.getElementById('name:'+productSrno).innerHTML
        productImage = document.getElementById('image:'+productSrno).src
        productQuantity=document.getElementById('quantity:'+productSrno).innerHTML
        productQuantity = productQuantity.split(':')[1]
        productPrice = document.getElementById('price:'+productSrno).innerHTML
        console.log(productPrice)
        userEmail = localStorage.getItem('user')
        jsonObj = {
            'productSrno':productSrno,
            'productName':productName,
            'productImage':productImage,
            'productQuantity':productQuantity,
            'productPrice':productPrice,
            'userEmail':userEmail
        }
        cartList = JSON.parse(localStorage.getItem('cartList'))
        console.log((cartList))
        //newProduct = (JSON.stringify(jsonObj))
        //console.log(newProduct)
        cartList[count] = jsonObj
        count+=1
        //cartList = cartList+newProduct
        //localStorage.setItem('cart', JSON.stringify(jsonObj))
        localStorage.setItem('cartList', JSON.stringify(cartList))
        alert('product added to cart')
        //console.log(productSrno)
        //console.log(buttonId)

    })
});

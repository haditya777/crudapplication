


function loadcart() {
    if(localStorage.getItem('productDict'))
{
    alert('if')
 productDict = JSON.parse(localStorage.getItem('productDict'))
}
else{
    alert('esle')
localStorage.setItem('productDict', JSON.stringify({}))
productDict = {}
}
    divTag = document.getElementById('usercart')

    cartList = localStorage.getItem('cartList')
    cartList = JSON.parse(cartList)

    userEmail = localStorage.getItem('user')
    console.log(cartList)

    var totalPrice = 0.0

    value = ''
    for (objId in cartList) {
        jsonObj = cartList[objId]
        if (jsonObj['userEmail'] == userEmail) {
            console.log(jsonObj)
            console.log(parseFloat(jsonObj['productPrice']))
            totalPrice += parseFloat(jsonObj['productPrice'])
            maxquantity = parseInt(jsonObj['productQuantity'])
            console.log(parseFloat(jsonObj['productPrice']))
            if (jsonObj['productSrno'] in productDict){
            quantity = parseInt(productDict[jsonObj['productSrno']][1])
            }
            else{            
            productDict[jsonObj['productSrno']] = [parseFloat(jsonObj['productPrice']), 1]
            quantity = 1
            }

            value = value + `<div class="row border-top border-bottom">
            <div class="row main align-items-center">
                <div class="col-2"><img class="img-fluid" src="${jsonObj['productImage']}"></div>
                <div class="col">
                    <div class="row text-muted">${jsonObj['productSrno']}</div>
                    <div class="row">${jsonObj['productName']}</div>
                </div>
                <div class="col"> <a class="subtract" value="minus:${jsonObj['productSrno']}" href="#">-</a><a id="quantity:${jsonObj['productSrno']}" href="#" class="border">${quantity}</a><a class="add" value="plus:${jsonObj['productSrno']}" href="#">+</a> </div>
                <div class="col">${jsonObj['productPrice']}</div>
            </div>
        </div>`
        }
        console.log(jsonObj)
    }
    updateTotalPrice()
    console.log(productDict)
    console.log(value)
    divTag.innerHTML = value
    
    minusTag = document.getElementsByClassName('subtract')
    plusTag = document.getElementsByClassName('add')

    Array.from(minusTag).forEach(element => {
        element.addEventListener('click', () => {
            alert('minus')
            tag = event.currentTarget
            value = tag.getAttribute('value')
            console.log(tag)
            console.log(value)
            productSrno = value.split(':')[1]
            console.log('productSrno', productSrno)
            quantity = document.getElementById('quantity:' + productSrno).innerHTML

            quantity = parseInt(quantity)
            if (quantity > 1) {
                quantity = quantity - 1
                productDict[productSrno][1] = quantity
            }
            document.getElementById('quantity:' + productSrno).innerHTML = quantity
            console.log(productDict)
            localStorage.setItem('productDict', JSON.stringify(productDict))
            updateTotalPrice()

        })
    })

    Array.from(plusTag).forEach(element => {
        element.addEventListener('click', () => {
            alert('plus')
            tag = event.currentTarget
            value = tag.getAttribute('value')
            console.log(tag)
            console.log(value)
            productSrno = value.split(':')[1]
            console.log('productSrno', productSrno)
            quantity = document.getElementById('quantity:' + productSrno).innerHTML
            quantity = parseInt(quantity)
console.log(maxquantity)
            if (quantity < maxquantity) {
                quantity = quantity + 1
                productDict[productSrno][1] = quantity
            }

            document.getElementById('quantity:' + productSrno).innerHTML = quantity
            console.log(productDict)
            localStorage.setItem('productDict', JSON.stringify(productDict))
            updateTotalPrice()

        })
    })


}
loadcart()

function updateTotalPrice() {
    totalPrice = 0
    for (srno in productDict) {
        productPrice = productDict[srno][0]
        console.log(productPrice)
        quan = productDict[srno][1]
        totalPrice = totalPrice + (productPrice * quan)
    }
    document.getElementById('totalPrice').innerHTML = totalPrice
}

$(".navbar-burger").click(function () {
 
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  

let carts = document.querySelectorAll('#add-cart');

for (let i=0; i<carts.length; i++){
  carts[i].addEventListener('click', () =>{
    console.log("added to cart")
  })
}
<?php include("header.php"); ?>



<div class="check_shedul">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="shedul_info">
          <ul>
            <li class="active"><p>Order Summery</p></li>
            <li class="active"></li>
            <li class="active"><p>Delivery Address</p></li>
            <li class="active"></li>
            <li class="active"><p>Place Order</p></li>
            <li></li>
            <li><p>Payment</p></li>
            <li></li>
            <li><p>Completation</p></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>





<div class="order-summery">
<div class="container-fluid">
<div class="row">


<div class="col-md-9">
<div class="order-pro">
<div class="order-block">
<h3>Review Your Delivery Address and Order list 
</h3>
</div>
<div class="summ-block-page"> 
<div class="row"> 
<div class="col-md-8">
<div class="order-block-img">
<p>Delivery Address</p> 
<p>Name of Customer</p> 
<p>Address line 1</p> 
<p>Address line 2</p> 
<p>Address line 3</p> 
<span>Would you like to change your Delivery address,then click on <a href="delivery-address.php">CHANGE</a></span>
</div>  
</div>
<div class="col-md-4">
<div class="delivery_to_address">
    <h4><a href="delivery-address.php">Delever to this Address</a></h4>

  </div>
  <div class="edit-block">
      <a href="#">Edit</a>

  </div>

</div>
</div>


<div class="block-block-page list-block">
<h3>Order List</h3>
<div class="row"> 
<div class="col-md-3">
<div class="order-block-img">
<img src="assets/img/cart4.png" alt="">

  <div class="product_variant quantity">
  <label>quantity</label>
  <input min="1" max="100" value="1" type="number">  
  </div>  
</div>  
</div>
<div class="col-md-9">
<div class="order-content-black">
LABOMED VISION 2000 LED</div> 
<div class="pro-duct"><i class="fa fa-inr" aria-hidden="true"></i> 300</div>
<div class="sea-block"><i class="fa fa-inr" aria-hidden="true"></i> 150</div>
<div class="off-block">50% off</div>
<div class="sold-by">Sold by: xyz Company</div>
<div class="sold-by-block-in">Quentity: 2 unit</div>
<div class="cod-abail">COD Available</div>
<div class="remove">Remove</div>
</div>
</div>
</div>

</div>


  
</div>
<div class="continue place-cus-cus">

<a href="payment.php">Place Order</a> 

</div>

</div>


<div class="col-md-3">
<div class="order-pro">
<div class="billing-block total-count">
<h3>Total Billing Amount</h3> 
</div>

<div class="total-amount">
<p>Sub Total<span><i class="fa fa-inr" aria-hidden="true"></i> 500</span></p> 
<p>Shipping Charge<span><i class="fa fa-inr" aria-hidden="true"></i> 40</span></p>    
</div>

<div class="total-amount-block">
<p>Total<span><i class="fa fa-inr" aria-hidden="true"></i> 540</span></p>    
</div>  

<div class="payble abail-abail-block">
<p>Total Payable<span><i class="fa fa-inr" aria-hidden="true"></i> 540</span></p>
<p class="purchase">You are saving <i class="fa fa-inr" aria-hidden="true"></i> 300 on this purchase</p>  
</div>


<a href="payment.php" class="place-btn">Place Order</a>
<div class="safe-block">
  
  <img src="assets/img/safe.png" alt="">
  <p>Safe &amp; Secure Payment</p>
  <img src="assets/img/aw1.png" alt="">
  <p>Quality Seal</p>
  <img src="assets/img/lowes.png" alt="">
  <p>Lowes Price Gurentee</p>
  <img src="assets/img/can.png" alt="">
  <p>Easy Cancelation</p>
  <img src="assets/img/auth.png" alt="">
  <p>100% Authentic Product</p>
</div>
  </div>
</div>




  
</div>  
  
</div>  


  
</div>









<?php include("footer.php");?>
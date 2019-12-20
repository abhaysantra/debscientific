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
            <li class="active"></li>
            <li class="active"><p>Payment</p></li>
            <li></li>
            <li><p>Completation</p></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>



<section class="main-container col1-layout payment_sect">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">

        <div class="page-content page-order">
          
        <div class="page-title method-block">
            <h2>Select Payment Method</h2>
          </div>


        <div class="order-detail-content cradit-block">
         <div class="row">
            <div class="col-md-9">
           <form action="#" method="post">
             <div class="form-group">

                <label class="">
                 <input type="radio" name="radio" checked=""> <span class="label-text">
                 Cradit Card / Debit Card
               </span></label>

                 <label class="">
                <input type="radio" name="radio" checked=""> <span class="label-text">
                 Net Banking
               </span></label>

               <label class="">
                 <input type="radio" name="radio" checked=""> <span class="label-text">
                 BHIM UPI
               </span></label>


               <label class="">
                 <input type="radio" name="radio" checked=""> <span class="label-text">
                 Cash On Delivery
               </span></label>
             </div>
             <div class="form-group">

             </div>
           </form>

        </div>
      <!--   <div class="col-md-3">
          <div class="cart-price">
            <form action="#" method="post">
              <div class="cart-price-title">
                <h3>Price Details</h3>
              </div>
              <div>
                <ul>
                  <li>Quantity : <span>5</span></li>
                  <li>Tax : <span>99.00</span></li>
                  <li>Subtotal : <span>99.00</span></li>
                  <li class="Wallet-input">
                    
                      <input type="text" name="" class="form-control" placeholder="Wallet Point">
                    <button type="submit">Redeem</button>
                    </li>
                  
                </ul>
              </div></form>
              <div class="cart-price-total">
                <h3>Amount Payble <span>Rs.999</span></h3>
              </div>
            
          </div>
        </div> -->
         </div>
        <div class="cart_navigation text-center"> <!-- <a class="continue-btn" href="shopping_cart.php"><i class="fa fa-arrow-left"> </i>&nbsp; Back to Cart</a> --> <a class="checkout-btn process" href="completation.php">Process Order</a> </div>
      </div>
    </div>
  </div>
</div>
</div>
</section>





<?php include("footer.php");?>
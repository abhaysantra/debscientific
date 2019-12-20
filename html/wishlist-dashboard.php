<?php include("header.php"); ?>

 <section class="my-account-wrapper section-padding dashboard_section">
        	<div class="container-fluid">
             <div class="ch-cont">
        		<div class="row clearfix">


        			<div class="col-lg-3 col-md-3 col-sm-4 col-xs-12">
        				

        			
        				<div class="myaccount-sidebar">
        					<div class="profile-content">
        						<div class="profile-image">
                                
                          
        							<img src="assets/img/man.jpg" class="img-responsive" alt="">


                                                
        						</div>
                                 
                               <h4 class="my-name">Shamin Piyada</h4>
                                
                                        						
        					</div>

                      
        					<ul>

    							<li><a href="edit-profile.php" class="active">Edit Profile</a></li>
    							<li><a href="change-password.php">Change Password</a></li>
                                <li><a href="manage-address.php">Manage Addresses</a></li>
    							<li><a href="my-order.php">My Order</a></li>
                                <li><a href="view-cart.php">My Cart</a></li>
    							<li><a href="wishlist-dashboard.php">My Wishlist</a></li>
                                <li><a href="notification.php">All Notification</a></li>
                                <li><a href="wallet.php">My wallet</a></li>
                                <li><a href="#">Log Out</a></li>
    						</ul>
        				</div>        			
                   
        		      		
                    </div>
        			<div class="col-md-9 col-sm-8 col-xs-12">

                    <div class="myaccount-widget">
                              
                             
                            <h3 class="title">My Wishlist</h3>
                            
     <!--wishlist area start -->
    <div class="wishlist_area mt-30">
                <div class="container">   
                    <form action="#"> 
                        <div class="row">
                            <div class="col-12">
                                <div class="table_desc wishlist">
                                    <div class="cart_page table-responsive">
                                        <table>
                                            <thead>
                                                <tr>
                                                    
                                                    <th class="product_thumb">Image</th>
                                                    <th class="product_name">Product</th>
                                                    <th class="product-price">Price</th>
                                                    <th class="product_quantity">Stock Status</th>
                                                    <th class="product_total">Add To Cart</th>
                                                    <th class="product_remove">Delete</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                   
                                                    <td class="product_thumb"><a href="#"><img src="assets/img/cart1.png" alt=""></a></td>
                                                    <td class="product_name"><a href="#">Handbag fringilla</a></td>
                                                    <td class="product-price"><i class="fa fa-inr" aria-hidden="true"></i> 65.00</td>
                                                    <td class="product_quantity">In Stock</td>
                                                    <td class="product_total"><a href="#">Add To Cart</a></td>
                                                    <td class="product_remove"><a href="#">X</a></td>


                                                </tr>

                                                <tr>
                                                 
                                                    <td class="product_thumb"><a href="#"><img src="assets/img/cart2.png" alt=""></a></td>
                                                    <td class="product_name"><a href="#">Handbags justo</a></td>
                                                    <td class="product-price"><i class="fa fa-inr" aria-hidden="true"></i> 90.00</td>
                                                    <td class="product_quantity">In Stock</td>
                                                    <td class="product_total"><a href="#">Add To Cart</a></td>
                                                     <td class="product_remove"><a href="#">X</a></td>


                                                </tr>
                                                <tr>
                                                  
                                                    <td class="product_thumb"><a href="#"><img src="assets/img/cart3.png" alt=""></a></td>
                                                    <td class="product_name"><a href="#">Handbag elit</a></td>
                                                    <td class="product-price"><i class="fa fa-inr" aria-hidden="true"></i> 80.00</td>
                                                    <td class="product_quantity">In Stock</td>
                                                    <td class="product_total"><a href="#">Add To Cart</a></td>
                                                     <td class="product_remove"><a href="#">X</a></td>


                                                </tr>

                                            </tbody>
                                        </table>   
                                    </div>  

                                </div>
                             </div>
                         </div>

                    </form> 
                    
                    
                </div>
            </div>
     <!--wishlist area end -->
                        </div>
    </div>




                    </div>
        		</div>
        	</div>
        </section>




<?php include("footer.php");?>
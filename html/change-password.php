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
        			<div class="col-lg-9 col-md-9 col-sm-8 col-xs-12">
                        <div class="myaccount-widget">
                              
                             
                            <h3 class="title">Change Password</h3>
                            <div class="form-container">
                               <form action="#" name="form" method="post" onsubmit="return testVal()">
                                   <div class="row">
                                       

                                        <div class="col-md-4">
                                            <input type="Password" name="old_pass" id="Txt1" class="form-control" placeholder="Old Password" value="" onkeyup="field1(this.value)"><span id="old_pass_match" style="color:red"></span>
                                        </div>

                                        <div class="col-md-4">
                                            <input type="Password" name="new_pass" id="Txt2" class="form-control" placeholder="New Password" onkeyup="field2(this.value)"><span id="new_pass_match" style="color:red"></span>
                                        </div>
                                        <div class="col-md-4">
                                            <input type="Password" name="confirm_pass" id="Txt3" class="form-control" placeholder="Confirm Password" onkeyup="field3(this.value)"><span id="conf_pass_match" style="color:red"></span>
                                            <input type="hidden" value="1234" name="hidden_pass">
                                     <input type="hidden" value="246" name="user_id">
                                        </div>
                       
                                   
                                   </div>
                                    <div class="text-right">
                                        <button class="checkout-btn">Submit</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>




                    </div>
        		</div>
        	</div>
        </section>




<?php include("footer.php");?>
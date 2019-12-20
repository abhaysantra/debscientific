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
                             
        					<h3 class="title">My Profile</h3>
                            <div class="form-container">
                                <form id="edt_profile" action="" name="form" method="post" enctype="multipart/form-data">
                                   <div class="row">
                                     <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                        <div class="form-group">
                                       <label>First Name<span>*</span></label>
                                            <input type="text" name="fname" id="first_name" class="form-control" placeholder="First Name">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                        <div class="form-group">
                                       <label>Last Name<span>*</span></label>
                                            <input type="text" name="lname" id="last_name" class="form-control" placeholder="Last Name">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <div class="form-group">
                                        <label>Email<span>*</span></label>
                                            <input type="email" class="form-control" id="email" name="email" placeholder="Email">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <div class="form-group">
                                        <label>Phone Number<span>*</span></label>
                                            <input type="text" name="ph_no" id="phn_no1" onkeypress="return event.charCode >= 48 &amp;&amp; event.charCode <= 57" maxlength="10" class="form-control" placeholder="Phone Number">
                                        </div>
                                    </div>

                                     <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <div class="form-group">
                                       <label>Pin Code<span>*</span></label>
                                            <input type="text" name="pin_c" onkeypress="return event.charCode >= 48 &amp;&amp; event.charCode <= 57" maxlength="6" id="pin_code" class="form-control" placeholder="Pin Code" onkeyup="check_zip()">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <div class="form-group">
                                        <label>City<span>*</span></label>
                                            <input type="text" name="city" id="city1" class="form-control" placeholder="City">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 nopadd-left">
                                    <div class="form-group ">
                                       <label>State<span>*</span></label>
                                            <input type="text" name="state" id="state1" class="form-control" placeholder="State">
                                        </div>
                                    </div>
                                     <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <div class="form-group">
                                       <label>Ward No<span>*</span></label>
                                            <input type="text" name="count" id="country" class="form-control" placeholder="Country">
                                        </div>
                                    </div>
                                     
                                    
                       
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                                    <div class="form-group ">
                                        <label>Address<span></span></label>
                                            <textarea class="form-control" name="addr" id="address1" rows="4" placeholder="Address"></textarea>
                                        </div>
                                    </div>

                                      <div class="col-lg-12 col-md-12 col-sm-6 col-xs-12 img-section-p">
                                   	<div class="choose-block">
                                            <img id="prof_pic" src="assets/img/man.jpg" class="img-responsive" alt="" height="70px" width="70px">
                                        </div>
                                        <div class="sub-block">
                                        	 <input type="file" name="img_upload" id="img_upload" onchange="readURL(this);">
                                           </div>
                                           <div class="gg-btn-sec">
                                           <button type="submit" class="btn-p-cus-secs">Submit</button>
                                       </div>
                                        </div>
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
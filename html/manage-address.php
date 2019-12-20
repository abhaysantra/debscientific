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
                        <h3 class="title">Manage Addresses</h3>
                        <div class="form-container">
                            <form id="sign_up" action="#" name="form" method="post">
                                <div class="row">
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                        <div class="form-group">
                                            <label>First Name<span>*</span>
                                            </label>
                                            <input type="text" name="fname" id="first_name" class="form-control" placeholder="First Name">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                        <div class="form-group">
                                            <label>Last Name<span>*</span>
                                            </label>
                                            <input type="text" name="lname" id="last_name" class="form-control" placeholder="Last Name" value="">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Email<span>*</span>
                                            </label>
                                            <input type="text" name="email" id="email1" class="form-control" placeholder="Email">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Phone Number<span>*</span>
                                            </label>
                                            <input type="text" name="ph_no" onkeypress="return event.charCode >= 48 &amp;&amp; event.charCode <= 57" maxlength="10" id="phn_no" class="form-control" placeholder="Phone Number">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Alternate Phone (Optional)<span></span>
                                            </label>
                                            <input type="text" name="phone" id="phone_no" onkeypress="return event.charCode >= 48 &amp;&amp; event.charCode <= 57" maxlength="10" class="form-control" placeholder="Alternate Phone (Optional)">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Pincode<span>*</span>
                                            </label>
                                            <input type="text" name="pin_c" onkeypress="return event.charCode >= 48 &amp;&amp; event.charCode <= 57" maxlength="6" id="pin_code" class="form-control" placeholder="Pincode" onkeyup="check_zip()">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>City/District/Town<span>*</span>
                                            </label>
                                            <input type="text" name="city" id="city1" class="form-control" placeholder="City/District/Town">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>State<span>*</span>
                                            </label>
                                            <input type="text" name="state" id="state1" class="form-control" placeholder="State">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Country<span>*</span>
                                            </label>
                                            <input type="text" name="count" id="country" class="form-control" placeholder="Country">
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Landmark (Optional)<span></span>
                                            </label>
                                            <input type="text" name="landmark" id="landmark1" class="form-control" placeholder="Landmark (Optional)">
                                        </div>
                                    </div>
                                    <div class="col-lg-12 col-md-12 col-sm-6 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Post Office<span>*</span>
                                            </label>
                                            <input type="text" name="post_office" id="post_office" class="form-control" placeholder="Post Office">
                                        </div>
                                    </div>
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 ">
                                        <div class="form-group">
                                            <label>Address<span>*</span>
                                            </label>
                                            <textarea class="form-control" name="addr" id="address" rows="2" placeholder="Address"></textarea>
                                        </div>
                                    </div>
                                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 ">
                                <div class="form-group">
                                <div class="address-type mt-10">
                                <label>Address Type<span>*</span>
                                </label>
                                <br> 
                                <span>
                                <div class="form-check">
                              <label>
                        <input type="checkbox" name="check" checked=""> <span class="label-text">Home</span>
                    </label>
                </div>
                <div class="form-check">
                    <label>
                        <input type="checkbox" name="check"> <span class="label-text">Office/Commercial</span>
                    </label>
                </div>
                           </span>
                            </div>
                            </div>
                                    </div>
                                </div>
                                <div class="col-md-12 no-padding">
                                    <div class="form-group div-block">
                                        <button class="checkout-btn mr-0" onclick=" return address_validation();">Save</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div id="del_address">
                            <div class="col-md-12 no-padding">
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="address-single">
                                            <div class="address-single-top"> <span class="add-type">home</span>
                                                <div class="pull-right">
                                                    <button onclick="document.location.href = '#';" class="add-action-btn edt-btn"><i class="fa fa-pencil"></i>
                                                    </button>
                                                    <button onclick="delete_address_ofc(143)" class="add-action-btn del-btn"><i class="fa fa-trash-o"></i>
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="address-single-detail">
                                                <h4>Pitam Mukherjee</h4>
                                                <p>8436966401</p>
                                                <p>pitam.ion@gmail.com</p>
                                                <p>, kolkata, wb, kolkata.chinerpark, 700137</p>
                                            </div>
                                            <button type="button" onclick="change_status(143)" class="btn btn-info btn-sm"> <span class="glyphicon glyphicon-check"></span> Make default</button>
                                            <!-- </a> -->
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="address-single">
                                            <div class="address-single-top"> <span class="add-action-btn edt-btn">Default</span>
                                                <span class="add-type">home</span>
                                                <div class="pull-right">
                                                    <button onclick="document.location.href = '#';" class="add-action-btn edt-btn"><i class="fa fa-pencil"></i>
                                                    </button>
                                                    <button onclick="delete_address_ofc(144)" class="add-action-btn del-btn"><i class="fa fa-trash-o"></i>
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="address-single-detail">
                                                <h4>Sujan Mondal</h4>
                                                <p>7003647070</p>
                                                <p>sujan.ion@gmail.com</p>
                                                <p>chinerpark, kolkata, wb, kolkata, hooghly, 71223</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="address-single">
                                            <div class="address-single-top"> <span class="add-type">home</span>
                                                <div class="pull-right">
                                                    <button onclick="document.location.href = '#';" class="add-action-btn edt-btn"><i class="fa fa-pencil"></i>
                                                    </button>
                                                    <button onclick="delete_address_ofc(145)" class="add-action-btn del-btn"><i class="fa fa-trash-o"></i>
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="address-single-detail">
                                                <h4>Mojibul Haque</h4>
                                                <p>7003647070</p>
                                                <p>mojibul.ion@gmail.com</p>
                                                <p>chinerpark, kolkata, wb, kolkata, hooghly, 71223</p>
                                            </div>
                                            <button type="button" onclick="change_status(145)" class="btn btn-info btn-sm"> <span class="glyphicon glyphicon-check"></span> Make default</button>
                                            <!-- </a> -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>




                    </div>
        		</div>
        	</div>
        </section>




<?php include("footer.php");?>
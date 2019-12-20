<?php include("header.php"); ?>
<div class="container"> 
<div class="row">	
<div class="col-md-6 offset-md-3">
<div class="enquiry-block">
 
  <form id="contact" action="" method="post">
    <h3>Enquiry Form</h3>
    <h4>Contact us today, and get reply with in 24 hours!</h4>
    <fieldset>
      <input placeholder="Your name" type="text" tabindex="1" required autofocus>
    </fieldset>
    <fieldset>
      <input placeholder="Your Email Address" type="email" tabindex="2" required>
    </fieldset>
    <fieldset>
      <input placeholder="Your Phone Number" type="tel" tabindex="3" required>
    </fieldset>
    <fieldset>
      <input placeholder="Your Web Site starts with http://" type="url" tabindex="4" required>
    </fieldset>
    <fieldset>
      <textarea placeholder="Type your Message Here...." tabindex="5" required></textarea>
    </fieldset>
    <fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Send</button>
    </fieldset>
  </form>
 
  </div>
</div>
</div>
</div>





<?php include("footer.php");?>

<script src='//cdn.tinymce.com/4/tinymce.min.js'></script>
<style type="text/css">
    .thumb-image{float:left;width:100px;position:relative;padding:5px;}
</style>
<script type="text/javascript">
    tinymce.init({
      selector: ".tinyarea",
      theme: "modern",
      menubar: "edit insert tools",
      plugins: [
        "advlist autolink lists link image charmap print preview hr anchor pagebreak",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking save table contextmenu directionality",
        "emoticons template paste textcolor colorpicker textpattern imagetools"
      ],
      toolbar1: "undo redo | styleselect | bold italic| forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist | link preview",
      image_advtab: true
    });
  </script>
<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
        <h1>Product Edit</h1>
        <ol class="breadcrumb">
            <li><a href="<?php echo base_url()?>index.php/admin_dashboard"><i class="fa fa-dashboard" aria-hidden="true"></i>Dashboad</a></li>
            <li class="active">Product Edit</li>
        </ol>
    </section>

    <!-- Main content -->
    <section class="content">
        <div class="row">
            <div class="col-xs-12 table-responsive">
                <div class="box">
                    <div class="box-header">
                        <!--<h3 class="box-title">Category List</h3>-->
                       <!--  <ul class="nav nav-tabs">
                           <li class="active"><a data-toggle="tab" href="#vital_info">Vital Info</a></li>
                          
                       </ul> -->

                    </div>
                    <div class="clearfix"></div>
                    <!-- /.box-header -->
                    <div class="box-body">
                        <div class="tab-content">


                                <div id="vital_info" >
                                    <form action="<?php echo base_url();?>index.php/manage_product/update_product" role="form" method="post" enctype="multipart/form-data">
                                        
                                         <div class="form-group" >
                                            <label for="category" class="col-sm-2 control-label">Product Category <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="category" id="category" style="margin-bottom:12px" >
                                                <option value="">Select Product Category</option>

  <?php $all_parent_category=$this->admin_model->all_parent_category(); ?>
                                                <?php foreach($all_parent_category as $parent_category){ ?>
                                                 <option value="<?php echo $parent_category->category_id; ?>" <?php if($parent_category->category_id==$product_details[0]->cat_id){echo 'selected'; }?>> <?php echo $parent_category->category_name; ?></option>
                                                <?php $all_sub_category=$this->admin_model->all_sub_category($parent_category->category_id); ?>
                                                <?php foreach($all_sub_category as $sub_category){ 
                                                  ?>
                                                  <option value="<?php echo $sub_category->category_id; ?>"<?php if($sub_category->category_id==$product_details[0]->cat_id){echo 'selected'; }?>>
                                                    <?php echo $parent_category->category_name; ?> >
                                                    <?php echo $sub_category->category_name; ?> 
                                                   
                                                  </option>
                                                <?php $all_category=$this->admin_model->all_category($sub_category->category_id); ?>
                                                <?php 
                                                foreach($all_category as $category){ ?>
                                                  <option value="<?php echo $category->category_id; ?>" <?php if($category->category_id==$product_details[0]->cat_id){echo 'selected'; }?>>
                                                    <?php echo $parent_category->category_name; ?> >
                                                    <?php echo $sub_category->category_name; ?> >
                                                    <?php echo $category->category_name; ?>
                                                  </option>
                                                <?php } ?>
                                                <?php } ?>
                                                <?php } ?>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group">
                                            <label for="product_name" class="col-sm-2 control-label">Product Title <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="product_name" id="product_name" style="margin-bottom:12px" onkeyup="catname(this.value)" value="<?php echo @$product_details[0]->product_name;?>"  >
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                       

                                        <div class="form-group" >
                                            <label for="featured" class="col-sm-2 control-label">Is Featured <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="featured" id="featured" style="margin-bottom:12px" >
                                                    <option value="">Select</option>
                                                    <option value="Yes" <?php if(@$product_details[0]->featured=='Yes'){ echo 'selected'; }?>>Yes</option>
                                                    <option value="No" <?php if(@$product_details[0]->featured=='No'){ echo 'selected'; }?>>No</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group" >
                                            <label for="popularity" class="col-sm-2 control-label">Popularity <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="popularity" id="popularity" style="margin-bottom:12px" >
                                                    <option value="Yes" <?php if(@$product_details[0]->popular=='Yes'){ echo 'selected'; }?>>Yes</option>
                                                    <option value="No" <?php if(@$product_details[0]->popular=='No'){ echo 'selected'; }?>>No</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>


                                        <div class="form-group" >
                                            <label for="brand" class="col-sm-2 control-label">Brand <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="brand" id="brand" style="margin-bottom:12px" >
                                                     <option value="">Select A Brand</option>
                                                <?php foreach($brand as $bra){?>     
                                                    <option value="<?php echo $bra->brand_id; ?>" <?php if(@$product_details[0]->brand_id==$bra->brand_id){ echo 'selected'; }?>><?php echo $bra->brand_name; ?></option>
                                                <?php } ?>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                       <div class="form-group" >
                                            <label for="size" class="col-sm-2 control-label">Size Chart  </label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="file" name="size_chart" id="size_chart" onchange="readURL(this);" style="margin-bottom:12px" placeholder="Product Size Chart ">
                                                <input type="hidden" name="hidden_size_chart" value="<?php echo $product_details[0]->size_chart;?>">
                                                <?php
                                        if(@$product_details[0]->size_chart!="")
                                        {
                                            ?>
                                            <img id="prof_pic" src="<?php echo base_url() ?>../assets/upload/chart/<?php echo @$product_details[0]->size_chart; ?>" alt="User Image" style="width:90px;height:90px;" />
                                            <?php
                                        }
                                        else
                                        {
                                            ?>
                                            <img id="prof_pic" src="<?php echo base_url(); ?>../assets/upload/no-image.jpg"  alt="User Image" style="width:90px;height:90px;" />
                                            <?php
                                        }
                                        ?>
                                            </div>
                                        </div>
                                         <div class="clearfix"></div>
                                        
                        <input type="hidden" value="<?php echo @$product_details[0]->id?>" name="edit_id" >
                          <!-- <div class="clearfix"></div>  
                          <div class="form-group">
                                        <label for="type" class="col-sm-2 control-label">Product Type  <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control" type="text" name="product_type" id="pro_type" onchange="get_size(this.value)" style="margin-bottom:12px" >  
                                           <option value="0">Select</option>
                                            <?php foreach($pro_type as $type){ ?>
                                              <option value="<?php echo $type->type_id;?>" <?php if(@$type->type_id==@$product_details[0]->product_type){ echo 'selected';} ?>><?php echo $type->product_type;?></option>
                                              <?php } ?>
                                          </select>
                                        </div>
                                    </div> -->

                                  <div class="clearfix"></div>
                                     <div class="form-group">
                                        <label for="size" class="col-sm-2 control-label">Product Size <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control select2 mb-10" type="text" name="pro_size[]" id="pro_size" style="margin-bottom:12px" multiple >


                        <?php   

                   $this->db->select('*');
                  $this->db->from('tbl_size');

                  $this->db->group_by('size');
                  $query=$this->db->get();
                  $size= $query->result();
    ?>

             <?php for ($i=0; $i <count($size) ; $i++) {     ?>
  
        <option value="<?php echo @$size[$i]->size; ?>" 
      <?php   foreach ($pro_size as $row) {    
                  if(@$size[$i]->size==@$row->product_size){ echo 'selected'; } ?>   <?php } ?>>
                    <?php echo @$size[$i]->size; ?>

                          </option>
                                              <?php } ?>

                                          </select>
                                        </div>
                                    </div><br><br>
                                          
                                        
                                        
                                   
                                   <div class="clearfix"></div>
                                     <div class="form-group">
                                        <label for="color" class="col-sm-2 control-label">Product Color  <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control select2 mb-10" type="text" name="product_color[]" id="pro_color" style="margin-bottom:12px" multiple >
                   <?php   

                    $this->db->select('*');
                    $this->db->from('tbl_color');
                   $this->db->group_by('color_name');
                    $query=$this->db->get();
                    $color= $query->result();





                   //$color=$this->admin_model->selectAll('tbl_color');  ?>

             <?php for ($i=0; $i <count($color) ; $i++) {     ?>
  
        <option value="<?php echo @$color[$i]->color_id; ?>" 
    <?php   foreach ($pro_color as $row) {    
                  if(@$color[$i]->color_id==@$row->color_id){ echo 'selected'; } ?>   <?php } ?>>
                   <?php echo @$color[$i]->color_name; ?>
        
                          </option>
                                              <?php } ?>
                                          </select>
                                        </div>
                                    </div><br><br>
                                    <div class="clearfix"></div>
                                       
                                    <script type="text/javascript">
                                        $("#size").select2();
                                        </script>   

                         

                                         <div class="clearfix"></div>
                                         <div class="form-group" >
                                            <label for="price" class="col-sm-2 control-label">Price: <span style="color:red">*</span></label>
                                            <div class="col-sm-3">
                             <input class="form-control"   type="text" name="mrp_price" id="mrp_price" placeholder="MRP Price" style="margin-bottom:12px" value="<?php echo @$product_details[0]->price; ?>">
                                            </div>
                                            <div class="col-sm-3">
                            <input class="form-control" type="text" name="sale_price" id="sale_price"  style="margin-bottom:12px" placeholder="Sale Price" value="<?php echo @$product_details[0]->net_price; ?>">
                                            </div>
                                             <div class="col-sm-2">
                          <input class="form-control" type="text" name="discount"  id="discount" style="margin-bottom:12px" placeholder="Discount " value="<?php echo @$product_details[0]->discount; ?>" readonly="">
                                            </div>
                                            <div> % </div>
                                        </div>
                                        <div class="clearfix"></div>

                                         <div class="form-group">
                                            <label for="shipping_charge" class="col-sm-2 control-label">Shipping Charge <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="shipping_charge" id="shipping_charge" style="margin-bottom:12px" value="<?php echo @$product_details[0]->shipping_charge; ?>">
                                            </div>
                                        </div>

                                        <div class="clearfix"></div>
                                   <div class="form-group">
                                            <label for="delvr_days" class="col-sm-2 control-label">Delivery Days <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="delvr_days" id="delvr_days" style="margin-bottom:12px" value="<?php echo @$product_details[0]->delivery_days; ?>">
                                            </div>
                                        </div>


                                        <div class="clearfix"></div>
                                   <div class="form-group">
                                            <label for="return_polcy" class="col-sm-2 control-label">Easy Return Policy <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="return_polcy" id="return_polcy" style="margin-bottom:12px" value="<?php echo @$product_details[0]->return_policy; ?>">
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                        <div class="form-group" >
                                            <label for="sku" class="col-sm-2 control-label">Product SKU<span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="sku" id="sku" style="margin-bottom:12px" value="<?php echo @$product_details[0]->sku_id;?>"  >
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        <div class="form-group" >
                                            <label for="sku" class="col-sm-2 control-label">Avaliable Quantity<span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="qty" id="qty" style="margin-bottom:12px" value="<?php echo @$product_details[0]->quantity;?>" onkeypress='return event.charCode >= 48 && event.charCode <= 57' >
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                         <!--  <div class="form-group" >
                                            <label for="manufactured_date" class="col-sm-2 control-label">Manufactured Date</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="manufactured_date" id="manufactured_date" style="margin-bottom:12px" value="<?php echo @$product_details[0]->manufactured_date;?>"  >
                                                <i class="fa fa-calendar form-control-feedback" style="margin-right:12px"></i>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                         <div class="form-group" >
                                            <label for="expiry_date" class="col-sm-2 control-label">Expiry Date</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="expiry_date" id="expiry_date" style="margin-bottom:12px" value="<?php echo @$product_details[0]->expiry_date;?>"  >
                                                 <i class="fa fa-calendar form-control-feedback" style="margin-right:12px"></i>
                                            </div>
                                        </div>  
                                        <div class="clearfix"></div> -->

                                        <div class="form-group" >
                                            <label for="product_descript" class="col-sm-2 control-label">Product Description<span style="color:red">*</span></label>
                                            <div class="col-sm-8">
       <textarea class="tinyarea"  name="product_description" id="product_description" style="height:100px"><?php echo @$product_details[0]->description;?></textarea>
                                            </div>
                                        </div>
                                     
                                        <div class="clearfix"></div>
                                        

                                        <div class="form-group" >
                                            <label for="sku" class="col-sm-2 control-label">Warrenty 
                                              <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="warrenty" id="warrenty" style="margin-bottom:12px" value="<?php echo @$product_details[0]->warrenty;?>">
                                            </div>
                                        </div>
                                         <div class="clearfix"></div>

                                         <div class="form-group">
                                        <label class="col-sm-2 control-label" for="input-weight"> Weight <span style="color:red">*</span>
                                        </label>
                                        <div class="col-sm-5">
                                            <input type="text" name="shipping_weight" id="shipping_weight"  class="form-control" value="<?php echo @$product_details[0]->product_shipping_weight;?>">
                                        </div>
                                        <div class="col-sm-3">
                                          <select class="form-control select" name="shipping_weight_class" id="shipping_weight_class" style="margin-bottom:12px">
                                            <?php 
                        
                                            $id = $product_details[0]->product_shipping_weight_class;
                                            
                                            $pro_name = $this->admin_model->selectOne('tbl_weight_class','weight_class_id',$id);
                                            $pro_weight = $this->admin_model->selectAll('tbl_weight_class');
                
                                            ?>
                                            <?php
                                            foreach($pro_weight as $weight){
                                            ?>
                                            <option value="<?php echo $weight->weight_class_id;?>"
                                            <?php if($weight->weight_class_id==$product_details[0]->product_shipping_weight_class)
                                                {
                                                    echo"selected";
                        
                                                }   
                                            ?>                                              
                                                ><?php echo $weight->weight_class?>
                                            </option>

                                            <?php
                                            }
                                            ?>
                                          </select>
                                        </div>
                                    </div>

                                    <div class="clearfix"></div>

                                  <div class="form-group">
                                        <label class="col-sm-2 control-label" for="input-length"> Package Dimensions(L x W x H) <span style="color:red">*</span>
                                        </label>
                                        <div class="col-sm-8">
                                            <div class="row">
                                                <div class="col-sm-3">
                                                    <input type="text" name="shipping_product_length" value="<?php echo @$product_details[0]->product_shipping_length; ?>" id="shipping_product_length"  class="form-control" style="margin-bottom:12px">
                                                </div>
                                                <div class="col-sm-3">
                                                    <input type="text" name="shipping_product_width" value="<?php echo @$product_details[0]->product_shipping_width; ?>" id=""  class="form-control">
                                                </div>
                                                <div class="col-sm-3">
                                                    <input type="text" name="shipping_product_height" value="<?php echo @$product_details[0]->product_shipping_height; ?>" id="shipping_product_height"  class="form-control">
                                                </div>
                                                <div class="col-sm-3">
                                                  <select class="form-control" name="shipping_dimension_class" id="shipping_dimension_class">
                                                    <?php foreach($dimension_class as $dimension){ ?>
         <option value="<?php echo $dimension->dimension_class_id; ?>" <?php if(@$dimension->dimension_class_id==@$product_details[0]->product_shipping_dimension_class){ echo 'selected';} ?>><?php echo $dimension->dimension_class; ?></option>
                                                      <?php } ?>
                                                  </select>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                      <div class="clearfix"></div>
                                        
                                     
                                        
                                        <div class="form-group" >
                                            <label for="meta_title" class="col-sm-2 control-label">Meta Title</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="meta_title" id="meta_title" style="margin-bottom:12px" value="<?php echo @$product_details[0]->meta_title;?>"  >
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group" >
                                            <label for="meta_key" class="col-sm-2 control-label">Meta Keyword</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="meta_key" id="meta_key" style="margin-bottom:12px" value="<?php echo @$product_details[0]->meta_keyword;?>"  > 
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                        <div class="form-group" >
                                            <label for="meta_description" class="col-sm-2 control-label">Meta Description</label>
                                            <div class="col-sm-8">
   <textarea class="tinyarea"  name="meta_description" id="meta_description" style="height:100px" ><?php echo @$product_details[0]->meta_description;?></textarea>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="clearfix"></div>
                                        <div class="box-footer">
                                        </div>

                                </div>
                                <div class="box-footer" style="margin-top: 10px">
                                     <button type="submit" class="btn btn-primary" onclick="return validate()"> Update</button>
                                    <a href="<?php echo base_url();?>index.php/manage_product"  class="btn btn-danger" style="margin-left:12px">Cancel</a>
                                </div>
                        
                            </form>

                        </div>
                    </div>
                    <!-- /.box-body -->
                </div>

            </div>
            <!-- /.col -->
        </div>
        <!-- /.row -->
    </section>
    <!-- /.content -->

</div>



<script>

        $("#manufactured_date").datepicker({
         startDate: new Date(),
         format: 'dd-mm-yyyy',
         autoclose: true,
         todayHighlight: 1
    });

    $('#expiry_date').datepicker({
        startDate: new Date(),
        format: 'dd-mm-yyyy',
        autoclose: true,
        todayHighlight: 1
    });
</script>
<script type="text/javascript">
function produce_file_box(id)
    {
        //alert(id);
         
        var val=id;
            
            if(val==2)
                {
                     $("#no_2").hide();
                      $("#minus").hide();
                }
            var base_url='<?php echo base_url(); ?>';
            if(val==3)
                {
                    $("#no_"+val).hide();
                   
                }
            if(val==4)
                {
                    $("#no_"+val).hide();
                }
           

            $.ajax({
              
             url:base_url+'index.php/manage_product/file_box_show',
             data:{num:val},
             dataType: "html",
             type: "POST",
             success: function(data){


              $("#more_image_"+id).html(data);
              $("#more_image_"+id).show();

                 
                
              }
             });

    }
          
    
    function hiding_out(val)
    {
    
          var current_div=val-1;          
          $("#more_image_"+current_div).html('');
          $("#more_image_"+current_div).hide();
      
    }

    </script>

<script>
     function catname(value)
      {
        //alert(value);
          
          $.ajax({

              type: "POST",
              dataType:'json',
              url:"<?php echo base_url();?>index.php/manage_product/category_slug_show",
              data: {slug: value},
              async: false,

               success: function(data)
                {
                    var cat_slug_name= data.slug_name;

                      if(cat_slug_name!='')
                        {
                           $('#product_slug').val(cat_slug_name);

                        }
                }
          });
          
     
      }
   </script>
   <script>
  $(function () {
    //Initialize Select2 Elements
    $(".select2").select2();

   
  });
</script>

   <script>
    function validate()
    {

         var category=$('#category').val();

         if(category=="")
         {
            $("#category").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#category").removeClass("glowing-border-red");
         }

         var product_name=$('#product_name').val();

         if(product_name=="")
         {
            $("#product_name").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#product_name").removeClass("glowing-border-red");
         }

         var featured=$('#featured').val();

         if(featured=="")
         {
            $("#featured").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#featured").removeClass("glowing-border-red");
         }
          var brand=$('#brand').val();

         if(brand=="")
         {
            $("#brand").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#brand").removeClass("glowing-border-red");
         }

         var product_type=$('#product_type').val();

         if(product_type=="")
         {
            $("#product_type").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#product_type").removeClass("glowing-border-red");
         }


         var mrp_price=$('#mrp_price').val();

         if(mrp_price=="" || mrp_price<0)
         {
            $("#mrp_price").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#mrp_price").removeClass("glowing-border-red");
         }
         var sale_price=$('#sale_price').val();

         if(sale_price=="" || sale_price<0)
         {
            $("#sale_price").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#sale_price").removeClass("glowing-border-red");
         }
        
         var discount=$('#discount').val();

         if(discount=="" || discount<0)
         {
            $("#discount").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#discount").removeClass("glowing-border-red");
         }
         

          var sku=$('#sku').val();

         if(sku=="")
         {
            $("#sku").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#sku").removeClass("glowing-border-red");
         }
          var qty=$('#qty').val();

         if(qty=="" || qty<0 || qty==0)
         {
            $("#qty").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#qty").removeClass("glowing-border-red");
         }

        

         var shipping_charge=$('#shipping_charge').val();

         if(shipping_charge=="")
         {
            $("#shipping_charge").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#shipping_charge").removeClass("glowing-border-red");
         }

        

         var delvr_days=$('#delvr_days').val();

         if(delvr_days=="")
         {
            $("#delvr_days").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#delvr_days").removeClass("glowing-border-red");
         }

         var return_polcy=$('#return_polcy').val();

         if(return_polcy=="")
         {
            $("#return_polcy").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#return_polcy").removeClass("glowing-border-red");
         }

         
         var warrenty=$('#warrenty').val();

         if(warrenty=="")
         {
            $("#warrenty").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#warrenty").removeClass("glowing-border-red");
         }


         
         var shipping_weight=$('#shipping_weight').val();

         if(shipping_weight=="")
         {
            $("#shipping_weight").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#shipping_weight").removeClass("glowing-border-red");
         }

         var shipping_product_length=$('#shipping_product_length').val();

         if(shipping_product_length=="")
         {
            $("#shipping_product_length").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#shipping_product_length").removeClass("glowing-border-red");
         }

         var shipping_product_width=$('#shipping_product_width').val();

         if(shipping_product_width=="")
         {
            $("#shipping_product_width").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#shipping_product_width").removeClass("glowing-border-red");
         }
         var shipping_product_height=$('#shipping_product_height').val();

         if(shipping_product_height=="")
         {
            $("#shipping_product_height").addClass("glowing-border-red");
            return false;
         }
         else
         {
            $("#shipping_product_height").removeClass("glowing-border-red");
         }

         

         
     
     }


     
</script>

<script type="text/javascript">
  function get_size(value)
  {
    // alert(value);
    var html='<option value="">Select</option>';
    if(value>0){
       $.ajax({

        type: 'POST',
        dataType: 'json',
        url:'<?php echo base_url(); ?>index.php/Manage_product/get_size',
        data: {pro_id: value},
        async: false,
        success: function(data)
        {
          // alert(data[0].product_size);
          for (var i = 0; i < data.length; i++) {
        
        html+='<option value="'+data[i].size+'">'+data[i].size+'</option>';
          
          }
          $('#pro_size').html(html);
         
        }
       });
    }
       else
    {
        $("#pro_size").html(html);
    }
  }
</script>
<script type="text/javascript">
  function catname(value)
  {
    var value=value;
    var new_value=value.replace(" ","-");
    $('#product_slug').val(new_value);
    $('#meta_title').val(new_value);
  }
</script>
<script type="text/javascript">
  function pro_desc(value)
  {
    
    var new_value=value.replace(" ","-");
    $('#meta_description').val(new_value);
    
  }
</script>
<script type="text/javascript">
  $('#mrp_price,#sale_price').on('keyup keypress change',function(e){
    var mrp=$('#mrp_price').val();
    var sale=$('#sale_price').val();
    var total=mrp - sale;
    var percnt=(total*100)/mrp;
    if(mrp=='' || sale==''){
    }
    else {
          $('#discount').val(percnt);

    }
  });
</script>
<script>


    function readURL(input)
    {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#prof_pic')
                    .attr('src', e.target.result)
                    .width(90)
                    .height(90);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

     </script>  
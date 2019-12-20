<style type="text/css">
    .thumb-image{float:left;width:100px;position:relative;padding:5px;}
</style>

<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
        <h1>Product Details</h1>
        <ol class="breadcrumb">
            <li><a href="<?php echo base_url()?>index.php/admin_dashboard"><i class="fa fa-dashboard" aria-hidden="true"></i>Dashboad</a></li>
            <li class="active">Product Details</li>
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
                                    <form action="<?php echo base_url();?>index.php/manage_product/product_insert" role="form" method="post" enctype="multipart/form-data">
                                        
                                         <div class="form-group" >
                                            <label for="category" class="col-sm-2 control-label">Product Category</label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="category" id="category" style="margin-bottom:12px" disabled="">
                                                <option value="">Select Product Category</option>
                                                <?php foreach($category as $cat)

                                                {
                                                    $parent_cat = $cat->parent_category;
                                                    $parent = $this->admin_model->selectone('tbl_category','category_id',$parent_cat);
                                                    $sub_cat = $cat->sub_category;
                                                    $sub = $this->admin_model->selectone('tbl_category','category_id',$sub_cat);

                                                ?>
                                                    
                                                    <option value="<?php echo $cat->category_id;?>" <?php if(@$product_details[0]->cat_id==$cat->category_id){ echo 'selected';}?>><?php if(@$parent[0]->category_name!=""){ echo @$parent[0]->category_name." >> "; } ?><?php if(@$sub[0]->category_name!=""){ echo @$sub[0]->category_name." >> "; } ?><?php echo $cat->category_name; ?></option>
                                                <?php 

                                                } ?>
                                                    
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group">
                                            <label for="product_name" class="col-sm-2 control-label">Product Title</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="product_name" id="product_name" style="margin-bottom:12px" onkeyup="catname(this.value)" value="<?php echo @$product_details[0]->product_name;?>"  disabled>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                       

                                        <div class="form-group" >
                                            <label for="featured" class="col-sm-2 control-label">Is Featured</label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="featured" id="featured" style="margin-bottom:12px" disabled="">
                                                    <option value="">Select</option>
                                                    <option value="Yes" <?php if(@$product_details[0]->featured=='Yes'){ echo 'selected'; }?>>Yes</option>
                                                    <option value="No" <?php if(@$product_details[0]->featured=='No'){ echo 'selected'; }?>>No</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group" >
                                            <label for="availability" class="col-sm-2 control-label">Popularity</label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="availability" id="availability" style="margin-bottom:12px" disabled="">
                                                    <option value="Yes" <?php if(@$product_details[0]->popular=='Yes'){ echo 'selected'; }?>>Yes</option>
                                                    <option value="No" <?php if(@$product_details[0]->popular=='No'){ echo 'selected'; }?>>No</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                        <div class="form-group" >
                                            <label for="brand" class="col-sm-2 control-label">Brand</label>
                                            <div class="col-sm-8">
                                                <select class="form-control" name="brand" id="brand" style="margin-bottom:12px" disabled="">
                                                     <option value="">Select A Brand</option>
                                                <?php foreach($brand as $bra){?>     
                                                    <option value="<?php echo $bra->brand_id; ?>" <?php if(@$product_details[0]->brand_id==$bra->brand_id){ echo 'selected'; }?>><?php echo $bra->brand_name; ?></option>
                                                <?php } ?>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        

                                       <!--  <div class="form-group" >
                                            <label for="price" class="col-sm-2 control-label">Product Images</label>
                                            
                                            <div class="col-sm-2">
                                            <?php foreach($product_image as $image){?>
                                                <img src="<?php echo base_url();?>../assets/upload/product/<?php echo $image->image;?>" height="100px" width="100px"> 
                                            <?php  } ?>
                                            </div>
                                            <div class="clearfix"></div>
                                            
                                        </div> -->

                          
                                        <div class="clearfix"></div>

                                        <div class="form-group">
                                        <label for="type" class="col-sm-2 control-label">Product Type  <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control" type="text" name="product_type" id="pro_type" onchange="get_size(this.value)" style="margin-bottom:12px" disabled>  
                                           <option value="0">Select</option>
                                            <?php foreach($pro_type as $type){ ?>
                                              <option value="<?php echo $type->type_id;?>" <?php if(@$type->type_id==@$product_details[0]->product_type){ echo 'selected';} ?>><?php echo $type->product_type;?></option>
                                              <?php } ?>
                                          </select>
                                        </div>
                                    </div>
                     

                                  <div class="clearfix"></div>
                                     <div class="form-group">
                                        <label for="size" class="col-sm-2 control-label">Product Size <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control select2 mb-10" type="text" name="pro_size[]" id="pro_size" style="margin-bottom:12px" multiple  disabled>
                   <?php 
                          $id=@$product_details[0]->id;
                     $size=$this->admin_model->selectOne('tbl_product_size','product_id',$id);  ?>

                     <?php for ($i=0; $i <count($size) ; $i++) { ?>
                                   
  
    <option value="<?php echo @$size->size_id; ?>" <?php  if(@$size[$i]->product_id==@$product_details[0]->id){ echo 'selected'; } ?>> 
                   <?php echo @$size[$i]->product_size; ?>
        
                          </option>
                                              <?php } ?>
                                        
                                          </select>
                                        </div>
                                    </div><br><br>
                                          
                                
                                        
                                   

                                

                                   <div class="clearfix"></div>
                                     <div class="form-group">
                                        <label for="color" class="col-sm-2 control-label">Product Color  <span style="color:red">*</span></label>
                                        
                                        <div class="col-sm-8">
                                          <select class="form-control select2 mb-10" type="text" name="product_color[]" id="pro_color" style="margin-bottom:12px" multiple  disabled>
               <?php   $color=$this->admin_model->selectAll('tbl_color');  ?>

                     <?php for ($i=0; $i <count($color) ; $i++) { 
                                       ?>
  
        <option value="<?php echo @$color->color_id; ?>" 
    <?php   foreach ($pro_color as $row) {    if(@$color[$i]->color_id==@$row->color_id){ echo 'selected'; } ?>   <?php } ?>>
                   <?php echo @$color[$i]->color_code; ?>
        
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
                             <input class="form-control"   type="text" name="mrp_price" id="mrp_price" placeholder="MRP Price" style="margin-bottom:12px" value="<?php echo @$product_details[0]->price; ?>" disabled>
                                            </div>
                                            <div class="col-sm-3">
                            <input class="form-control" type="text" name="sale_price" id="sale_price"  style="margin-bottom:12px" placeholder="Sale Price" value="<?php echo @$product_details[0]->net_price; ?>" disabled>
                                            </div>
                                             <div class="col-sm-2">
                          <input class="form-control" type="text" name="discount"  id="discount" style="margin-bottom:12px" placeholder="Discount " value="<?php echo @$product_details[0]->discount; ?>" disabled>
                                            </div>
                                            <div> % </div>
                                        </div>
                                        <div class="clearfix"></div>

                                         <div class="form-group">
                                            <label for="shipping_charge" class="col-sm-2 control-label">Shipping Charge <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="shipping_charge" id="shipping_charge" style="margin-bottom:12px" value="<?php echo @$product_details[0]->shipping_charge; ?>" disabled>
                                            </div>
                                        </div>

                                        <div class="clearfix"></div>
                                   <div class="form-group">
                                            <label for="delvr_days" class="col-sm-2 control-label">Delivery Days <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="delvr_days" id="delvr_days" style="margin-bottom:12px" value="<?php echo @$product_details[0]->delivery_days; ?>" disabled>
                                            </div>
                                        </div>


                                        <div class="clearfix"></div>
                                   <div class="form-group">
                                            <label for="return_polcy" class="col-sm-2 control-label">Easy Return Policy <span style="color:red">*</span></label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="return_polcy" id="return_polcy" style="margin-bottom:12px" value="<?php echo @$product_details[0]->return_policy; ?>" disabled>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                        <div class="form-group" >
                                            <label for="sku" class="col-sm-2 control-label">Product SKU</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="sku" id="sku" style="margin-bottom:12px" value="<?php echo @$product_details[0]->sku_id;?>"  disabled>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <!--  <div class="form-group" >
                                            <label for="manufactured_date" class="col-sm-2 control-label">Manufactured Date</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="manufactured_date" id="manufactured_date" style="margin-bottom:12px" value="<?php echo @$product_details[0]->manufactured_date;?>"  disabled>
                                                <i class="fa fa-calendar form-control-feedback" style="margin-right:12px"></i>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                         <div class="form-group" >
                                            <label for="expiry_date" class="col-sm-2 control-label">Expiry Date</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="expiry_date" id="expiry_date" style="margin-bottom:12px" value="<?php echo @$product_details[0]->expiry_date;?>"  disabled>
                                                 <i class="fa fa-calendar form-control-feedback" style="margin-right:12px"></i>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div> -->

                                        <div class="form-group" >
                                            <label for="product_descript" class="col-sm-2 control-label">Product Description</label>
                                            <div class="col-sm-8">
                                                <textarea class="form-control"  name="product_description" id="product_description" style="margin-bottom:12px" rows="4" disabled=""><?php echo @$product_details[0]->description;?></textarea>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                      
                                        
                                        <div class="form-group" >
                                            <label for="meta_title" class="col-sm-2 control-label">Meta Title</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="meta_title" id="meta_title" style="margin-bottom:12px" value="<?php echo @$product_details[0]->meta_title;?>"  disabled>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="form-group" >
                                            <label for="meta_key" class="col-sm-2 control-label">Meta Keyword</label>
                                            <div class="col-sm-8">
                                                <input class="form-control" type="text" name="meta_key" id="meta_key" style="margin-bottom:12px" value="<?php echo @$product_details[0]->meta_keyword;?>"  disabled> 
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>
                                        
                                        <div class="form-group" >
                                            <label for="meta_description" class="col-sm-2 control-label">Meta Description</label>
                                            <div class="col-sm-8">
                                                <textarea class="form-control"  name="meta_description" id="meta_description" style="margin-bottom:12px" rows="4" disabled=""><?php echo @$product_details[0]->meta_description;?></textarea>
                                            </div>
                                        </div>
                                        <div class="clearfix"></div>

                                        <div class="clearfix"></div>
                                        <div class="box-footer">
                                        </div>

                                </div>


                            
                                <div class="box-footer" style="margin-top: 10px">
                                    
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
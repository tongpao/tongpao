// JavaScript Document
$(document).ready(function(){
	//newlist start
			var flag = 0;
			var item_index = 0;
			function isDisabled(){
				if(item_index==0){
					$('#previous').parent('li').addClass('disabled');
					$('#firstPage').parent('li').addClass('disabled');	
				}else{
					$('#previous').parent('li').removeClass('disabled');
					$('#firstPage').parent('li').removeClass('disabled'); 	
				}
				if(item_index==19){
					$('#next').parent('li').addClass('disabled');
					$('#lastPage').parent('li').addClass('disabled');	
				}else{ 
					$('#next').parent('li').removeClass('disabled');
					$('#lastPage').parent('li').removeClass('disabled');		
				}	
			}
			isDisabled();
			$('#next').bind('click',function(e){ 
				if(item_index==19){
					return false;
					}
				flag = flag+1; 
				item_index = item_index+1;
				$('.pageindex').children('li').removeClass('active');
				$('.pageindex li:eq('+item_index+')').addClass('active');
				
            	var itemWidth = $('.pageindex').children('li').outerWidth();
				var moveFactor = parseInt($('.pageindex').css('left'))-itemWidth;
				$('.pageindex').animate({'left':moveFactor},'slow','linear');
                isDisabled();             
       		});
			$('#previous').bind('click',function(){
				if(item_index==0){
					return false;
					}  
				flag = flag-1; 
				item_index = item_index-1;
				$('.pageindex').children('li').removeClass('active');
				$('.pageindex li:eq('+item_index+')').addClass('active');
            	var itemWidth = $('.pageindex').children('li').outerWidth();
				var moveFactor = parseInt($('.pageindex').css('left'))+itemWidth;
				$('.pageindex').animate({'left':moveFactor},'slow','linear');
                isDisabled();             
       		});
			$('.pageindex li a').bind('click',function(){
				item_index = $(this).attr('id')-1;//过滤器：:eq(index)和:gt(index)和:lt(index)中的index是从0开始的
				if(!$(this).parent('li').hasClass('active')){					 	
						$(this).parents('ul').children('li').removeClass('active');
						$('.pageindex li:eq('+item_index+')').addClass('active');
					}
				
				var item_num = parseInt(item_index)-(flag + 4);
				var itemWidth = $('.pageindex').children('li').outerWidth();
				var moveFactor = parseInt($('.pageindex').css('left'))-item_num * itemWidth;
				
				$('.pageindex').animate({'left':moveFactor},'slow','linear');
					
				isDisabled();
				flag = item_index-4;
			});
			$('#firstPage').click(function(){
					flag = 0;
					item_index = 0;
					$('.pageindex').animate({'left':'0px'},'slow','linear');
					$('.pageindex li').removeClass('active');
					$('.pageindex li:eq('+item_index+')').addClass('active');
					isDisabled();
			});
			$('#lastPage').click(function(){
					flag = 14; 
					item_index = 19;
					var item_num = '12';
					var itemWidth = $('.pageindex').children('li').outerWidth();
					var moveFactor = 0-item_num * itemWidth;
					$('.pageindex').animate({'left':moveFactor},'slow','linear');
					$('.pageindex li').removeClass('active');
					$('.pageindex li:eq('+19+')').addClass('active');
					isDisabled();
			});
	//newslist end
	//index.html 轮播start
	$('#artCarousel').carousel({
      interval: 4000,
      cycle: true
    });
	//index.html 轮播end
	 //index.html 圆圈start
	 $('.list3_outter.list3_news').hover(
		
		function(){
			$('.list3_news .list3_inner,.list3_news .list3_cover .introduction').css('display','block');
			$('.list3_news .list3_cover').css('background','rgba(0,0,0,.9)');
		},
		function(){
			$('.list3_news .list3_inner,.list3_cover .introduction').css('display','none');
			$('.list3_news .list3_cover').css('background','rgba(0,0,0,.1)');
		}
	);
	$('.list3_outter.list3_members').hover(
		
		function(){
			$('.list3_members .list3_inner,.list3_members .list3_cover .introduction').css('display','block');
			$('.list3_members .list3_cover').css('background','rgba(0,0,0,.9)');
		},
		function(){
			$('.list3_members .list3_inner,.list3_cover .introduction').css('display','none');
			$('.list3_members .list3_cover').css('background','rgba(0,0,0,.1)');
		}
	);
	$('.list3_outter.list3_honer').hover(
		
		function(){
			$('.list3_honer .list3_inner,.list3_honer .list3_cover .introduction').css('display','block');
			$('.list3_honer .list3_cover').css('background','rgba(0,0,0,.9)');
		},
		function(){
			$('.list3_honer .list3_inner,.list3_cover .introduction').css('display','none');
			$('.list3_honer .list3_cover').css('background','rgba(0,0,0,.1)');
		}
	);
	//index.html 圆圈end
});
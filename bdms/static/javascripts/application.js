$(function() {
  // Advanced Search: Filters
  $('.filters-menu').on('click', function(e) {
    e.stopPropagation();
  });

  $('.data-table').dataTable();
});



function hideUnhide(element,parent_element){
   $('.sub-menu').hide();
   $('.category-container').removeClass('category-container');
   parent_element.parent().addClass('category-container');
   if (element.is(':visible')){
        element.hide();
   }
   else{
       element.show();
   }
}

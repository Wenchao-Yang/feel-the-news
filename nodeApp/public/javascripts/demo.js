// Populate News Table with Database information
//var getAllPosting = $.pos('/users/getAll');
//getAllPosting.done(function(data) {
//  // Will arrive in array form
//  $(jQuery.parseJSON(JSON.stringify(data))).each(function() {
//    add(this);
//  });
//});
// General Add News Row, Handles Delete & Update
function add(data) {

  // Unique id for the rows, remove all non alphabets and numbers
  id = data.url.replace(/[^A-Za-z0-9]/g, '');
  var htmlResult = '<tr class=\"'+id+'\"><td>'+'<a href=\"'+data.url+'\" target=\"_blank\">'+ data.title+'</a>'+'</td><td>'+data.description+'</td><td>'+data.senRate+'</td><td>'+data.readRate+'</td><td>'+data.readby+'</td><td><button>Delete</button></td></tr>';

  $('#newsTable').append(htmlResult);

  // Delete on Click
  function remove(id, newsURL){
    $('.'+id).remove();
    // Remove from database
    var removePosting = $.post('/users/remove', {url: newsURL});
    removePosting.done(function(data){
      alert(data);
    });
  }
  $('.' + id).show().find('button').click(remove.bind(null, id, data.url));

  // Update Read status
  function updateRead(id, newsURL){
    $('.' + id).find('td:nth-child(5)').text('Read');
    var updateReadPosting = $.post('/users/updateRead', {url: newsURL});
    updateReadPosting.done(function(data){
      alert(data);
    });
  }
  $('.' + id).show().find('a').click(updateRead.bind(null, id, data.url));
}

// Readability Query
$('#readDrop').change(function() {
  var number = $(this).find('option:selected').attr('data-number');
  var readQueryPosting = $.post('/users/readQuery', {'type': number});
  readQueryPosting.done(function(data){
    // Will arrive in array form
    if (data != {}) {
        $(jQuery.parseJSON(JSON.stringify(data))).each(function() {
          add(this);
        });
    }
  });
});

// Crawl World News
$("#crawlBBC").click(function() {
  var posting = $.post('/users/crawlBBCWorld');
  posting.done(function(data) {
    // Will arrive in array form
    if (data != {}) {
        $(jQuery.parseJSON(JSON.stringify(data))).each(function() {
          add(this);
        });
    }
  });

});

// Analyze URL Form
$("#urlInput").submit(function(event){

  // Stop form from default submit
  event.preventDefault();

  // Get url
  var $form = $( this ),
    urlQuery = $form.find("input[name='urlQuery']").val(),
    act = $form.attr("action");

  // Send data using post
  var posting = $.post(act, { url: urlQuery });


  // Receive results and modify webpage
  posting.done(add);
  this.reset();
});

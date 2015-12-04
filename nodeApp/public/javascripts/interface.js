var CSRF_HEADER = 'X-CSRF-Token';

var setCSRFToken = function (securityToken) {
  jQuery.ajaxPrefilter(function (options, _, xhr) {
    if (!xhr.crossDomain) {
      xhr.setRequestHeader(CSRF_HEADER, securityToken);
    }
  });
};

setCSRFToken($('meta[name="_csrf"]').attr('value'));

// Populate News Table with Database information
var getAllPosting = $.post('/users/normalQuery', {});
getAllPosting.done(function(data) {
  // Will arrive in array form
  $(data).each(function() {
    add(this);
  });
});

// Get User Likes
$.post('/users/getLikesURL').done(function(data) {
    $(data).each(function() {
        var id = this.url.replace(/[^A-Za-z0-9]/g, '');
        $('.'+id).show().find('button').text('Unlike');
    });
});


// General Add News Row, Handles Delete & Update
function add(data) {

  // Unique id for the rows, remove all non alphabets and numbers
  var id = data.url.replace(/[^A-Za-z0-9]/g, '');
  var htmlResult = '<tr class=\"'+id+'\"><td>'+'<a href=\"'+data.url+'\" target=\"_blank\">'+ data.title+'</a>'+'</td><td>'+data.description+'</td><td>'+data.senRate+'</td><td>'+data.readRate+'</td><td>'+data.category+'</td><td><button>Like</button></td></tr>';
  $('#newsTable').append(htmlResult);

  // Insert Like on Click
  function likeUnlike(id, newsURL){
    if ($('.'+id).show().find('button').text() == 'Like') {
        // add like to database
        $.post('/users/like', {url: newsURL});
        $('.'+id).show().find('button').text('Unlike');
    } else {
        // remove like to database
        $.post('/users/removeLike', {url: newsURL});
        $('.'+id).show().find('button').text('Like');
    }
  }
  $('.' + id).show().find('button').click(likeUnlike.bind(null, id, data.url));
}

// Query
$('.selectDrop').change(function() {
  // Prepare Query
  var query = {};
  var readRateLowSelected = $('#readDrop').find('option:selected').attr('readRateLow');
  var readRateHighSelected = $('#readDrop').find('option:selected').attr('readRateHigh');
  var senRateSelected = $('#senDrop').find('option:selected').attr('senRate');
  var categorySelected = $('#catDrop').find('option:selected').attr('category');
  if (readRateLowSelected)
    query.readRateLow = readRateLowSelected;
  if (readRateHighSelected)
    query.readRateHigh = readRateHighSelected;
  if (senRateSelected)
    query.senRate = senRateSelected;
  if (categorySelected)
    query.category = categorySelected;

  var readQueryPosting = $.post('/users/normalQuery', query);
  // Empty Table
  $('#newsStats').empty();
  readQueryPosting.done(function(data){
    // Will arrive in array form
    if (data != {}) {
        $(jQuery.parseJSON(JSON.stringify(data))).each(function() {
          add(this);
        });
    }
  });
  // Get User Likes
  $.post('/users/getLikesURL').done(function(data) {
      $(data).each(function() {
          var id = this.url.replace(/[^A-Za-z0-9]/g, '');
          $('.'+id).show().find('button').text('Unlike');
      });
  });
});

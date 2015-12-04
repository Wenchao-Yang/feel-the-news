var CSRF_HEADER = 'X-CSRF-Token';

var setCSRFToken = function (securityToken) {
  jQuery.ajaxPrefilter(function (options, _, xhr) {
    if (!xhr.crossDomain) {
      xhr.setRequestHeader(CSRF_HEADER, securityToken);
    }
  });
};

setCSRFToken($('meta[name="_csrf"]').attr('value'));

// Get User Added Articles
var getUserArticles = $.post('/users/getUserAddedArticles');
getUserArticles.done(function(data) {
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
